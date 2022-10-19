#Summative for Arrays
#Packing for a trip!
# List 1 - Who you are taking on the trip, their names
# Dict 1 - Items you are taking and how many of that
# Dict 2 - Transport and how much it will cost

#Importing delays. I love these because they make the thing come out nicer
import time

# The list for where you are going!
destinations = ["Las Vegas"]
# The list for who you are bringing on the trip, will be modifiable
people_on_trip = []

# The dict. for the items you are bringing and how many of each item
packed_items = {}

# The dict. for what types of transport you are using and each one of its cost
transport = {}


#------------------Functions defined here------------------------

# Function for adding a mode of transport and its cost
def add_transport():
    done = False
    while done == False:
        key = input("What are you using for transport? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
        elif key != "done":
            value = input("How much is it in $ ? > ") #I made sure you actually type an amount of money here!
            if value.isdigit():                
                print(f"Adding {key} which costs about {value}")
                transport[key] = value
                
            else:
                print("That's not a value of money.") #I add alot of these while loops for user mess-ups!

# The function for adding an item you are packing and how many/much of that item
def add_items():
    done = False
    while done == False:
        key = input("What do you want to add to your suitcase? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
        elif key != "done":
            value = input("How many of that/those do you want to bring? > ") # A number here too!
            if value.isdigit():
                
                print(f"Adding {value} {key}")
                packed_items[key] = value
                
            else:
                print("That's not an amount.")


# Here is the function for removing an item 
def remove_item():
    done = False 
    while done == False:
        print("Here are the items you've packed for your trip!")
        time.sleep(1)
        for items in packed_items:  #These for-loops display the information nicely         
            print(f"-{items}")
        time.sleep(2)
        key = input("What item do you want to remove? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
            
        elif key != "done":
            if key in packed_items:
                print("Erasing", key)
                del packed_items[key]
            else:
                print("Sorry, you don't have that!")

# The function for removing a mode of transport
def remove_transport():
    done = False
    while done == False:
        print("Here are the transports you are using on your trip!")
        time.sleep(1)
        for things in transport:           
            print(f"-{things}")
        time.sleep(2)
        key = input("What mode of transport do you want to remove? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
            
        elif key != "done":
            if key in transport:
                print("Erasing", key)
                del transport[key]
            else:
                print("Sorry, you don't have that!")
                
# Add people who are coming on your trip
def add_people():
    done = False
    while done == False:
    
        person_added = input("Who do you want to bring? Type 'done' to exit > ")
    
        if person_added != "done":
            print(f"Perfect! We are adding {person_added} to the list of people joining you on your trip!")
            people_on_trip.append(person_added)
            
        
        elif person_added == "done":
            done = True

# Function for removing people from list
def remove_people():
    done = False
    while done == False:
        print("Here are the people on your trip!")
        time.sleep(1)
        for people in people_on_trip:           
            print(f"-{people}")
        time.sleep(2)
        person_removed = input("Who do you want to remove? Type 'done' to exit > ")
        if person_removed == 'done':
            done = True
        elif person_removed != "done":
            if person_removed in people_on_trip:
                print(f"Poor, {person_removed}! Removing {person_removed}!")
                people_on_trip.remove(person_removed)
                
            else:
                print("They're not on your list!")
            
#Function for viewing everything in each Dict. or List
#I try to use the time.sleep to make it as nice to read out as possible for the user!
def view_everything():
    print("In your bag you have:")
    time.sleep(0.5)
    for (key,value) in packed_items.items():
        time.sleep(1)
        print(f"You have {value} {key}!")
    print("In total you have:")
    print(len(packed_items), "items!")
    
    
    time.sleep(3)
    print("For transport, you have:")
    for (key, value) in transport.items():
        print(f"You have {key} which costs about {value}!")
        time.sleep(1)
    print("In total you have:")
    print(len(packed_items), "modes of transport!")
    time.sleep(3)
    
    
    print("The people joining you on your trip are:")
    for people in people_on_trip:
        print(f"-{people}")
        time.sleep(1)
    print("In total you have:")
    print(len(people_on_trip), "people on your trip!")
    time.sleep(3)
    
    print("The destinations you are travelling to are:")
    for places in destinations:
        print(f"-{places}")
        time.sleep(1)
    print("In total you have:")
    print(len(destinations)), ("modes of transport")
    time.sleep(2)

#Function for adding a destination
def add_destination():
    done = False
    while done == False:
    
        destination_added = input("Where do you want to go? Type 'done' to exit > ")
    
        if destination_added != "done":
            print(f"Perfect! We are adding {destination_added} to where we are going on our trip!")
            destinations.append(destination_added)
            
        
        elif destination_added == "done":
            done = True
# Function for removing a destination
def remove_destination():
    done = False
    while done == False:
        destination_removed = input("What do you want to remove? type 'done' to exit >")
        
        if destination_removed == 'done':
            done = True
        elif destination_removed != 'done':
            if destination_removed in destinations:
                print(f"Removing {destination_removed}")
                destinations.remove(destination_removed)
                
            else:
                print("That's not on your list!")
            
    

#Main function where each choice can be chosen!
def main():
    print("You have a trip planned for:")
    for places in destinations:
        print(places)
    time.sleep(2)
    las_vegas_choice = input("""Do you want to remove Las Vegas? - You can add a different destination later
    1 - Keep it
    2 - Remove it

    """)
    stay = True
    while stay == True:
        if las_vegas_choice == "1":
            print("Okay, we will keep it for now!")
            stay = False
        elif las_vegas_choice == "2":
            print("Removing Las Vegas!")
            destinations.pop(0)
            stay = False
        else:
            print("Try again!")
        
    print("Let's prepare for the trip!")
    go = 1
    while go == 1:
        print("")
        print("What would you like to do?")
        choice = input("""

        1 - ADD A Mode of Transport
        
        2 - REMOVE A Mode of Transport
        
        3 - ADD Items To Bag
        
        4 - REMOVE Items From Bag
        
        5 - ADD People Who Are Coming On Trip
        
        6 - REMOVE People Who Are Coming On Trip
        
        7 - VIEW Everything on Each List
        
        8 - ADD a destination
        
        9 - REMOVE a destination
        
        10 - Quit
        
        
        """).lower()
        if choice == "1":
            add_transport()
        elif choice == "2":
            remove_transport()
        elif choice == "3":
            add_items()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            add_people()
        elif choice == "6":
            remove_people()
        elif choice == "7":
            view_everything()
        elif choice == "8":
            add_destination()
        elif choice == "9":
            remove_destination()
        elif choice == "10":
            go = 0
            print("Good Bye!")
        else:
            print("I don't understand. Try again.")        
        


#-------------------Main Code----------------------
main()