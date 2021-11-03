
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

def isfloat(n) :
    try :
        float(n)
        return True
    except ValueError :
        print('That was no valid number.  Try again')
        return False

q = True
while q :
    x = input('Enter number x : ')
    y = input('Enter number y : ')

    if isfloat(x) and isfloat(y) :
        print(float(x)+float(y))
    else : 
        print("Error: You have to enter digits")
    
    q = input("Would you like to leave? yes / no : ")

    if q == "yes" :
        q = False
    
