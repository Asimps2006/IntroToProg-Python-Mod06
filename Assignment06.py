# ---------------------------------------------------------------------------- #
# Title: Assignment06 - “To Do List – Part 2” Scripting Exercise
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# ASimpson,2.2.2020, Modified code to complete assignment 6
# created several functions in both the Processor or IO Class
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")  # Open the file Object here
        # Use a for loop to read data from the To Do List text file
        for line in file:
            task, priority = line.split(",")
            # Build Row dictionary here
            row = {"Task": task.strip(), "Priority": priority.strip()}
            # Append the dictionary row to the List
            list_of_rows.append(row)
        file.close()  # Close the file Object
        # Return the list of rows
        return list_of_rows, 'Success'

    @staticmethod
    def input_new_task_check_if_already_exists(task):
        """ Check to see if the task name already exists in the list

        :param task: (string) name of the task:
        :return: Boolean value T/F
        """
        task_exists = False  # Set the initial task exists flag to False here
        # Use a for loop to see if the New Task Name is already in the table
        for item in lstTable:
            # change the name of the task to all lower case and see if current item is in the list
            if task.lower() == item.get("Task").lower():
                task_exists = True  # If the 2 task names match then set this to True
        # If the task already exists in the list return True otherwise return false
        if task_exists is True:
            return True
        else:
            return False

    @staticmethod
    def add_data_to_list(task, priority):
        """ Add a task name and priority to the list

        :param task: (string) name of the task:
        :param priority: (string) Priority of Task:
        :return: 'success'
        """
        # Set access to Global Variables within this function here
        global dicRow, lstTable
        # Create the dictionary row object using the user input values and the next ID value
        dicRow = {"Task": task, "Priority": priority}
        # Append the dictionary row to the List Table
        lstTable.append(dicRow)
        return 'Success'

    @staticmethod
    def remove_data_from_list(task):
        """ Remove a task name and priority to the list

        :param task: (string) name of the task:
        :return: 'success'
        """
        # Set access to Global Variables within this function here
        global lstTable
        # Use this For loop to evaluate each task name
        for objRow in lstTable:
            # Compare the user given task name with the values in each dictionary
            if task.lower() in str(objRow.values()).lower():
                # Let the user know that the task name is valid and will be removed
                print("Removing this task from the list: " + task)
                # Remove the Task Name form the ToDoList
                lstTable.remove(objRow)
        return 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write the list of TO DO task to the text file

        :param file_name: (string) name of text file:
        :param list_of_rows: (List) list of rows:
        :return: (list) of dictionaries, 'success'
        """
        # Open a file and use a For Loop to write each table row or item to a text file
        File_Object_Write = open(file_name, "w")
        for item in lstTable:
            # write the name of the item and the value to the Home Inventory List text file
            File_Object_Write.write(str(item.get("Task")) + "," + str(item.get("Priority")) + "\n")
        # Close the text file object here
        File_Object_Write.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(optional_message="Add another task?(Y/N): "):
        """ Gets a yes or no choice from the user, pass in an optional message
        :param optional_message: Pass in a Yes/No Question message
        :return: string
        """
        # Use the Default Message or pass in an optional message, strip white spaces, and make lower case
        return str(input(optional_message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)  # Print optional messages here otherwise print ''
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Input a new task and priority, check to see if task name exists.  If true, try another task!

        :return: nothing
        """
        # Get the User input about the new task name
        str_task = input("What's the New Task Name?:  ")
        # Call this function to see if the task already exists in the list, if false, add new task
        if not Processor.input_new_task_check_if_already_exists(str_task):
            # Get the User input about the task priority
            str_priority = input("What's the priority of this task?: ")
            # Call this processing function to add the task and priority to the To Do list
            Processor.add_data_to_list(str_task, str_priority)
        else:
            # Let the user know that the given task name already exists using this print statement
            print("The given task name already exists. Please try again!!")
            print()  # Add a line for looks

    @staticmethod
    def input_task_to_remove():
        """ Input a task name to remove, check to see if exists.  If so, delete it from the list!

        :return: nothing
        """
        # Get the User input about the task name to remove
        str_task = input("What task do you want to remove?:  ")
        # Call this function to see if the task already exists in the list, if true, add remove the task
        if Processor.input_new_task_check_if_already_exists(str_task):
            # Remove the task name from the To Do List by using this processor function
            Processor.remove_data_from_list(str_task)
        else:
            # Let the user know that the given task name already exists using this print statement
            print("The given task does not exist.  Please try again!!")


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoList.txt.
# Use this Processor function to read a text file and return a table of data
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    print()  # Adding a line for looks
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        while True:  # Use a While loop to allow for continued data entry
            # Use this IO function to input a new task and priority
            IO.input_new_task_and_priority()
            # Evaluate the user choice and exit loop if "n" in response
            if "n" in IO.input_yes_no_choice():
                print()  # Add a line here for readability
                # Exit the loop and go to the Main Menu
                break

    elif strChoice == '2':  # Remove an existing Task
        while True:  # Use a While loop to allow for continued task name removal
            # Get the Task Name from the IO function below
            IO.input_task_to_remove()
            # Evaluate the user choice and exit loop if "n" in response
            if "n" in IO.input_yes_no_choice("Remove another task? (y/n) - "):  # Use the user choice IO function here
                print()  # Add a line here for readability
                # Exit the loop and go to the Main Menu
                break

    elif strChoice == '3':  # Save Data to File
        # Evaluate the user choice and exit loop if "y" in response
        if "y" in IO.input_yes_no_choice("Save this data to file? (y/n) - "):  # Use the user choice IO function here
            # If the user enters "y" get the filename and task list table and user the Processor function to write to
            # a text file
            Processor.write_data_to_file(strFileName, lstTable)
            strStatus = "Data Saved!!"  # Pass this message to the IO function below
            IO.input_press_to_continue(strStatus)
        else:
            # In this step we're passing in a message instead of a variable for this function
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        # Evaluate the user choice and exit loop if "y" in response, use the IO User input function
        if 'y' in IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  "):
            Processor.read_data_from_file(strFileName, lstTable)  # read file data
            strStatus = "Original Data has been restored from file"
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
