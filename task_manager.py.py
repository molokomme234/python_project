#This is a pythonn program for a small business
import datetime
import os
import fileinput

#Import necessary modules
#Create a menu with choices to select from and define each selection

def choices():
    print("You are logged in. Welcome to the program!")
    print("Please select one option from below")
    choice = input("r - register user\n a - add tasks\n va - view all task\n vm - view my tasks\n gr - Generate reports \n ds - Statistics\n e - Exit\n")
    if choice == "r" and userName == "admin":
        return register()
    elif choice == "a":
        return addTask()
    elif choice == "va":
        return viewAll_tasks()
    elif choice == "vm":
        return viewMy_tasks()
    elif choice == "gr":
        return generateReports()
    elif choice == "ds" and userName == "admin":
        return Statistics()
    else:
        return Exit()
     
 
#if user chooses "r", the admin gets to register a new user to the data base
def register():
    print("Register a new user")
    print("-------------------")
    name = str(input("Enter Username: "))
    #password = str(input("Enter Password: "))
    f = open('user.txt','r')
    for line in f:
        user = line.split(",")
    while name == user[0]:
        print("Username already in use, please enter a different Username")
        name = str(input("Enter a Username: "))
#write new registered user to the user text file
    if name != user[0]:
        password = str(input("Enter Password: "))
        f = open('user.txt','a')
        f.write("\n")
        f.write(name)
        f.write(",")
        f.write(password)
        f.write("\n")
        f.close()
        return "Registering user to data base" 

#If user choose "a" they add a task for an exixting user on the database
def addTask():
    count = 1
    print("Add a new task: ")
    print("----------------")
    name = input("Enter Username assigned to the task: ").lower()
    f = open('user.txt','r')
    info = [i.split(",")[0] for i in f.readlines() if len(i) > 3]
    
    #Getting the user to assign the task to the user in the data base an setting due dates
    if name in info:
        taskTitle = input("Enter title for the task: ")
        taskDescription = input("Enter task description: ")
        taskDueDate = input("Enter due date for the task: (yyy-mm-dd)")
        taskSignOnDate = datetime.datetime.now()
        print(taskSignOnDate.strftime('%Y-%m-%d'))
        taskCompleted = False
        if taskCompleted == False:
            taskCompleted = "No"
        else:
            taskCompleted = "Yes"
            
        taskFile = open('tasks.txt','a+')
        tasks = ("\nUser assigned to task: " + str(count) + "\n " + name + "\nTask Title: " +"\n" + taskTitle + "\n" + "Task Description:\n"+ taskDescription + "\n" + "Task Due Date:\n" + str(taskDueDate) + "\n" + "Date Signed:\n" + str(taskSignOnDate) + "\n" + "Task Completed:\n" + taskCompleted + "\n")
        taskFile.write(tasks)
        return "Writing to file"
    count += 1
    
    
    if name not in info:
         return "Username entered is not on data base"

#If user chooses "va",they view all tasks in the database
def viewAll_tasks():
    print("Here is a list of all the tasks in the database: ")
    print("--------------------------------------------------")
    print("Username" +5*"" + "Title" + 15*"" + "Description" +50*"" + "Due Date" + 50*"" + "Assigned Date" + 5*"" + "Completed")
    taskList = open('tasks.txt','r')
    tasks = taskList.read()
    tasks = tasks.split()
    print(tasks[0] + (12-len(tasks[0]))*" "+
          tasks[1] + (20-len(tasks[1]))*" "+
          tasks[2] + (61-len(tasks[2]))*" "+
          tasks[3] + (13-len(tasks[1]))*" "+
          tasks[4] + (18-len(tasks[1]))*" "+
          tasks[5])

def generateReports():
    file = open('task_overview.txt','w')
    file2 = open('user_overview.txt','w')

    print(userOverview())
    print(taskOverview())
    print(count_char())
    print(complete_task())
    print(percentage())


def edit_task():
    class ExistException(Exception):  # Custom exception used later
        pass
    choice = ""  # used later
    tf = open("tasks.txt","r")  # Open task file for reading first
    data = tf.readlines()
    edit_line = data
    #print(f"EDIT TASK {task_number}:\n")

    # Split the selected task (edit_line) into separate fields:
    task_num = data[0]
    task_user = data[1]  # Stores username
    task_title = data[3]  # Stores title
    task_desc = data[5]  # Stores description
    task_so = data[9]  # Stores sign on date
    task_dd = data[7]  # Stores due date
    task_complete = data[11]  # Stores completion indicator

   # Print out task detail:
    print(f"Task number: {task_num}")
    print(f"Description:    {task_desc}")
    print(f"Assigned to:    {task_user}")
    print(f"Signed on:     {task_so}")
    print(f"Due Date:       {task_dd}")
    print(f"Completed?:     {task_complete}")
    #print("")


    # Check if already done, print accordingly and return to previous menu:
    if task_complete == 'Yes':
        print("\nThis task is already completed, and cannot be edited.\n")
        view_mine()

    # Give user different options to edit task:
    edit_option = input(f"Type 'DONE' to mark task {task_num} as completed.\n"
    "Type 'USER' to assign the task to someone else.\n"
    "Type 'DATE' to change the due date.\n"
    "Type any other key to go back to the main menu:\n-->").lower()

    # User selected to mark as completed:
    if edit_option == "done":
        task_complete = "Yes"  # change variable
        with open('tasks.txt','w') as f:
            # Go through file line by line and rewrite the data:
            for i, line in enumerate(data):
                # If relevant line (selected task) replace necessary field:
                if i == edit_line:
                    f.writelines(line.replace(line.strip().split(", ")[11], "Yes"))
                # For other lines, just replace with same data again
                else:
                    f.writelines(line)
            tf.close()
            # Print updated task:
            print(f"Task {task_num} marked as completed:\n")
            print(f"Task {task_num}: {task_title}")
            print(f"Description:    {task_desc}")
            print(f"Assigned to:    {task_user}")
            print(f"Signed on:     {task_so}")
            print(f"Due Date:       {task_dd}")
            print(f"Completed?:     {task_complete}")
            print(" ")

            option = input("Type '-1' to go back to the Main Menu, "
                    "or any other key to exit.\n--> ").lower()
            if option == '-1':
                    return(choices())
            #else:
                #print("Goodbye")
                #exit(1)
                # If username does NOT exist, throw error and ask user to go to registration, OR
                # try enter username again:
            else:  
                print("This user does not exist. Press 'r' to register them, or enter a"
                    " different username:")
                print (f"Available users: {users}")
                choice = input("\n-->").lower()  # store username and go back to start if loop
                if choice == 'r':            #... unless they chose, "R" the go to Registration
                    reg_user()
                else:
                    raise ExistException
            #except ExistException:
                #pass

    # User selected to change due date:
    elif edit_option == 'date':
        new_due_date = date_val()  # Calls function to enter & validate date, & returns variable
        with open("tasks.txt",'w') as f:
            # Go through file line by line and rewrite the data:
            for i, line in enumerate(data):
                # If relevant line (selected task) replace necessary field:
                if i == edit_line:
                    f.writelines(line.replace(line.strip().split(", ")[7], new_due_date))
                # For other lines, just replace with same data again
                else:
                    f.writelines(line)
        tf.close()
        print(f"Due Date \'{task_dd}\' changed to '{new_due_date}'.")
        option = input("Type '-1' to go back to the Main Menu, "
        "or any other key to exit.\n--> ").lower()
        if option == '-1':
            print(choices())
        else:
            print("Goodbye")
            exit()
    
#print("") 



def taskOverview():
    file = open('task_overview.txt','w')
    dueDate = datetime.datetime.today()
    data = open('tasks.txt','r')

    for line in data:
        if not line.startswith('Due Date'):continue
        field,value = line.split(":")
        if field == "Due Date":
            if datetime.datetime.strptime(value.strip(),'%Y-%m-%d') < today:
                print("This task is overdue")
                file.write("This task is overdue:" + dueDate)


def complete_task():
    data = open('tasks.txt','r')
    file = open('task_overview.txt','a')

    count = 0
    data = data.readlines()
    task = data[0]
    if task == "Yes":
     count += 1
    file.write("The number of completed tasks is:" + str(count))
    print("The number of completed tasks is : {count}")

    if task == "No":
       count += 1
    file.write("The number of incomplete tasks is:" + str(count))
    print("The number of incomplete tasks is: {count}")

    
    
                

def count_char():
    with open('tasks.txt') as file:
        text = file.read()
        count = 0
    for character in text.lower():
     if character == "no":
        count += 1
        perc = 100 * count / len(text)
        return perc
        f = open('user_overview.txt','a')
        f.write("\nThe percentage of incomplete tasks is: " + perc)
        f.close()


def percentage():
    with open('tasks.txt') as file:
        text = file.read()
        count = 0
    for character in text.lower():
     if character == "yes":
        count += 1
        perc = 100 * count / len(text)
        return perc
        f = open('user_overview.txt','a')
        f.write("\nThe percentage of complete tasks is: " + perc)
        f.close()    

def registered_tasks():
    tasks = open('tasks.txt','r')
    count = 0
    items = tasks.readlines()
    for items in tasks:
        count +=1
        print(count)
        file = open('user_overview.txt','a')
        file.write("\nThe total number of tasks is:" + str(count) + "\n")
        print("The total number of tasks is : {count}")

def Usertasks():
    count = 0
    user = open('user.txt','r')
    name = user.readlines()
    
    tasks = open('tasks.txt','r')
    items = tasks.readlines()
    if name == items[2]:
        count +=1
        print(count)
        f = open('user_overview.txt','w')
        f.write("\nThe number of tasks assigned to you is" + str(count))
        print("The number of tasks assigned to you is: {count}")

def userOverview():
    numUsers = open('user.txt','r')
    count = 0
    for line in numUsers:
        count +=1
        print(count)
        file = open('user_overview.txt','w')
        file.write("The total number of users registered is:" + str(count) + "\n")

        return (registered_tasks())
        return (Usertasks())
        
    
#If user chooses "vm" they view all tasks assigned to them
def viewMy_tasks():
    print("Here are the tasks assigned to your Username: ")
    print("----------------------------------------------")
    count = 0
    name = open('user.txt','r')
    user = name.read()
    tasks = open('tasks.txt','r')
    userTask = tasks.readlines()
    if user == userTask[0]:
       print(str(count+1)+ (8-len(str(count+1)))*" "+
        taskItems[0] + (12-len(taskItems[0]))*" "+
        taskItems[1] + (20-len(taskItems[1]))*" "+
        taskItems[2] + (61-len(taskItems[2]))*" "+
        taskItems[3] + (13-len(taskItems[1]))*" "+
        taskItems[4] + (18-len(taskItems[1]))*" "+
        taskItems[5]) 
    count += 1

    print(edit_task())
    
    if count == 0:
        print("There are no tasks assigned to your username")
        print(choices())


#If admin chooses "s" they view all statistics in the database
def Statistics():
    print("Statistics")
    print("----------")
    f = open('user.txt','r')
    user = f.read()
    file = open('tasks.txt','r')
    tasks = file.readlines()
    userCount = 0
    tasksCount = 0
    for task in tasks:
        tasksCount +=1
    for users in user:
        userCount +=1
        print("The total number of tasks listed is :" + str(tasksCount)+ " tasks")
        print("The total number of users registered is :" + str(userCount)+ " users.")
        
    with open('task_overview.txt','w')as file:
     file.write("The total number of tasks listed is :" + str(tasksCount)+ " tasks")
        
def Exit():
    print("Goodbye")
    exit()

    
#Logging in and getting the program to start     
users = {}
with open('user.txt','rt')as username:
    for line in username:
        username,password = line.split(",")
        users[username.strip()] = password.strip()

userName = input("Enter your username:\n")
if username not in users:
    print("Username incorrect")
    userName = input("Enter correct username: \n")

if userName in users:
    print("Username correct")

    with open('user.txt','rt') as password:
        for line in password:
            username,password = line.split(",")
            users[password.strip()]= username.strip()
            
passWord = input("Enter your password: \n")
if passWord not in users:
    print("Incorrect password")
    passWord = input("Enter correct password: \n")

if passWord in users:
    print("Correct password")

print(choices())                    



    





                 
    
                     
