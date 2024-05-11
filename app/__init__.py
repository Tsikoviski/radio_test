from flask_login import LoginManager, UserMixin

login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    # Load user from your database or other storage
    return User(user_id)
