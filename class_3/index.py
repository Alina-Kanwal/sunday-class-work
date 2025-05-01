# Positional Arguments
def login(email, password):
  user_obj = {
      "email":email,
      "password":password
  }
  print(user_obj)
login("ali@gmail.com" , "ali123") #Arguments


#Key Word Arguments
'''If we have many pparameter that means may be you could make a mistake while passing the argument
at the end we Key Word Arguments to solve this matter'''
def login(rollno,*,email, password, dob): # *, That showing that we will pass keyword arguments I used Position arguments before key_arguments
  user_obj = {
      "rollno":rollno,
      "email":email,
      "password":password
  }
  print(user_obj)
login(234567 ,email = "ali@gmail.com" , password = "ali123", dob="12_feb_2001") # Keyword Arguments are written by this way
login(234567 , password = "ali123", email = "ali@gmail.com" ,dob="12_feb_2001") #I changed sequence but get sequence after printing it

'''Rest Parameters in t.script
unlimited no of parameters with 3 dots'''
#Python
'''We use Double Asterics in python for => UNLIMITED ARGUMENTS'''

def volet(**Kuch_bhi):
  print(Kuch_bhi)

volet(money=24356 , nic="alina", coin="5")  #We could pass unlimited arguments keyword argument ki trhan pass hoga

def Binance(**kuch_bhi):
  print(kuch_bhi)

Binance(rupees="345" , dollar="76")

#Is string Class OR Data Type
'''Yes, String is data type But We use Class as a data_type We can made our custom data type for getting the exact
data we pass in any custom data_type'''

class Teacher(str):
  pass 
'''Teacher is now we are using as a data type but it is CLASS here. It is not necessary that string is data
type we use class to make custom data_type'''

teacher_name:Teacher = Teacher("Sir Ali Jawwad")
print(teacher_name)


#After installing mypy we could find mistake

teacher:int = "Sir Ali jawwad"
print(teacher)