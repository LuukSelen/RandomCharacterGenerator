# We will start working on the first version of our flask application.
# Our application is intended for Dungeon Masters and it helps them generate random NPC's
# The flask application should have a single route under the '/' url (base url).
# Upon visiting this URL the user should be presented with a nice GUI containing all the information to run the NPC.
    # Information that is required: Name, Gender, Race, Job
    # Add your own stuff! Think about what information can be added to make the NPC feel more alive (eye-color, hair-color, weight, maybe pets?)
    # Present this information using Flask templating to generate HTML and CSS
# The url should take an optional URL parameter that specifies the first name of the NPC. I.e. : http://127.0.0.1:5000?name=Hans should return an NPC with the first name "Hans" 
 
# Tips:
    # Want to know more about flask routing? -> https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
    # Want to know how to use templates to generate HTML? -> https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
        # Want to know more about Jinja templates and the available commands? Check -> https://jinja.palletsprojects.com/en/2.10.x/templates/
    # Want to know how to include 'static' files like CSS? -> https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
    # Want to know how to acces URL parameters? -> https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
    # Try to write the random generator for NPC's first and then put it in your flask application if you prefer.
    # Reading and googling are essential skills for a developer, get used to reading documentation.
