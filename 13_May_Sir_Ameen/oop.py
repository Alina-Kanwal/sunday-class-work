'''We are learning from this repo of panaversity
https://github.com/panaversity/learn-modern-ai-python/tree/main/00_python_colab/13_traditional_oop_part_2'''

'''Abstraction means background par kea horha hay
Variable for storing data We make variable for making refrence in memory
Constructor us wqt bunta hy jb class ka instance/object create hota hy
jb class chlti hy sb say phly constructor chlta hy kyu ky wo return my obj dy raha hota hy'''

# class Bankaccount:
#     account_number:str = "ABC"
#     def __init__(self):
#         self.account_number:str = '5566'
       
# # alina_account = Bankaccount()           #This is instance creation 
# print(Bankaccount.account_number)          #ABC class varaiblr call hoga
# Bankaccount.account_number = "xyz"          
# print(Bankaccount.account_number)          #XYZ

# #NOW WE ARE GIVING HUZAIR TYPE 
# huzair:Bankaccount = Bankaccount()
# print(huzair.account_number)             #self wala yani instance varaible call hoga 5566
# huzair.account_number = "1515"
# print(huzair.account_number) 

# What if we remove self part

# class Bankaccount:
    # account_number:str = "ABC"
    
       
# alina_account = Bankaccount()            #This is instance creation 
       
# print(Bankaccount.account_number)          #ABC
# huzair:Bankaccount = Bankaccount()         
# print(huzair.account_number)               #ABC

# Bankaccount.account_number = "xyz"         #class ky varaiable ko change kea
# print(Bankaccount.account_number)          #XYZ
# print(huzair.account_number)               #instance ka varaible bh change hogya xyz may


# huzair.account_number = "CHANGE1"
# print(Bankaccount.account_number)   #yhn XYZ raha .Yani class varaible change ni hoa instance varaible change krny say
#                                     #kyu ky is ky pass y power ni hy ky ye globally jakar class ky varaible ko change kry

# huzair.phone_number = "H"
# print(huzair.phone_number) # H That means python can add refrence of a varaible which does exist in stack(self waly part my)










