# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = ""  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print (store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store_name != store.name
            return False
          
    return store

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print (store.name)
    store_picked = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
        if store_picked == "checkout":
            return "checkout"


        elif get_store(store_picked):
            return get_store(store_picked)
        else:
            print("Invalid store")
            picked_store()    
            

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.pick_products()

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
