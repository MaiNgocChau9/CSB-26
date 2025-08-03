class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

class Admin(User):
    def reset_password(self, new_password):
        self.__password = new_password

user = User("john_doe", "securepassword123")
admin = Admin("admin_user", "adminpassword")
admin.reset_password("newadminpassword")
print(f"User: {user.username}, Password: {user._User__password}")
print(f"Admin: {admin.username}, Password: {admin._User__password}")