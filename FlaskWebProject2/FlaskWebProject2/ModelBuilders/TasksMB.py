from FlaskWebProject2.DAO.GetTasks import getTasks
from FlaskWebProject2.ViewModels.Tasks import Tasks
from FlaskWebProject2.Models.Task import Task

class TasksMB(object):
    """description of class"""
    def getTasksModel(self,user_id):
        tasks = Tasks()
        result = getTasks(user_id)
        for row in result:
            tasks.add_task(Task(row['task_id'],row['user_id'],row['candidate_id'],row['name'],row['task'],row['details'],row['technology'],row['source'],row['link'],row['time'],row['notes']))
        return tasks