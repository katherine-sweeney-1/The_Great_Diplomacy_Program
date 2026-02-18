import os
from flask import Flask

app = Flask(__name__, instance_relative_config = True)
"""
@app.route("/")
def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = "password",
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok = True)
    @app.route("/hello")
    def hello():
        return "Hello World!!!"
    return app
"""
app = Flask(__name__)

@app.route("/https://the-great-diplomacy-program.netlify.app/")
def hello():
    return "Hello World!!!"

# runs if I use http://127.0.0.1:5000/hello
if __name__ == "__main__":
    app.run("localhost", 5000)



