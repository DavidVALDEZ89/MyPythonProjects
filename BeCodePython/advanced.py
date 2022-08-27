# TITLE< Objets 

# class Voiture:  #On utilice toujours mayuscule dans la premiere part
#     # opens the constructor
#     def __init__ (self, nom, colour, top_speed):
#         # les characteristiques de la class
#         self.nom = nom
#         self.colour = colour
#         self.top_speed = top_speed

# laferrary205 = Voiture ("Ferrary","Rouge","350 km/hr")

# print (Voiture)
# print (laferrary205.nom)  #El objeto ahora tiene estas variables, y las podemos utilizar


# class Personne:
#     def __init__ (self,nom,prenom,age,residence,aniversaire):
#         self.nom=nom  #Variable et valor , se convierte en un method
#         self.prenom=prenom
#         self.age = age
#         self.residence = residence
#         self.aniversaire = aniversaire
#         self.type = "humain"
        
#     def bonjour (self):  #cuando escribimos self, jala todas las caracterisitcas de la clase
#         print ("Bonjour",self.prenom,self.nom, "tu as :",self.age,"tu habites en :",self.residence)
#     def aniv(self):
#         print ("Bonjour",self.nom,"ton aniversaire est :",self.aniversaire)
        
# david = Personne("VALDEZ","David",32,"Uccle","23/10/1989")
# jose = Personne("Jose","juarez",35,"Mex","23/67/1234")

# eleves = [david,jose]
# print (eleves)
# print ("-------------")
# for i in eleves:
#     i.bonjour()
#     i.aniv()
#     print()
    
# # # Class compteur
# class Compteur:
#     #Cette classe a un attribut (`objets_créés`) qui est incrémenté chaque fois que vous créez un objet de ce type
#     objt_crée = 0  #le compteur est 0 au départ
#     def __init__(self):
#         Compteur.objt_crée = Compteur.objt_crée + 1
# # premier objet
# for i in range (10):
#     i = Compteur ()
# print(Compteur.objt_crée)



# # Method
# class Blackboard:
#     def __init__ (self):
#         self.surface = ""
#     def write (self,message_writen):
#         if self.surface :
#              self.surface += "\n"
#         self.surface += message_writen
#     def read (self):
#         print ("Thanks to print, the surface of the painting")
#     def reset (self):
#         self.surface = ""
        
# board = Blackboard()
# print (board.surface)
# board.write("Hello world")
# board.write("Are you all right?")
# print (board.surface)
# board.read()
# board.reset()
# print (board.surface)

# TITLE< Practice time!

# class Becodian:
#     def __init__(self,name,is_staff_member):
#         self.name = name
#         self.is_staff_member = is_staff_member
#     def introduce_becodian(self):
#         if self.is_staff_member:
#             return f"{self. name} is a staff member!"
#         else :
#             return f"{self. name} is a lerner!"
        
# class Learner (Becodian):
#     def __init__(self,name,promotion):
#         super().__init__(name,promotion)
#         self.promotion = promotion
#         self.name = name
#         self.is_staff_member = False
#         print (f"{self.introduce_becodian()} is in the course {promotion}")
              
# thomas = Becodian("Thomas",True)
# david = Learner ("David","Python Advanced")
# jeremy = Learner("Jeremy", "Bouman 1")
# giuliano = Learner("Giuliano", "Bouman 1")
# mathieu = Learner("Mathieu", "Bouman 1")
# geoffrey = Learner("Geoffrey", "Bouman 1")
# adrien = Becodian("Adrien", True)

# members = [thomas, david,jeremy,giuliano,mathieu,geoffrey,adrien]
# # print (members)
# for member in members:
#     if member.is_staff_member == True:
#         print(member.introduce_becodian())
#     else :
#         print(member.introduce_becodian(),member.promotion)
# staff = []
# students = []

# for member in members:
#     if member.is_staff_member == True:
#         staff.append(member)
#     else :
#         students.append(member)

# print("---------\nStaff :\n")
# for member in staff:
#     print(member.introduce_becodian())
# print("---------\nStudents :\n")
# for member in students:
#      print(member.introduce_becodian(),"from ",member.promotion)

# print (thomas.name,thomas.introduce_becodian())
# print (david.name,david.introduce_becodian(),david.promotion)

# class Becodiann:
#     def __init__(self):
#         self.name = ""
#         self.is_staff_member = ""
#     def introduce_becodian(self):
#         if self.is_staff_member:
#             return f"{self. name} is a staff member !"
#         else :
#             return f"{self. name} is a lerner !"

# item1 = {"name" : "Tomas", "s_staff_member" : False}  #We can use a dictionary inside of a class
# c_item1= Becodiann()  #For that we need to call it
# c_item1.name = "Tomas" #And we need to name it as well

# print ("--------------")
# print (c_item1.introduce_becodian())



# TITLE< Exercise de person et method class

# from datetime import datetime
# import re


# class Person:
#     def __init__ (self, name, year, month, day):
#         self.name = name
#         self.year = int(year)
#         self.month = int(month)
#         self.day = int(day)
#         self.birthday = datetime(self.year,self.month,self.day)
#         self.age = round(((abs(datetime.now() - self.birthday).days)/365),1)
    
#     # metodo dentro de la Clase que afecta a la clase
#     def bday (self,lang):
#         self.lang = lang
#         if self.lang == "en":
#             print (f"Hello {self.name}!, you where born in {self.birthday}, you are {self.age} years old")
#         elif self.lang == "fr":
#             print (f"Bonjour {self.name}!, t'est né le {self.birthday}, t'as {self.age} ans")
#         else :
#             print (f"Que onda {self.name}!, sabemos que tu naciste el {self.birthday}, y que tienes {self.age} años, sabemos donde vives, Skynet esta viva !")
             
# dav3 = Person("David",1989,10,23)

# print("---------")
# dav3.bday("fr")
# print("---------")
# dav3.bday("en")
# print("---------")
# dav3.bday("?")
# a = (1989,10,23)
# b = ((abs((datetime.now() - datetime(a[0],a[1],a[2])).days))/365)
# print (round(b,1))



# TITLE< Execercide method @static

# class Animaux:
#     def __init__ (self, name,espèce):
#         self.name = name
#         self.espèce = espèce
#         self.carnivore = False
#     def zoo(self):
#         print (f"{self.name} is a {self.espèce}")
    
#     def carniv (self) :
#         if self.carnivore == True :
#             print ("this is a carnivore")
#         else :
#             print ("this is not a carnivore")    
    
    
    
#     def sumee (self,a,b):  # Tiene que ser un metodo estatico para que funcione o agregar Self al inicio de la formula
#         print (a + b)
    
    
        
#     @staticmethod #  es una funcion que existe en la clase y que utiliza informacion duera de sus atributos
#     def carn (n) :
#         if n == True :
#             print ("this is a carnivore")
#         else :
#             print ("this is not a carnivore")
        
# item1 = Animaux("Gatita", "Chat")
# print (item1)

# item2 = 1

# item1.zoo()
# print (item1.carnivore)
# item1.carn(True) # te permite defirnirlo en la operacion
# # item1.carniv(True) # no se define aqui, se define con el objeto
# item1.sumee (1,2)
# print ("---------------see this -----------------")
# Animaux.carn(False)  #We can use the method without an object
# print ("---------------see this -----------------")
# # Animaux.carniv(self)  #this will give us an error due the formula depends of an object   



# TITLE< other example 
    
# class Blala:
#     # if you dont name the constructor, we have nothing to modify
#     def age(age_number):
#         if age_number <= 30:
#             print("Young")

#         elif age_number <= 50:
#             print("Middle Age")

#         else:
#             print("Senior Age")


# John = Blala # when we transform the object, you dont use the () because the class is empthy
# age_category = (John.age(45))



# TITLE< One more static method example

# class Dates:
#     def __init__(self, date):
#         self.date = date
        
#     def getDate(self):
#         return self.date

#     @staticmethod  #We use this type of formulas to create formulas that can be used with an input, they are called within a calss, without an object!
#     def toDashDate(date):
#         return date.replace("/", "-")

# date = Dates("15-12-2016")
# dateFromDB = "15/12/2016"
# dateWithDash = Dates.toDashDate(dateFromDB)

# print( Dates.toDashDate("2105/10/2"))  #This element is not an Object, but is using a function out of a class


# if(date.getDate() == dateWithDash):
#     print("Equal")
# else:
#     print("Unequal") 



# TITLE< Try and Error
# we can bypass ans expected error or defined with except, else or finaly

# try:
#     print (3/3)
# except ZeroDivisionError:
#     print ("Error in line 2")

# else:
#     print("Everything is ok")
    
# def division(num, div):
#     if div == 0:
#         raise ZeroDivisionError
#     else:
#         return num / div


# division(5, 0)



# # TITLE< Regular expresions

# # Use a string to check if a given value is a number

import re

# number = "1"
# # traditional method
# if re.match("^[0-9]+$", number):
#     print("The string entered is a number.")
# else:
#     print("The string entered is NOT a number.")
# # Triad method
# print(("The string entered is NOT a number.","The string entered is a number.")[bool(re.match("\d", number))])


# s = "sssgdds 8 Dave sfs9fs"
# x = re.match("[ ]",s)
# print (x)

# pattern = "There"
# string = "I am fine ! There are still 6 months left :()"
# print (string [12]) # Le search returne dans le =span(a,b) a = localization del premier character sur le string, et b= le dernier character de le string

# # Searches the pattern in the previous string and return a `MatchObject` if matches are found,
# # otherwise returns `None`.
# print(re.search(pattern, string))  #busca y da como resultado la palabra
# print(re.match("I am fine ! There are still 6 months left :()", string))  #Compara y encuentra los valores



# # EXCERCICE< 1. Create a regex that find integers without size limit
# s = "sssgdds8sfs9fs"
# x = re.findall("\d",s)
# print (x)



# # EXERCICE< 2. create a regex that finds negative integers without size limit
# s = "sssgdds-8sfs-9fs"
# x = re.findall("-\d",s)
# print (x)



# # EXCERCE< 3. Create a regex that finds positive or negative integers without size limit
# s = "s1s7sg-34dds-8s8fsf9s-76"
# x = re.findall("-?\d",s)
# print (x)



# # EXCERCE< 4. Capture all the nulbers of the following sentence:
# text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00%\ happy."
# x = re.findall("\d+\.?,?\d*",text)
# print (x)
# textt = "21 21 3333"
# z = re.findall("\d+\.?,?\d*",textt)
# print (z)



# # EXCERCICE< 5. Find all words that end with 'ly'
# text = "He had prudently disguised himself but was quickly captured by the police."
# x = re.findall("\w+ly",text)
# print (x)



# # EXCERCICE< 6.License number

# plate_list = ["AA-889-DD","DD-E12-AA","11-AAA-11","AA.111.AA","AF-885-HD","AA","aerzfdezfzdzdzedz"]
# for plate in plate_list:
#     if len(plate) == 9 and re.match("[A-Z]{2}-\d{3}-[A-Z]{2}",plate):  
#         print (f"Ok _{plate}_ is a valid plate")
#     else:
#         print (f"Error _{plate}_ is not a valid plate")

# # # We can do it in a single liner
# for plate in plate_list : print((f"Error _{plate}_ is not a valid plate" , f"Ok _{plate}_ is a valid plate") [bool(re.match("\w\w\-\d\d\d\-\w\w" , plate))] )

# # We can do it as a loop
# plate_program = True
# while plate_program == True :
#     plate = (input("Enter your license plate number (AA-000-AA): "))
#     print((f"Error _{plate}_ is not a valid plate" , f"Ok _{plate}_ is a valid plate") [bool(re.match("[A-Z]{2}-\d{3}-[A-Z]{2}" , plate))] )
#     if str.lower(input ("Do an other consult (y/n): ")) == "y" : plate_program = True 
#     else : plate_program = False ; print ("Thank you for using our services, we hope to see you soon!")
    
# # Finaly, we can do all of that as a def and call it back
# def plate_prog():
#     plate_program = True
#     while plate_program == True :
#         plate = (input("Enter your license plate number (AA-000-AA): "))
#         print((f"Error _{plate}_ is not a valid plate" , f"Ok _{plate}_ is a valid plate") [bool(re.match("[A-Z]{2}-\d{3}-[A-Z]{2}" , plate))] )
#         if str.lower(input ("Do an other consult (y/n): ")) == "y" : plate_program = True 
#         else : plate_program = False ; print ("Thank you for using our services, we hope to see you soon!")
    
# plate_prog()



# # EXERCICE< 7. Address IPV4
# pattern = "([0-255])\.([0-255])\.([0-255])\.([0-2]{0,1}[0-5]{0,1}[0-9]{0,1})" #Revisar, esto esta mal
# ipv4_program = True
# while ipv4_program == True :
#     ipv4_ = (input("Enter your IP address : "))
#     print((f"Error _{ipv4_}_ is not a IP address" , f"Ok _{ipv4_}_ is a IP address") [bool(re.match(pattern , ipv4_))] )
#     if str.lower(input ("Do an other consult (y/n): ")) == "y" : ipv4_program = True 
#     else : ipv4_program = False ; print ("Thank you for using our services, we hope to see you soon!")



# # EXERCICE< 8. Valid eMail
# pattern = "\w+[\._]?\w*[@]\w*[.]\w{2,3}"
# email_program = True
# while email_program == True :
#     email = (input("Enter your e_mail address : "))
#     print((f"Error <{email}> is not a e_mail address" , f"Ok <{email}> is a e_mail address") [bool(re.match(pattern , email))] )
#     if str.lower(input ("Do an other consult (y/n): ")) == "y" : email_program = True 
#     else : email_program = False ; print ("Thank you for using our services, we hope to see you soon!")
 



# # EXERCICE< 9. Valid Password after email; 6> characters
# pattern_email = "[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]*[@][a-zA-Z0-9]*[.]\w{2,3}"
# pattern_passw = "\w{6,}"
# val_program = True
# while val_program == True :
    
#     email = (input("Enter your e_mail address : "))
#     print((f"Error <{email}> is not a e_mail address" , f"Ok <{email}> is a e_mail address") [bool(re.fullmatch(pattern_email , email))] )
    
#     passw = (input("Enter your password \n  (it must contain 6 characters : "))
#     print((f"Error <{passw}> is not a valid password" , f"Ok <{passw}> is a a valid password") [bool(re.fullmatch(pattern_passw , passw))] )
    
#     if str.lower(input ("Do an other consult (y/n): ")) == "y" : val_program = True 
#     else : val_program = False ; print ("Thank you for using our services, we hope to see you soon!") 
 
 
 
 
# EXERCICE< 10. Valid Password after email
# pattern_email = "[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]*[@][a-zA-Z0-9]*[.]\w{2,3}"
# pattern_passw = "[A-Za-z0-9$#@]{6,}" #"[a-z]+[0-9]+[A-Z]+([$]?[#]?[@]?)+"
# val_program = True
# while val_program == True :
    
#     email = (input("Enter your e_mail address : "))
#     print((f"Error <{email}> is not a e_mail address" , f"Ok <{email}> is a e_mail address") [bool(re.match(pattern_email , email))] )
    
#     passw = (input("Enter your password \n  (it must contain 6 characters, \n  at least one lowercase,\n  at least one uppercase,\n  at least one number and \n  at least one special character among $#@) : "))
#     print((f"Error <{passw}> is not a valid password" , f"Ok <{passw}> is a a valid password") [bool(re.fullmatch(pattern_passw , passw))] )
    
#     if str.lower(input ("Do an other consult (y/n): ")) == "y" : val_program = True 
#     else : val_program = False ; print ("Thank you for using our services, we hope to see you soon!")
