"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avotype, AvotypeSchema, Avocado


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    avotype = Avotype.query.order_by(Avotype.typeid).all()

    # Serialize the data for the response
    avotype_schema = AvotypeSchema(many=True)
    data = avotype_schema.dump(avotype)
    return data


def read_one(typeid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    avotype = (
        Avotype.query.filter(Avotype.typeid == typeid)
        .outerjoin(Avocado)
        .one_or_none()
    )

    # Did we find a person?
    if avotype is not None:

        # Serialize the data for the response
        avotype_schema = AvotypeSchema()
        data = avotype_schema.dump(avotype)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo type not found for Id: {typeid}")


def create(avotype):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    typeid = avotype.get("typeid")
    type = avotype.get("type")

    existing_avotype = (
        Avotype.query.filter(Avotype.typeid == typeid)
        .filter(Avotype.type == type)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_avotype is None:

        # Create a person instance using the schema and the passed in person
        schema = AvotypeSchema()
        new_avotype = schema.load(avotype, session=db.session)

        # Add the person to the database
        db.session.add(new_avotype)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_avotype)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f"Avo type {type} exists already")


def update(typeid, avotype):
    """
    This function updates an existing person in the people structure
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_avotype = Avotype.query.filter(
        Avotype.typeid == typeid
    ).one_or_none()

    # Did we find an existing person?
    if update_avotype is not None:

        # turn the passed in person into a db object
        schema = AvotypeSchema()
        update = schema.load(avotype, session=db.session)

        # Set the id to the person we want to update
        update.typeid = update_avotype.typeid

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_avotype)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo type not found for Id: {typeid}")


def delete(typeid):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    avotype = Avotype.query.filter(Avotype.typeid == typeid).one_or_none()

    # Did we find a person?
    if avotype is not None:
        db.session.delete(avotype)
        db.session.commit()
        return make_response(f"Avo type {typeid} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avo type not found for Id: {typeid}")