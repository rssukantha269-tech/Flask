from flask import Flask, render_template
from flask_login import LoginManager
from flask_pymongo import PyMongo
from config import Config   # ✅ works when app.py is root file

app = Flask(__name__)
app.config.from_object(Config)

# MongoDB
mongo = PyMongo(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# -------------------------------
# User class
# -------------------------------
class User:
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.username = user_data["username"]
        self.email = user_data["email"]
        self.password = user_data["password"]

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


@login_manager.user_loader
def load_user(user_id):
    from bson.objectid import ObjectId
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_data)
    return None


# -------------------------------
# Blueprints (IMPORTANT FIX)
# -------------------------------
from routes.auth import bp as auth_bp
from routes.booking import bp as booking_bp

app.register_blueprint(auth_bp)
app.register_blueprint(booking_bp)


# -------------------------------
# Home page
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -------------------------------
# Run app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
