'''
File Name: hw5_starter.py
Started By: Emily Alfs-Votipka
Completed By: Elijah James
Section: CIS115 - 
Description: Homework 5 project
'''


def price_check(price):
    """This function takes a price and returns a float"""
    try:
        price = float(price)
        return price
    except ValueError:
        print("Please enter a valid price")
        return False


def checkout(cart, inventory):
    """This function checks out and finishes the order"""
    total = 0
    receipt = ""
    for item in cart:
        receipt += str(cart[item]['quantity']) + " " + item + " " + str(cart[item]['price']) + " " +     str(cart[item]['quantity'] * cart[item]['price']) + "\n" 
        total += cart[item]['quantity'] * cart[item]['price']
    total = print("Your subtotal is : $" + str(total) + "\n" "Your actual total for today is: $  = %.2f" % total)
    receipt += "Thank you for deciding to shop with us today!" 
    return receipt

    
def show_qty(inventory):
    """This function prints the inventory
    """
    print("Here is the current inventory:")
    for item in inventory:
        print(item, inventory[item]['quantity'])


def show_prices(inventory):
    """
    This function prints the inventory
    """
    print("These are the current prices:")
    for item in inventory:
        print(item, inventory[item]['price'])

      
def show_cart(cart): 
    """This function shows the items in your cart"""
    print("Here is your cart:") 
    for item in cart: 
        print("\t", item, "x", cart[item]['quantity'])


def add_to_cart(item,cart,inventory):
    """
    This function adds an item to the cart
    """
    if item in inventory:
        if inventory[item]['quantity'] > 0:
            if item in cart:
                cart[item]['quantity'] += 1
            else:
                cart[item] = {'quantity': 1, 'price': inventory[item]['price']}
            inventory[item]['quantity'] -= 1
            return True
        else:
            print("Sorry, we don't have that many")
            return False
    else:
        print("Sorry, we don't have that item")
        return False


def remove_from_cart(item, cart, inventory):
    """
    This function removes an item from the cart
    """
    
    if item in cart:
        if cart[item]['quantity'] > 1:
            cart[item]['quantity'] -= 1
            inventory[item]['quantity'] += 1
            return True
        else:
            del cart[item]
            inventory[item]['quantity'] += 1
            return True
    else:
        print("Sorry, we don't have that item")
        return False
   

def main():
    """Main source code"""
    inventory = {
        'Eggs': {'quantity': 7, 'price': 2.07},
        'Milk': {'quantity': 5, 'price': 3.42},
        'Cheese': {'quantity': 4, 'price': 4.98},
        'Bread': {'quantity': 7, 'price': 2.72},
        'Ketchup': {'quantity': 5, 'price': 3.98},
        'Mustard': {'quantity': 2, 'price': 2.72},
        'Turkey': {'quantity': 3, 'price': 34.58},
        'Chicken': {'quantity': 4, 'price': 14.92}
    }
    cart = {}
    print("Welcome to our store!")
    shopping = True
    while shopping:
        print("What would you like to do?")
        print("Check (P)rice")
        print("(V)iew Inventory")
        print("(S)how cart")
        print("(G)et Item")
        print("(R)eturn an item from your cart or")
        print("(C)heckout")
        choice = input("Enter your choice: ")
        if choice == "P" or choice == "p":
            show_prices(inventory)
        elif choice == "V" or choice == "v":
            show_qty(inventory)
        elif choice == "S" or choice == "s":
            show_cart(cart)
        elif choice == "G" or choice == "g":
            item = input("What would you like to add? : ")
            add_to_cart(item,cart,inventory)
        elif choice == "R" or choice == "r":
            item = input("What would you like to remove? :")
            remove_from_cart(item,cart,inventory,)
        elif choice == "C" or choice == "c":
          print("Your order is :" , checkout(cart,inventory,))
          checkout(cart,inventory)
          shopping = False
         
        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()
    print("Goodbye! Have a good day!")
    quit()
    main()




