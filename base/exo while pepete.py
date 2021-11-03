
# x = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est-ce qui reste ?")
# while x != 'tu es lourd' :

#     if x == "repète" :
#         x = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est-ce qui reste ?")
#     elif x == "tu es lourd" :
#         print("Ok j'arrête")
#     else :
#         x = input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste ?")
# ======================================
# ======================================
# x = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est-ce qui reste ?")
# while True :

#     if x == "repète" :
#         x = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est-ce qui reste ?")
#     elif x == "tu es lourd" :
#         break
#     else :
#         x = input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste ?")
# ======================================
# ======================================

# def isfloat(n) :
#     try :
#         float(n)
#         return True
#     except ValueError :
#         print('That was no valid number.  Try again')
#         return False

# q = True
# while q :
#     x = input('Enter number x : ')
#     y = input('Enter number y : ')

#     if isfloat(x) and isfloat(y) :
#         print(float(x)+float(y))
#     else : 
#         print("Error: You have to enter digits")
    
#     q = input("Would you like to leave? yes / no : ")

#     if q == "yes" :
#         q = False

# ======================================
# ======================================

leave = True
cart = []

while leave :
    
    print("Menu : \n")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. Display what's in your cart")
    print("4. Empty your cart")
    print("5. Leave")
    
    choice = input("Choose an option please : \n")
    
    match choice :
        case '1':
            cart.append(input("What would you like to add to your cart? : \n"))
            print("Item added !\n")
        case '2':
            cart.remove(input("Which item would you like to remove? : \n"))
            print("Item removed !\n")
        case '3':
            print("This is what is currently in cart : \n")
            print(cart)
            print("\n")
        case '4':
            cart.clear()
            print("Your cart have been emptied ! \n")
        case '5':
            leave = False
        case _:
            print("ERROR: Please select a correct option.\n")
