# USER MODEL
from flask_login import UserMixin
from werkzeug.security import check_password_hash

from root.globals import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Load the user object from the user ID stored in the session"""
    return User.objects(pk=user_id).first()


class User(db.Document, UserMixin):
    """
    USER MODEL
    When [sparse=True] combined with [unique=True] and [required=False]
    means that uniqueness won't be enforced for None values
    """

    # User editable fields
    username = db.StringField(required=True, unique=True, max_length=20, index=True)
    company_name = db.StringField(required=True, unique=True, max_length=25, index=True)
    email = db.EmailField(unique=True, required=False, sparse=True, max_length=80, index=True)
    password_hash = db.StringField(required=False, index=True)
    gold = db.IntField(default=0)
    meta = {"db_alias": "playerData", "collection": "users"}


    # OAUTH COMMENTED OUT
    # google_id = db.StringField(unique=True, required=False, sparse=True, index=True)

    def __repr__(self):
        """Define what is printed for the user object"""
        return f"Username: {self.username} id: {self.id}"

    def check_password(self, password):
        """Checks that the pw provided hashes to the stored pw hash value"""
        return check_password_hash(self.password_hash, password)