# TITLE< invente un program de toss coin avec un class
import random
from re import X

# choise = input("Enter pile ou face : ")
# if choise.lower() == "pile":
#     x = 1
# elif choise.lower() == "face" :
#     x = 0
# else :
#     "Mauvaise réponse, tu perds!"


# Game
       
# def game():
    
#     gameon = True
#     tosses = 0
#     wins = 0
    
    
#     while gameon:
        
#         # Random chance of wining
#         luck = random.randint(0,1)
        
#         print("------Pile ou face-----\n")
#         c = input("\nEnter pile ou face : ")
#         if c.lower() != "pile" and c.lower() != "face":
#                 print("\nMauvaise réponse, ecrit pile ou face, tu perds!")
        
#         # asing a value to the response
#         elif c.lower() == "pile":
#             x = 1
#         elif c.lower() == "face" :
#             x = 0
        
#         # calculate result
#         print("\n-----Result----") 
#         if x == luck:
#             # score a point
#             print (c,"Wins !")
#             wins += 1
#         else :
#             print (c,"Loses !")
        
        
#         tosses +=1
        
#         print("\n-----YourScore----")
#         print(wins,"/",tosses)
#         print("----------------")
   
#         replay = input("\nun autre jeu ? (y/n)")
#         if replay.lower() == "y":
#             gameon = True
#         else:
#             gameon = False
      
# game()    
# print ("\n----Sayonara baby----\n")    

    
    
# ------------------------------------------------------ OOP 

# TITLE< Solution avec une class

# TRY TO DO IT MORE EFICIENT !!!
    
class CoinToss:
    pass    
    
    @staticmethod    
    def game():

        gameon = True
        tosses = 0
        wins = 0
        
        while gameon:
            luck = random.randint(0,1)
            
            print("------Pile ou face-----\n")
            c = input("\nEnter pile ou face : ")
            
            if c.lower() != "pile" and c.lower() != "face":
                print("\nMauvaise réponse, ecrit pile ou face tu perds!")
                print("""\n    ৻(  •̀ ᗜ •́  ৻)""")
                        
            elif c.lower() == "face" :
                x = 0
            elif c.lower() == "pile":
                x = 1
                
            print("\n------Result------")
            try:
                if x == luck:
                    # score a point
                    print ("\n",c,"Wins !")
                    wins += 1
                else :
                    print ("\n",c,"Loses !")
            except:
                print("\nMauvaise réponse, tu perds!")
                print("""\n    ৻(  •̀ ᗜ •́  ৻)""")
        
            tosses +=1
            
            print("\n-----YourScore----")
            print("     ",wins,"/",tosses)
            print("------------------")
            

    
            replay = input("\nun autre jeu ? (y/n)")
            if replay.lower() == "y":
                gameon = True
            else:
                gameon = False
    


CoinToss.game()
print ("\n----Sayonara baby----\n")  
        
