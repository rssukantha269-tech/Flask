from flask import Flask, render_template
from flask_login import LoginManager
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# ---------------- USER MODEL ----------------
class User:
    def __init__(self, user):
        self.id = str(user["_id"])
        self.username = user["username"]
        self.email = user["email"]

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self): return True
    @property
    def is_active(self): return True
    @property
    def is_anonymous(self): return False


@login_manager.user_loader
def load_user(user_id):
    from bson.objectid import ObjectId
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return User(user) if user else None


# ---------------- BLUEPRINTS ----------------
from routes.auth import bp as auth_bp
from routes.booking import bp as booking_bp

app.register_blueprint(auth_bp)
app.register_blueprint(booking_bp)


# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
