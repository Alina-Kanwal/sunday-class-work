import requests
months:list = ["December" ,"february" , "March" , "April" , "May" , "June" , "July" , "August"]
print(months[0:3])
print(months[3:6])           #5 tak element ko get krna
print(months[3:])            #is trhn jo bh element add hoty rahyengen wo add hongy
months[0] = 'January'        #update krdea
print(months)

#Slicing my negative indexing
print(months[-3:-1])

#Tuples / Immutable version of list
numbers: tuple = ("Ali Jawwad", "Hasseb" , "Ahmed")
print(type(numbers))
print(numbers)


#What when if we want to change/update tuple
#We change tuple into list
tuple_to_list = list(numbers)
print(tuple_to_list)
print(type(tuple_to_list))

print(tuple_to_list.append('Sir Ali'))
print(tuple_to_list)

#Dictionary
student_info = {
    'Roll number': 1235678,
    'Name': 'Alina Kanwal',
    'Courses':["NextJS", "Fast API" , "OPen AI" , "Agents"],
    'assigment info': {
        'assignOne':'completed',
        'assignTwo':'In-process',
    }

}

#How to get dictionaries
# print(student_info["Courses"])
# print(student_info["assigment info"])
# print(student_info["Courses"][2])

#Loop through values
for abcd in student_info.values():
    print(abcd)

#Loop through Key and values    

for keys,values in student_info.items():
    print(keys,values)

#Works under range 
for i in range(1,10):
    print(i)

try:
   url = requests.get("https://jsonplaceholder.typicode.com/posts")
   res = url.json()
   print(res)
except Exception as e:
    print(e)   
