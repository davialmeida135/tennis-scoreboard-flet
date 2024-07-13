class User:
    def __init__(self, username=None,access_token=None,refresh_token=None, logged_user=None):
        if logged_user:
            self.username = logged_user["username"]
            self.access_token = logged_user["access_token"]
            self.refresh_token = logged_user["refresh_token"]
        else:
            self.username = username
            self.access_token = access_token
            self.refresh_token = refresh_token

        