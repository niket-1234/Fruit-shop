print("WELCOME TO GARDEN GROVE BAZAAR")

print("\n")



import sys
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

def login(users):
    # Simulate user login
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check credentials (simulated for simplicity)
    return users.get(username) == password, username

def signup(users):
    # Simulate user signup
    username = input("Enter a new username: ")
    # Check if the username is already taken
    if username in users:
        print("Username already taken. Please choose another.")
        return False, ""
    else:
        password = input("Enter a password: ")
        users[username] = password
        save_users_to_file(users)
        print("Account created successfully!")
        return True, username

def save_users_to_file(users):
    with open("user_data.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

def load_users_from_file():
    try:
        with open("user_data.txt", "r") as file:
            users = {}
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
            return users
    except FileNotFoundError:
        return {}

class Fruit:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

def display_menu(fruits):
    print("Fruit Menu:")
    for i, fruit in enumerate(fruits, 1):
        print(f"{i}. {fruit.name} - ${fruit.price} | Stock: {fruit.stock}")

def add_to_cart(user, fruit, quantity):
    # Check if the selected fruit is in stock
    if quantity <= fruit.stock:
        user.cart.append((fruit, quantity))
        fruit.stock -= quantity
        print(f"{quantity} {fruit.name}(s) added to your cart.")
    else:
        print("Sorry, not enough stock available.")

def calculate_total(user):
    total = 0
    for fruit, quantity in user.cart:
        total += fruit.price * quantity
    return total

def main():
    # Load user database from file
    users = load_users_from_file()

    while True:
        print("CHOOSE AN OPTION TO..")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            success, username = login(users)
            if success:
                print(f"Welcome, {username}!","\nLET YOUR CRAVINGS COME TO AN END WITH OUR LARGE VARIETY OF FRUITS\n")
                user = User(username, users[username])
                break
            else:
                print("Login failed. Please try again or sign up.")
        elif choice == "2":
            success, username = signup(users)
            if success:
                print(f"Welcome, {username}!")
                user = User(username, users[username])
                
                
                break
        elif choice == "3":
            #print("Goodbye!")
            sys.exit("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

    # Simulated fruit data
    apple = Fruit("Apple", 2.5, 10)
    banana = Fruit("Banana", 1.5, 15)
    orange = Fruit("Orange", 3.0, 8)
    mango=Fruit("Mango",4.0,500)
    watermelon=Fruit("Watermelon",2.0,50)
    kiwi=Fruit("Kiwi",6.0,100)
    guava=Fruit("Guava",5.0,300)
    papaya=Fruit("Papaya",4.0,200)   
    grapes=Fruit("Grape",5.0,350)    
    cherry=Fruit("Cherry",1.0,250)
    
    fruits = [apple, banana, orange,mango, watermelon,kiwi,guava,papaya,grapes,cherry]

    while True:
        print("choose an option to")
        print("\n")
        print("1. Display Fruit Menu")
        print("2. Add to Cart")
        print("3. Display Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu(fruits)
        elif choice == "2":
            display_menu(fruits)
            fruit_choice = int(input("Enter the number of the fruit to add to cart: "))
            selected_fruit = fruits[fruit_choice - 1] if 1 <= fruit_choice <= len(fruits) else None
            if selected_fruit:
                quantity = int(input(f"Enter the quantity of {selected_fruit.name}: "))
                add_to_cart(user, selected_fruit, quantity)
        elif choice == "3":
            print("\nYour Cart:")
            for i, (fruit, quantity) in enumerate(user.cart, 1):
                print(f"{i}. {fruit.name} - Quantity: {quantity}")
        elif choice == "4":
            total = calculate_total(user)
            print("_____________________________________")
            print("INVOICE")
            print(f"\nYour total bill is: ${total}","\n\nThank You for your purchase","\n\nPLEASE DO VISIT US AGAIN")
            print("_____________________________________")
            break
        elif choice == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()