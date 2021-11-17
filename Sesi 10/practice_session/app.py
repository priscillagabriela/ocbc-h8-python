"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# Local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


# Create a URL route in our application for "/avoregion"
@connex_app.route("/avoregion")
@connex_app.route("/avoregion/<int:regionid>")
def avoregion(regionid=""):
    """
    This function just responds to the browser URL
    localhost:5000/avoregion
    :return:        the rendered template "avoregion.html"
    """
    return render_template("avoregion.html", regionid=regionid)

# Create a URL route in our application for "/avoregion"
@connex_app.route("/avotype")
@connex_app.route("/avotype/<int:typeid>")
def avotype(typeid=""):
    """
    This function just responds to the browser URL
    localhost:5000/avotype
    :return:        the rendered template "avotype.html"
    """
    return render_template("avotype.html", typeid=typeid)

# Create a URL route to the notes page
@connex_app.route("/avoregion/<int:regionid>")
@connex_app.route("/avoregion/<int:regionid>/avotype/<int:typeid>/avocados")
@connex_app.route("/avoregion/<int:regionid>/avotype/<int:typeid>")
def notes(regionid, typeid=""):
    """
    This function responds to the browser URL
    localhost:5000/avocados/<person_id>
    :param person_id:   Id of the person to show notes for
    :return:            the rendered template "notes.html"
    """
    return render_template("avocados.html", regionid=regionid, typeid=typeid)


if __name__ == "__main__":
    connex_app.run(host='localhost', port=5000, debug=True)