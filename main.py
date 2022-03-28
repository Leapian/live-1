'''
Below is a task todo app. This app has the responsibilities:
    1) Fetch a list of tasks from an API (Will be provided)
    2) Create TodoTasks based on the data returned from the server and insert into a list
    3) Based on the user input there are a couple of operations that need to happen -> Fill the methods. 
    (Feel free to add any other methods, variables that you deem are needed for the completion of this exercise)
    
Useful Information:
    1) The datetimes are provided in miliseconds from the server
    2) The id is provided from the server for each task

The tasks should be displayed in the format below:
[ ] Task description / Due 12th Jan 2021 - For todo tasks
[x] Task description / Due 12th Jan 2021 - For done tasks
[o] Task description / Due 12th Jan 2021 - For overdue tasks

There is a bonus task:
    - Results should be displayed ascending / descending based on a flag that the user can change and stays that way until the user changes it again
'''


class Task:
    def __init__(self, id, taskDescription, dueDate, isComplete):
        self.id = id
        self.taskDescription = taskDescription
        self.dueDate = dueDate 
        self.isComplete = isComplete

    def setCompleted(self, isCompleted):
        self.isComplete = isCompleted
    
    def diplayTaskData(self):
        isCompleteIndicator = ""
        if(self.isComplete):
            isCompleteIndicator = "x"

        dueDateString = str(self.dueDate)
        print(self.id + " - [" + isCompleteIndicator +  "] " + self.taskDescription + " / Due " + dueDateString + "\n")
    
class TasksModel:
    def __init__(self):
        self.tasks = []
    
    def addTask(self, task):
        self.tasks.append(task)
    
    def displayAllTasks(self):
        for task in self.tasks:
            task.diplayTaskData()
    
    def diplayCompleteTasks(self):
        pass
    
    def diplayIncompleteTasks(self):
        pass
    
    def setTaskCompleteStatus(self, id, isCompleted):
        pass

def fetchTasksFromServer(apiEndpoint, taskModel):
    # Fetch the data from the server
    # Parse the data to json
    # For each json item -> convert to a Task object
    # Insert in the TasksModel each Task object
    pass

def main():
    userInput = ""
    apiEndpoint = "https://9cae-81-107-44-137.ngrok.io/tasks"
    taskModel = TasksModel()
    # @TODO fetch tasks using
    fetchTasksFromServer(apiEndpoint, taskModel)
    print("Tasks loaded from server. Here are all your tasks:")
    taskModel.displayAllTasks()
    while(userInput != "q"):
        print("Press 0 to display all tasks")
        print("Press 1 to display Complete tasks")
        print("Press 2 to display Incomplete tasks")
        print("Press a to add a task")
        print("Press e to mark a task as completed or not")
        print("Press q to exit")
        userInput = input('Please enter a command: ')
        if(userInput == "0"):
            pass
        elif(userInput == "1"):
            pass
        elif(userInput == "2"):
            pass
        elif(userInput == "a"):
            pass
        elif(userInput == "e"):
            pass
        elif(userInput == "q"):
            print("Goodbye")
            break;
        else:
            print("Command not recognized! Try again...")
        

if __name__ == "__main__":
    main()
