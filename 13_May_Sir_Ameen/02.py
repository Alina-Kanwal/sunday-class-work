#COMPOSITION REALATIONSHIP   (strong realation)
#AGGREAGATION REALATIONSHIP  (weak realation)

class User:
    def __init__(self , name):
        self.name = name
       
class Realstate_Property():             #bank ky khtm hony par adress khtm ni hoga is lea y aggregation realationship hy    
    def __init__(self, address):
        self.address = address  

address = Realstate_Property("Karachi") #Because obj bahar bana kr obj ko pass krrhy hain
                                        #ab agr b.a/c khtm hogya tw address khtm ni hoga             
class Bankaccount:
    def __init__(self, uname , address, balance = 0):
        self.user = User(uname)  #yhn user ko hum ny upar say uthaya y composite realation 
        self.address = address   #hy kyu ky bank ka user ky sath strong realation hy
                                 #inherit is lea ni kea kyu ky user Bankaccount ka parent ni hoskta 

ameen_account:Bankaccount = ("Ameen" , "55" , address)        
        

