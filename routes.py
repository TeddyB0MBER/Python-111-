from flask import Flask  # from the flask module import the Flask class


# Create an instance of the Flask class into the app (now an object)
# class is to object as blueprint is to house.
app = Flask(__name__)


@app.get("/")   # a decorator that allows us to map a route to a "view function"
def index():  # flask calls functions mapped to a route "view functions"
    out = {  # flask will automatically convert dictionaries to json for convenience
        "first_name": "John",
        "last_name": "Doe",
        "hobbies": "Illustration",
        "is_active": True
    }
    return out  # if we wish to build a restful service, this is a good convention  to follow
    # as JSON is the norm for the morst RESTful services
