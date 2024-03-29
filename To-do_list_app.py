'''
User Interface (UI):
Create a command-line interface (CLI) for the To-Do List Application.
Display a welcoming message and a menu with the following options:
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
To-Do List Features:
Implement the following features for the To-Do List:
Adding a task with a title (by default “Incomplete”).
Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
Marking a task as complete.
Deleting a task.
Quitting the application.

User Interaction:
Allow users to interact with the application by selecting menu options using input().
Implement input validation to handle unexpected user input gracefully.

Error Handling:
Implement error handling using try, except, else, and finally blocks to handle potential issues.

Code Organization:
Organize your code into functions to promote modularity and readability.
Use meaningful function names with appropriate comments and docstrings for clarity.

Testing and Debugging:
Thoroughly test your application to identify and fix any bugs.
Consider edge cases, such as empty task lists or incorrect user input.
'''

# def 4 functions 
# use a dic to be able to get keys and make them complete and not complete.
# allow the user to add a key and its value to it.


def add_task(to_do_list):
  predefined_commands = {"add": "Has been added to the list.\n"}

  while True:
    print("Add Menu:\n1. Add to list.\n2. Main Menu\n3. More to come...")
    user_input = input("Please select one of our menu options: ").lower()
    if user_input == "main menu":
      break
    for key, value in predefined_commands.items():
      result = user_input.find(key)
      if result == -1:
        pass
      elif key == "add":
        try:
          amount_to_add = int(input("How many tasks would you like to add: "))
          for i in range(amount_to_add):
            list_adding = input(f"What would you like to add to your To-do list?\n{i+1}. ")
            time_start = input("What is the time do you want to set this task to start:  ")
            while True:
              morning_afternoon1 = input("AM or PM: ").upper()
              if morning_afternoon1 == "AM":
                update = "AM"
                break
              elif morning_afternoon1 == "PM":
                update = "PM"
                break
              else:
                print("Wrong Input")
            time_end = input("What is the time do you want to set this task to end: ")
            while True:
              morning_afternoon2 = input("AM or PM: ").upper()
              if morning_afternoon2 == "AM":
                update2 = "AM"
                break
              elif morning_afternoon2 == "PM":
                update2 = "PM"
                break
              else:
                print("Wrong Input")
            while True:
              priority = input("What is the priority of this task [HIGH/LOW/NONE]: ").upper()
              if priority == "HIGH":
                update3 = "HIGH"
                break
              elif priority == "LOW":
                update3 = "LOW"
                break
              elif priority == "NONE":
                update3 = "NONE"
                break
              else:
                print("Wrong Input")
            adding_to = to_do_list.update({str.capitalize(list_adding):(time_start,update,"-",time_end,update2,"  Priority: ",update3,"  Task is: ","Incomplete")})
            print(f"{value}")  
        except ArithmeticError as a:
          print(f" Error: {a} in adding task")
        except Exception:
          print("I don't recognize that input try again please!")
      else:
        print("I don't recognize that input try again please!")

     
def view_task(to_do_list):
  predefined_commands = {"main": "Returning to Main Menu"}
  while True:
      for count, (key,value) in enumerate(to_do_list.items()):
        print(f"{count +1}. {key}: {"".join(value)}")
        
      print("View Menu:\n1. Main Menu\n2. More to come...")
      user_input = input("Please select one of our menu options: ").lower()
      for key, value in predefined_commands.items():
        result = user_input.find(key)
        if key == "main":
          print(f"{value}")
          break
        elif result == -1:
          pass
        else:
          print("I don't recognize that input try again please!")
      break

      
def mark_task(to_do_list):
    #predefined_commands = {"main":"Returning to Main Menu","list": "Lets start making tasks": "whole": "Choose a day to to mark"}
    while True:
      #print("Mark Menu:\n1. Mark a task\n2. Mark a whole day\n3. Main Menu\n4. More to come...")
      for count, (key,value) in enumerate(to_do_list.items()):
        print(f"{count +1}. {key}: {"".join(value)}")

      users_choice = str.capitalize(input("Which task would you like to mark as Complete? "))
      for item, completion in to_do_list.items():
        result = users_choice.find(item)
        if result ==-1 :
          pass
        elif users_choice == item:
          updated_to_do_list = to_do_list[item] = "Complete"

      user_input = input("Do you want to continue marking tasks [YES/NO]: ").upper()
      if user_input != "YES":
        break
      elif user_input == "YES":
        pass
      else:
        print("I don't recognize that input try again please!")
            

def delete_task(to_do_list):
  predefined_commands = {"main": "Returning to Main Menu","task":"Let's see what we can get rid of today"}
  
  while True:
    print("Delete Menu:\n1. Delete Task\n2. Main Menu\n3. More to come...")
    user_input = input("Please select one of our menu options: ").lower()
    if user_input == "main menu":
        break
    elif user_input == "delete task":
        try:
          for count, (key,value) in enumerate(to_do_list.items()):
              print(f"{count +1}. {key}: {"".join(value)}")
          removing_items = input("Which task do you want to Delete? ")
          updated_to_do_list = to_do_list.pop(str.capitalize(removing_items))
          user_input2 = input("Do you want to continue Deleting tasks: [YES/NO] ").upper()
          if user_input2 == "NO":
            break
          elif user_input2 == "YES":
            pass
          else:
            print("I don't recognize that input try again please!")
        except Exception:
          print("I do not understand try again!")
    else:
      print("I don't recognize that input try again please!")
      

def to_do_list_main():
  to_do_list = {}
  predefined_commands = {"add":"\nLet's get started adding tasks!", "view":"\nRight away lets take a look at your To-do list!", "mark":"\nLet's mark what we have completed.", "delete":"\nLet's clean up some of our To-do list!", "quit":"\nShutting down Application"}
  print("Welcome to the To-Do List Application!")
  try:
    while True:
        print("Main Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n6. More to come...")
        user_task_choice = input("Please select one of our menu options: ").lower()
        if user_task_choice == "quit":
              break
        for key, value in predefined_commands.items():
            result = user_task_choice.find(key)
            if result == -1:
              pass
            elif key == "add":
              print(f"{value}")
              add_task(to_do_list)
            elif key == "view":
              print(f"{value}")
              view_task(to_do_list)
            elif key == "mark":
              print(f"{value}")
              mark_task(to_do_list)
            elif key == "delete":
              print(f"{value}")
              delete_task(to_do_list)
            else:
              print("I don't recognize that input try again please!")
  except Exception as e:
    print(f"Error: {e} Problem with response input.")
  else:
    pass
  finally:
    print("Thank you for using our Application today!")

 

to_do_list_main()
