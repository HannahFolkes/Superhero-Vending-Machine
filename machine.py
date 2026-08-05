#Main Menu Options 
import string

print("Welcome to the Morden Day Superhero Vending Machine!\nIn this program, you have a chance to buy your own Marvel superhero plushie, DC superhero plushie, or create your own superhero plushie!")
print()
print("Main Menu:\n" 
"1. Buy Marvel Merchandise\n" 
"2. Buy DC Merchandise\n" 
"3. Create your own superhero plushie\n" 
"4. Exit")
menu_option = input("Please select an option from the main menu (1-4): ")
print()

# SUPHERO ARRAYS
marvel_superheroes = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Spider-Man"]
dc_superheroes = ["Superman", "Batman", "Wonder Woman", "The Flash", "Aquaman", "Green Lantern"]

#MAIN MENU WHILELOOP
while (menu_option != "4"):
    if menu_option == "1": #MARVEL MERCHANDISE COLLECTION
        print("Congratulations! You have chosen to buy a plushie from the Marvel Merchandise Collection!")
        print("Please select a Marvel superhero plushie from the following options:\n 1. Iron Man\n 2. Captain America\n 3. Thor\n 4. Hulk\n 5. Black Widow\n 6. Spider-Man") 
        marvel_plushie = marvel_superheroes[int(input("Enter your choice (1-6): ")) - 1]
        print("Now dispensing your Marvel superhero plushie...")
        print()
        print("You have selected option " + marvel_plushie + " from the Marvel Merchandise Collection.")
        #PLAYING ANOTHER ROUND OPTION
        return_option = input("Would you like to return to the main menu or exit the program? Type 'yes' to return to the main menu or 'no' to exit: ")
        return_option = return_option.lower()
        break; 
    elif menu_option == "2": #DC MERCHANDISE COLLECTION
         print("Congratulations! You have selected to buy a plushie from the DC Merchandise Collection!")
         print("Please select a DC superhero plushie from the following options:\n 1. Superman\n 2. Batman\n 3. Wonder Woman\n 4. The Flash\n 5. Aquaman\n 6. Green Lantern")
         dc_plushie = dc_superheroes[int(input("Enter your choice (1-6): ")) - 1]
         print("Now dispensing your DC superhero plushie...")
         print()
         print("You have selected option " + dc_plushie + " from the DC Merchandise Collection.")
        #PLAYING ANOTHER ROUND OPTION
         return_option = input("Would you like to return to the main menu or exit the program? Type 'yes' to return to the main menu or 'no' to exit: ")
         return_option = return_option.lower()
         break;  
    elif menu_option == "3":#CREATE YOUR OWN SUPERHERO PLUSHIE
        print("You have chosen to create your own superhero plushie!")
        myPlushie_name = input("Please enter the name of your superhero plushie: ") #PERSONAL PLUSHIE NAME 
        myPlushie_gender = input("Please enter the gender of your superhero plushie (type 'Male', or 'Female'): ")#PERSONAL PLUSHIE GENDER
        myPlushie_power = input("Please enter the elemental superpower of your superhero plushie (type 'Fire', 'Water', 'Earth', or 'Air'): ")#PERSONAL PLUSHIE COLOR
        print("Now dispensing your custom superhero plushie...")
        print()
        print("You have created a custom superhero plushie with the following attributes:\nName: " + myPlushie_name +" \nGender: " + myPlushie_gender + "\nElemental Superpower: " + myPlushie_power + "\nEnjoy your new superhero plushie!")
        #PLAYING ANOTHER ROUND OPTION
        return_option = input("Would you like to return to the main menu or exit the program? Type 'yes' to return to the main menu or 'no' to exit: ")
        return_option = return_option.lower()
        break;              
    elif menu_option == "4":#EXITING THE PROGRAM
     print("GAME OVER!")
     print("Thanks for playing the Morden Day Superhero Vending Machines! We hope you enjoyed your experience and look forward to seeing you again soon!")
else: #ERROR CASE CHECKER 
    print("Invalid input. Please select a valid option from the main menu (1-4).")