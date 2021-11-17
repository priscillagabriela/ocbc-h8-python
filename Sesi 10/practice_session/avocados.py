"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avoregion, Avotype, Avocado, AvocadoSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp
    :return:                json list of all notes for all people
    """
    # Query the database for all the notes
    avocados = Avocado.query.order_by(db.desc(Avocado.date)).all()

    # Serialize the list of notes from our data
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocados)
    return data


def read_one(regionid, typeid, avoid):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person
    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    avocado = (
        Avocado.query.join(Avoregion, Avoregion.regionid == Avocado.regionid)
        .filter(Avoregion.regionid == regionid)
        .join(Avotype, Avotype.typeid == Avocado.type)
        .filter(Avocado.type == typeid)
        .filter(Avocado.avoid == avoid)
        .one_or_none()
    )

    # Was a note found?
    if avocado is not None:
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Avocado not found")


def create(regionid, typeid, avocado):
    """
    This function creates a new note related to the passed in person id.
    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    avoregion = Avoregion.query.filter(Avoregion.regionid == regionid).one_or_none()
    
    avotype = Avotype.query.filter(Avotype.typeid == typeid).one_or_none()

    # Was a person found?
    if avoregion is None or avotype is None:
        abort(404, f"Avoregion or avotype not found for Id: {regionid} or Id: {typeid}")

    # Create a note schema instance
    schema = AvocadoSchema()
    new_avocado = schema.load(avocado, session=db.session)

    # Add the note to the person and database
    avoregion.avocados.append(new_avocado)
    avotype.avocados.append(new_avocado)
    # db.session.add(new_avocado)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_avocado)

    return data, 201


def update(regionid, typeid, avoid, avocado):
    """
    This function updates an existing note related to the passed in
    person id.
    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_avocado = (
        Avocado.query.filter(Avoregion.regionid == regionid)
        .filter(Avotype.typeid == typeid)
        .filter(Avocado.avoid == avoid)
        .one_or_none()
    )

    # Did we find an existing note?
    if update_avocado is not None:

        # turn the passed in note into a db object
        schema = AvocadoSchema()
        update = schema.load(avocado, session=db.session)

        # Set the id's to the note we want to update
        update.regionid = update_avocado.regionid
        update.type = update_avocado.type

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_avocado)

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Avocado not found")


def delete(regionid, typeid, avoid):
    """
    This function deletes a note from the note structure
    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the note requested
    avocado = (
        Avocado.query.filter(Avoregion.regionid == regionid)
        .filter(Avotype.typeid == typeid)
        .filter(Avocado.avoid == avoid)
        .one_or_none()
    )

    # did we find a note?
    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            "Avocado deleted", 200
        )

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Avocado not found")