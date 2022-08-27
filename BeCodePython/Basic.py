# #JOUR 01

# "1.1 Afficher les chaînes suivantes"
# print ("Coucou !")
# print ("L’étoile du Nord")
# print ("C’est “génial !!!”")
# print ("^0\/0^")
# print ("")

# "1.2 Déterminer le type des expressions suivantes"
# print (type(10 - 12))
# print (type(2 + 3.14))
# print (type("3"))
# print ("")

# "1.3 Evaluer chacune des expressions suivantes"
# print (37 - 5 - 2)
# print (37 / (5 * 2))
# print (37 / 5 / 2)
# print (37 % (5 % 2))
# print (37 % 5 % 2)
# print ("")

# print ("1.4 Evaluer chacune des expressions suivantes en supposant que m a pour valeur 24 et que n a pour valeur 7 :")
# m = 24
# n = 7
# print (m - n - 8)
# print (m % n)
# m = m + 1
# print (m)
# m += 1
# print (m)
# n -= 2
# print (n)
# m += n
# print (m)
# m = n = 3
# print (m , n)
# print ("")

# print ("1.5 Ecrire un programme qui demande vos noms et adresses")
# nombre = input ("Entrer votre Nom :")
# prenombre = input ("Entrer votre Prenom :")
# rue = input ("Rue :")
# nummero_batîment = ("Numero :")
# numero_boite = ("Boite :")
# postal_code = input ("Postal Code :")
# commune = input ("Commune :")
# print ("Bonjour " , nombre , " " , prenombre , ", " , "votre adresse est : " , rue ,
#        ", " , postal_code , ", " , commune , ", " , nummero_batîment , "/" , numero_boite)
# print ("")

# print ("1.6 Ecrire un programme qui affiche la lettre majuscule “P” dans grille 7x7:")
# p_a = "******"
# p_b = "*     *"
# p_c = "*"
# print (p_a + "\n" + p_b + "\n" + p_b + "\n" + p_a + "\n" + p_c + "\n" + p_c + "\n" + p_c)
# print ("")

# print ("1.7 Ecrire un programme qui affiche la somme, la différence, le produit, le quotient et le reste de deux entiers lus ou clavier. Testez avec les valeurs 60 et 7 !")
# x = 60
# y = 7
# print (x + y)
# print (x - y)
# print (x * y)
# print (x / y)
# print (x % y)

# semaine = ["Lundi","Mardi","Mercredi","Jeudi","vendredi","Samedi","Dimanche"]
# print (semaine)
# print (semaine[4])
# jour = semaine[0]
# semaine[0]=semaine[-1]
# semaine[-1]=jour
# print (semaine)
# print (semaine[-1]*12)

# for jour in semaine :
#     print (jour)

# personnage = ('Vladimir', 73, ['pêche', 'équitation'])
# nom, age, sport = personnage
# print(sport[0])

# datta = ("jose",[1,2,3,4,5],["Lundi","Mardi","Mercredi","Jeudi","vendredi","Samedi","Dimanche"])
# nom,nombre,jour=datta 
# print (datta)
# mois = ["jan","feb","mars"]
# jour = mois
# print (nom[0],nombre[3],jour[0])

# a = input("Ecrivez le nombre du personage :")
# b = input("Ecrivez l'age du personage :")
# c = input("Ecrivez une passion :")
# d = input("Ecrivez une passion :")

# personage = (a,b,[c,d])
# nom,age,passion=personage
# print (personage)
# print (passion[0])
# list(personage) #Y luego? como se saca la informacion de la lista para modificarla?, no se puede§§§§
# personage_dummy = personage[0]
# personage[0]=personage[-1]
# personage[-1]=personage_dummy
# print (personage)

#JOUR 02
# if 4 < 5 :
#     print ("4<5")
# if 5 > 6 :
#     print ("5>6")
# else : 
#     print ("5<6")

# if 4 != 4 :
#     print ('4!=4')
# elif 10 == 1 :
#     print ("10=1")
# else :
#     print ("Bonjour")

# x = int(input('Entrer une valeur pour x : '))
# y = int(input('Entrer une valeur pour y : '))

# if x == 5:
#     print('X contient l\'entier 5')

# if x > y:
#     print("x contient une valeur strictement supérieur à y")

# x = int(input('Entrer une valeur pour x : '))

# if x == 5:
#     print('X contient l\'entier 5')
# elif x == 6:
#     print('X contient l\'entier 6')
# elif x == 6:
#     print('X contient l\'entier 7')
# else:
#     print('x contient un autre entier' )

# print ("2.1 Ecrire un programme qui lit l’âge de l’utilisateur")
# age = int(input("T'as quelle age ? :"))
# if age < 18 :
#     print ("Junior")
# elif age >=18 and age <= 65 :
#     print ("Adulte")
# elif age >=65 :
#     print ("Senior")
# else :
#     print ("Error !")

# podemos gerenar una nueva variable e imprimir solamente esa variable

# print ("2.2 Ecrire un programme qui lit deux nombres entiers et qui affiche si l’un des nombres est multiple de l’autre.")
# a = float(input("Numero a : "))
# b = float(input("Numero b : "))

# if a < b :
#     a , b = b , a        
#     # hay que organizar la data antes de poder realizar la operacion

# if a % b == 0 :
#     print (str(a) + " est un multiple de :" + str(b))
# else :
#     print (str(a) + " Ce n'est pas un multiple de :" + str(b))
# print (str(a) + "/" + str(b) + "=" + str(a/b))

# print ("2.3 Ecrire un programme qui lit quatres nombres entiers puis affiche le plus petit et le plus grand de ces nombres.")
# a = float(input("Numero a :"))
# b = float(input("Numero b :"))
# c = float(input("Numero a :"))
# d = float(input("Numero b :"))

# print ("Le plus petite :" + str(min ([a,b,c,d])) + " , le plus grand :" + str(max ([a,b,c,d])))

# print("2.4 Ecrire un programme qui lit deux nombres et un caractère +,-,* ou /. Suivant le caractère, le programme affiche l’opération correspondante.")
# a = float(input("Numero a :"))
# b = float(input("Numero b :"))
# operator = input ("Ecrivez un operator + - * / :")

# if operator == "+" :
#     print (float(a + b))
# elif operator == "-" :
#     print (float(a - b))
# elif operator == "*" :
#     print (float(a * b))
# elif operator == "/" :
#     print (float(a / b))
# else :
#     print ("Error !")
  
# print ("2.5 Ecrire un programme qui vérifie si une année est bissextile. Ce sont les années divisibles par 4 mais pas par 100 ou les années divisible par 400.")  

# an = int(input("Ecrivez l'année : ")) 

# if (an%4 == 0 and an%100 != 0) or (an%400 == 0) : 
#     print(an, " c'est un année bissextile.") 
# else : print(an, " ce n'est pas un année bissextile.")

# list = range (2000,2050,1)
# bissextile = []
# # para generar una lista nueva de anos bisientos, primero hacemos una lista bacia para recibir la informacion
# for an in list : 
#     if (an%4 == 0 and an%100 != 0) or (an%400 == 0) : 
#         print(an, " c'est un année bissextile.")
#         bissextile.append(an)
#         # mandamos la informacion que cumple con la condicion a la lista creada
#     else : print(an, " ce n'est pas un année bissextile.")
# print (bissextile)
    
# print ("2.6 Ecrire un programme qui lit une côte sur 10, et qui affiche :")
# côte = float(input("Côte :"))
# if côte >= 9 :
#     print ("Exellente")
# elif côte >= 8 :
#     print ("Très bien")
# elif côte >= 6 :
#     print ("Bien")
# elif côte >= 5 :
#     print ("Faible")
# elif côte >= 3 :
#     print ("Médiocre")
# elif côte < 3 :
#     print ("Mauvais")
# else :
#     print ("Error")


# x = 1
# while x < 10 :
#     print (x)
#     x += 1
# Ctrl x para cerrar el boucle !!!!

# for n in range(10):
#     print(n)

# for n in range(10, 15, 2):
#     print(n)

# semaine = ["lundi", "Mardi", "Mercredi",
#             "Jeudi", "Vendredi", "Samedi", "Dimanche"
#             ]

# for id, Jour in enumerate(semaine):
#     if Jour == "Vendredi" :
#         break
#     print(id + 1,Jour)

# for val in "string":
#     if val == "i":
#         break
#     print(val)

# print("The end")

# for i in range(9):
#     if i % 2 == 0:
#         print ("")
#     else:
#         print(i)



# print("3.1 Pour afficher un carractère du code ASCII, il suffit d’utiliser la fonction chr(i), où i représente le numéro de caractère. Ecrire un programme qui affiche les 128 premiers caractères, précédés de leur numéro.")
# list = range (1,129)
# for id,carracterre in enumerate(list) :
#     print (id + 1,chr(carracterre))
    
# print ("3.2 Ecrire un programme qui lit le nombre de ligne d’étoiles, et qui affiche un triangle rectangle en accroissant de un le nombre d’étoiles par ligne.")

# x = input("Ecrivez nombre de lignes d’étoiles : ")
# numero = range (1,int(x))
# for id,etoile in enumerate(numero) :
#     print ("*" * (id + 1))
# print (numero)


# print ("3.2 Même exercice que le précédent, mais avec l’affichage d’un sapin (triangle isocèle).")

# x = 10
# numero = range (1,int(x))
# for id,etoile in enumerate(numero) :
#     if etoile % 2 != 0 :
#         print ((" " * int((x - id)/2)) + ("*" * (id + 1)))
# print (numero)

# print ("3.4 Selon une légende hindoue, l’inventeur du jeu d’échec demande au prince que l’on place un grain de riz sur la première case, 2 sur la deuxième , 4 sur la troisième, 8 sur la quatrième… et ainsi de suite jusqu’à la soixante-quatrième case. Ecrire un programme qui calcule le nombre total de grains de riz.")

# tale = range(64)
# riz = []
# for id,i in enumerate(tale) :
#     a = (id+1)
#     b = (2**id)  
#     riz.append(b)
#     print (a,b)
# print (sum(riz))
    
# # print("3.5 Ecrire un programme qui lit votre prénom et qui affiche à l’envers avec chaque caractère suivi d’une étoile *. Utiliser la fonction prédéfinie len().")

# nombre = "DanielJoseArmando"
# new_name = []
# for id,i in enumerate(nombre): 
#     y = (nombre[int(len(nombre)-id-1)]+"*")
#     new_name.append (y)
# print ("".join(new_name))



# """4.1 Ecrire un programme qui lit un entier 
# n saisi au clavier et qui affiche :"""

# a = input ("Escrivez un numero > 99 :")
# # a = 30 
# b = range(1,int(a))
# print ("liste \n")
# for n in b :
#     print (n)
# print (a)

# print ("liste par \n")
# for n in b :
#     if n%2 == 0 :
#         print ("liste impar ", n)
#         continue
# if a%2 == 0 :
#     print (a)
    
# print ("liste impar \n")
# for n in b :
#     if n%2 != 0 :
#         print (n)
#         continue
# if a%2 != 0 :
#     print (a)    


# a = input ("Escrivez un numero > 99 :")
# # a = 30 
# b = range(1,int(a))
# print ("liste \n")
# for n in b :
#     print (n)
# print (a)

# print ("liste par\n")
# for n in b :
#     if n % 2 == 0 :
#         print (n)
        
# # if a % 2 == 0 :
# #     print (a)  
    
# print ("liste impar\n")    
# for n in b :    
#     if n % 2 != 0 :
#         print (n)
        
# if a % 2 != 0 :
#     print (a)   

# "MEJOR SOLUCION"

# liste = range (1,100)
# pair = []
# inpair = []

# for i in liste :
#     if i % 2 == 0 :
#         pair.append(i)
#     else :
#        inpair.append(i)
# print ("liste par ",pair)
# print ("liste impar ",inpair)

# # """4.2 Ecrire un programme qui lit n nombres 
# # réels et qui les affiches d’abord dans l’ordre et 
# # ensuite dans l’ordre inverse.""""

# a = [1,2,3,56,87,23,9,10,0,-1,-50,99]
# print("a) list en l'ordre :",sorted(a,key=None,reverse=False))
# print("b) list en l'ordre inverse :",sorted(a,key=None,reverse=True))



# # """4.3 Ecrire un programme qui lit n nombres 
# # réels et qui affiche leur minimum et maximum"""
# a = [1,2,3,56,87,23,9,10,0,-1,-50,99]
# print (a)
# print("a) maximum :",max(a))
# print("b) minimum :",min(a))



# """4.4 Ecrire un programme qui lit n nombres réels et 
# qui affiche leur moyenne."""

# a = [1,2,3,56,87,23,9,10,0,-1,-50,99]
# print("a) Moyenne :",round(sum(a)/len(a),2))

# "Mejor solucion"

# n = 5

# liste = []

# for i in range (n) :
#     x = i+1
#     liste.append(x)
# print ("a) Moyenne :", sum(liste)/len(liste))



# # """5.1 La distance entre deux points P1(x1,x2) et P2(x2,y2) dans 
# # le plan est définie par : d = racine carrée de ((X2-X1)²+(y2-y1)²).
# # Ecrire une fonction qui calcule cette distance après la saisie des coordonnées."""


# # Values
# from cmath import sqrt
# import math

# x1 = 1
# x2 = 2
# y1 = x2
# y2 = 4

# p1 = (x1,x2)
# p2 = (x2,y2)
# print ("P1 =",p1)
# print ("P2 =",p2)
# d = 0
# # formula
# a = (x2 - x1)**2
# b = (y2 - y1)**2
# c = a + b
# # print (a)
# # print (b)
# # print (c)
# d=math.sqrt (c)
# print ("Distance a",round(d,2))

# "Mejor solucion"

# def dist(x1 , x2 , y1 , y2):
#     distance = sqrt((x2-x1)**2 + (y2-y1)**2)
#     return distance
# # print("Introduire les coordonées de P1")
# x1 = 1
# y1 = 2
# # print("Introduire les coordonées de P1")
# x2 = 2
# y2 = 4

# da = dist(x1 , x2 , y1 , y2)
# print ("Distance b",round(float(da.real),2))

# # """5.2 Reprendre l’exercice précédent afin 
# # de calculer le périmètre d’un triangle formé 
# # par trois points non alignés."""

# from cmath import sqrt
# import math
# # Coordonnées
# p1 = (1,1)
# x1 , y1 = p1

# p2 = (1,3)
# x2 , y2 = p2

# p3 = (4,1)
# x3 , y3 = p3


# d=[]

# # forlmula
# d1 = ((x2 - x1)**2) + ((y2 - y1)**2)
# d.append( math.sqrt(d1))
# d2 = ((x2 - x3)**2) + ((y2 - y3)**2)
# d.append( math.sqrt(d2))
# d3 = ((x1 - x3)**2) + ((y1 - y3)**2)
# d.append( math.sqrt(d3))

# distance = sum(d)
# print ("Coordonnées")
# print ("p1",p1)
# print ("p2",p2)
# print ("p3",p3)
# print (d)
# print("Périmètre :",round(distance,2))



# # """5.3 Pour les anciens grecs, un nombre était 
# # trianguaire si l’on pouvait disposer ce nombre de cailloux 
# # en triangle. Tn = n(n+1)/2; Les 5 premiers nombres triangulaires 
# # sont : 1,3,6,10,15. Ecrire une fonction permettant de vérifier 
# # si un nombre saisi au clavier est triangulaire ou non."""

# b = int(input ("Numero :"))

# # Formula that returns the value of a number trianguarie
# def tn (n):
#     return n*(n+1)/2

# # empty list that holds the values that are trianguarie
# tn_list = []
# a = range(0,b)
# for x in a:
#     y=tn (x)
#     tn_list.append(y)
 
# # Formula that identifies the trianguaire 
# def isTrianguaire (b) :       
#     if b in tn_list :
#         print ("True ",b,"is a trianguaire")
#     else:
#         print ("False",b,"is not a trianguaire")
        
        
# isTrianguaire(b)

# # Test the formula in a list
# c = range (99)
# for i in c :
#     isTrianguaire (i)

# "Mejor solucion"

# def trl(x):
#     tn = 0
#     n = 0
#     while tn < x :
#         tn = n*(n+1)/2
#         n = n + 1
#     if tn == x :
#         tri = "yes"
#     else :
#         tri = "No"
#     return tri

# y = 3
# print (trl (y))



# """5.4 Ecrire une fonction entourant d’étoiles une 
# chaîne de caractères saisie au clavier."""


# Formula revisada

# text = "David"
# a = []

# b = len (text)*2 + 5
# for id,n in enumerate(text) :    
#     y=text[int(id)]
#     a.append(y)

# print ("*"*b)
# print ("* ",(" ".join(a))," *")
# print ("*"*b)

# # hacer la formula en def

# text = "David"
# # 
# # Main formula
# def textInSquare(text):
#     a=[]
#     b = len (text)*2 + 5
#     for id,n in enumerate(text) :    
#         y=text[int(id)]
#         a.append(y.upper()) # upper se escribe como referencia al valor
#     print ("*"*b)
#     print ("* ",(" ".join(a))," *")
#     print ("*"*b)

# # Test formula with a single value    
# textInSquare(text)

# # Test with a list

# liste_nombres = ["David", "Yassine", "Alessandra", "Youness", "Thomas"]

# for classmate in liste_nombres:
#     textInSquare(classmate)



# ***JOUR 04 Exercices supplémentaires***


# # "1. Hello, World!"
# nombre = input ("Comment tu t'appelles ? ")
# if len (nombre) != 0 :
#     print ("Hello "+nombre)
# else :
#     print ("Hello World!")
    

# 2. Pangramme

# total_en_letters = 26
# phrase = "Dans un wagon bleu, tout en mangeant cinq kiwis frais, vous jouez du xylophone"
# # phrase = input("Ecrivez la phrase ")
# clean_data_list = []
# for ltr in phrase.lower() :
#     if ltr not in clean_data_list :
#         if ltr != " " and ltr != "," :
#             clean_data_list.append (ltr)
# if len(clean_data_list) == total_en_letters:
#     print (True)
# else :
#     print (False)
# print(sorted(clean_data_list))


