"sets are unorderesd and unindexed IT sequence keeps change when we execute it.. We use it when order does not matter"
"undexed mtlb inka index number ni hota set does not allow duplicate values"
fruits = {"apple", "orange", "watermelon"}
print(fruits)    #ok 
# print(fruits[0]) #Error

# dic = {}
# set = set()

"""Python is dynamic type lanuage it does not show typeerror we use mypy for getting typeerror"""

#Python my data type dalny ka tareeka
# name:list= ["hi", "hello" , "how are u"]

# name:str= "ali" , "zainab"
name:list[str]= ["ali" , "zainab" , "ramsha" , 89] # Array of string
print(name)

number:int= 1,2,3,4         #number
# nnumber:int[int]=[1,2,3,4,5]       #Array of number

"""use of union """

Alina_choice : set = {"Red" , "Black"}
Aliza_choice : set = {"Red" , "Black" , "feerozi"}
merge = Alina_choice.union(Aliza_choice)
same = Alina_choice.intersection(Aliza_choice)
print(merge)
print(same)

#Agar zada array may set my say commomn nikalna hoo
wow_react:set = {"usman" , "Ali" , "hussain" }
laugh_react:set={"asma", "wahaj", "sajjad"}
heart_react:set={"wahi", "jameel", "saira"}
all = wow_react| laugh_react | heart_react               #pipe is als consider union
print(all)


#Intersection

set_one = {"jelly" ,"chocolate", "fruit"}
set_two = {"jelly" , "dairymilk", "milk"}
same = set_one.intersection(set_two)
print(same)

ali_friends = {"Hani" , "Hania", "shams" , "abdullah"}
hasseb_friends = {"muskan" , "malaika" , "shamama" , "Hania"}
myfriends = {"Alia" , "Hania" , "yumna ", "saira"}
mutual_friends = ali_friends & hasseb_friends & myfriends
print(mutual_friends)

winter_fruits = {"Apple" , "orange" , "mosambi", "pear"}
if "orange" in winter_fruits:
    print("orange")

if "banana" not in winter_fruits:
    winter_fruits.add("banana")

if "pear" in winter_fruits:
    winter_fruits.discard("pear")  

print(winter_fruits)    

cart:list=[
    {'product':'shoes' , 'price':'99'},
    {'product':'jweelery', 'price':'100'},
    {'product':'fan', 'price':'25'}
]
total:int = 0,
for expense in cart:
    total = total + expense['price']
    
print(total)

