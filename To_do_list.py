tasks=[]
def showtasks():
    if not tasks:
        print("Tasks are Empty")
    else:
        print("My tasks are")
        for i,task in enumerate(tasks,start=1):
           print(f"{i}. {task}")
def addtasks():
    x=input("Enter the task:")
    tasks.append(x)
    print("Task added")
def removetasks():
    showtasks()
    try:
       y=int(input("Enter the task number to be removed:"))
       if 1<=y<=len(tasks):
           tasks.pop(y-1)
           print(f"The task number {y} has been deleted")
       else:
           print("Invalid task number")
    except ValueError:
        print("Invalid text!Only numbers can be added!!!!")
while True:
    try:
       print("Choose from the given options :")
       print("Add tasks")
       print("Show tasks")
       print("Delete tasks")
       print("Quit")
       Option=input("Enter the option:")
       if Option.lower() in ["add tasks","addtasks","add task","addtask"]:
            addtasks()
       elif Option.lower() in ["show tasks","showtasks","show task","showtask"]:
            showtasks()
       elif Option.lower() in ["delete tasks","deletetasks","delete task","deletetask"]:
            removetasks()
       elif Option.lower()=="quit":
            break
       else:
            # print("Invalid input!!Try again")
            raise Exception("Invalid input")
    except Exception as invalidinput:
       print("                                      Try again!             ")

        
