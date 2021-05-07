from flask import flask
application = flask(__name__)

@application.route("/")
def hello():
    return "Hello World Usachev!"

if __name__ == "__main__":
    application.run()
