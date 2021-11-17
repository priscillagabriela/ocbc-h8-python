"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avoregion, AvoregionSchema, Avocado


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    avoregion = Avoregion.query.order_by(Avoregion.regionid).all()

    # Serialize the data for the response
    avoregion_schema = AvoregionSchema(many=True)
    data = avoregion_schema.dump(avoregion)
    return data


def read_one(regionid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    avoregion = (
        Avoregion.query.filter(Avoregion.regionid == regionid)
        .outerjoin(Avocado)
        .one_or_none()
    )

    # Did we find a person?
    if avoregion is not None:

        # Serialize the data for the response
        avoregion_schema = AvoregionSchema()
        data = avoregion_schema.dump(avoregion)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo region not found for Id: {regionid}")


def create(avoregion):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    regionid = avoregion.get("regionid")
    region = avoregion.get("region")

    existing_avoregion = (
        Avoregion.query.filter(Avoregion.regionid == regionid)
        .filter(Avoregion.region == region)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_avoregion is None:

        # Create a person instance using the schema and the passed in person
        schema = AvoregionSchema()
        new_avoregion = schema.load(avoregion, session=db.session)

        # Add the person to the database
        db.session.add(new_avoregion)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_avoregion)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f"Avo region {region} exists already")


def update(regionid, avoregion):
    """
    This function updates an existing person in the people structure
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_avoregion = Avoregion.query.filter(
        Avoregion.regionid == regionid
    ).one_or_none()

    # Did we find an existing person?
    if update_avoregion is not None:

        # turn the passed in person into a db object
        schema = AvoregionSchema()
        update = schema.load(avoregion, session=db.session)

        # Set the id to the person we want to update
        update.regionid = update_avoregion.regionid

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_avoregion)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo region not found for Id: {regionid}")


def delete(regionid):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    avoregion = Avoregion.query.filter(Avoregion.regionid == regionid).one_or_none()

    # Did we find a person?
    if avoregion is not None:
        db.session.delete(avoregion)
        db.session.commit()
        return make_response(f"Avo region {regionid} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo region not found for Id: {regionid}")