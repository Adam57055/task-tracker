#Stores the variable "tasks" as a list
tasks = []

#Conditionals

while True:
    #Asks user for input to select one of the options
    action = input("Add/Remove/View/Exit").lower()
    if action == "add":
        task = input("What task would you like to add? ")
        tasks.append(task)
        print(f"{task} has been successfully added!")
    elif action == "remove":
        task = input("What task would you like to remove? ")
        if task in tasks:
            tasks.remove(task)
            print(f"{task} has been successfully removed!")
        else:
            print("Task could not be found.")
    elif action == "view":
        if not tasks:
            print("No tasks found.")
        else:
            for t in tasks:
                print("•", t)
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Enter one of the following options.")