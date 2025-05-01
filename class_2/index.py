#class 2
animals = ["cat", "cow", "Got", "Dog"]
print(animals[0])

Book={
    "author": "zain",
    "Book"  : "My_story"

}
print(Book["author"])
print(type(Book))

#conditions
weather = input("How weather is? ").lower()


if(weather == "sunny"):
  print("Stay hydrated")
elif(weather == "cold") :
  print("Take care")
elif(weather == "rainy"):
  print("Weather is rainy")
else:
  print("normal weather")


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your first number: "))
opp = input("Enter (add/div)").lower()
if(opp == "add"):
  print(f"{num1 + num2}")
elif(opp == "div"):
  div = num1 // num2
  print(div)


list = ["Biryani" , "Tikka" , "Colddrink"]

if("Biryani" in list):
  print("Best Dinner")
elif("coldrink" not in list):
  print("acha hoa")

if("Biryani" in list) and ("korma" in list) and ("Tikka" in list):
  print("not Good")
else:
  print("we will eat")

if("Biryani" in list) or ("korma" in list) or ("Tikka" in list):
  print("Khana dy do mujh")    


def greet(name , email=None):
  print(f"Your name is {name} and email is {email} ")

greet("Alina", "alinakanwal840@gmail.com")
greet("wickey")  


#Default Parameters
def marriage(choice = "Ami ki psnd"):
  print(choice)
marriage()
marriage("Meri psnd")
