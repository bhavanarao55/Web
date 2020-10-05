from FlaskWebProject2.DAO.GetUsers import getUsers
from FlaskWebProject2.ViewModels.Users import Users
from FlaskWebProject2.Models.User import User

class UsersMB:
    """description of class"""
    def getUsersModel(self):
        users = Users()
        result = getUsers()
        for row in result:
            users.add_user(User(row['user_id'],row['user_name']))
        return users