from time import sleep, strftime

name = "Rhett"
calendar = {

}
def welcome():
  print ("Welcome to your calendar, " + name + "!")
  sleep(1)
  print ("Today's date is: " + strftime("%A %B %d, %Y"))
  sleep(1)
  print ("The time is: " + strftime("%H:%M:%S"))
  print ("What would you like to do?")

def start_calendar():
  welcome()
  start = True
  while start == True:
      user_choice = input("Please choose: A to add; U to Update; V to View; D to Delete; X to Exit the calendar. ")
      user_choice = user_choice.upper()
      if user_choice == "V":
          if len(calendar.keys()) < 1:
              print("Your calendar is empty.")
          else:
              print(calendar)
      elif user_choice == "U":
          date = input("What date would you like to update? ")
          update = input("Enter the update: ")
          calendar[date] = update
          print("Your update was successful!")
          sleep(1)
          print(calendar)
      elif user_choice == "A":
          event = input("Enter event: ")
          date = input("Enter date (MM/DD/YYYY): ")
          if len(date) > 10 or int(date[-4:]) < int(strftime("%Y")):
              print("You have inputed an invalid date.")
              try_again = input("Would you like to try again? (yes/no) ")
              try_again = try_again.lower()
              if try_again == "yes":
                  continue
              else:
                  start = False
          else:
              calendar[date] = event
              print("The even was successfully added!")
              print(calendar)
      elif user_choice == "D":
          if len(calendar.keys()) < 1:
              print("Your calendar is already empty.")
          else:
              event = input("What even would you like to delete?")
              for date in calendar.keys():
                  if event == calendar[date]:
                      del calendar[date]
                      print("The even was successfully deleted!")
                      print(calendar)
                  else:
                      print("That was an invalid event.")
              continue
      elif user_choice == "X":
           start = False
      else:
           print("That was an invalid response.")
           start = False
           
start_calendar()