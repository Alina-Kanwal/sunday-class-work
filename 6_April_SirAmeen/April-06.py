# '''Python colab step 00 t0 11 shortly'''

# #02-data-types
# '''Python does not check type Thats why we install mypy . mypy is an compiler it will check type while running the code'''
# teacher:int = 'Sir Ali jawwad'
# print(teacher)

# #operators in python will be studid by own


# #04-string casting
# '''implicit wo hota jo declare ni kea
#    declicit jo declare kea ho''' 


# #05-control-flow
# '''کون سا کوڈ کب اور کیسے چلے گا؟
# کیا کچھ کوڈ کو چھوڑ دینا ہے؟
# کیا کچھ کوڈ بار بار چلانا ہے؟'''
# '''jaisay for loop if statement in sub ka scene alag alag hota hy control flow yani dkhna ky kahn kea krna hy'''
# '''Python is high level language because it manage many works by own for example if i '''

# teacher:str = 'Sir Ali jawwad'  #string is immutable matlb jb assign kea teacher ko dubara tw wahan change ni hoa 
# #blky aik copy bana kar wahan save kardea iska mtlb y hy ky string or int my variable ki aik new location 
# # bunti hy jb wo update hota hy assign hota hy

# sunday_teacher:str= teacher 
# print(teacher)        #'Sir Ali jawwad'  iski alag location hy
# print(sunday_teacher) #'Sir Ali jawwad'  iski alag location hy 


# #list and tuples
# '''List my time complexity zada hoti hy yani bar bar data add krny ki wja say time zada 
# lgskta hy jb ky tuple may aesa ni hota'''
# lit:list=[1,2,3] #can add more data
# lit:tuple=(1,2,3) #can't add more data

# '''Both variable have values after assigning it first waly teacher ky pass ni hona chahye tha kyu ky wo 
# tw agy pass krdea hy data  Here sir Ameen give us an example of a man who went hotel'''
# '''
# *variable ky pass data ni data ki location hoti hay 
# *string integer replce hojaty hain magar list my mzeed element add hoskty hain'''
# '''Backend ky under obj hota hy C ky under symbol ky name ka obj hota hy jb bh aik variable ki location 
# dosray variable ki location say bt krti hay jisko hum pointer khty hain '''


'''python my refrence ka mtlb same cheez dena jaisay ye immutable data may hota hy'''
teacher:int='Sir ali'       #01-jaga data #jo yhn tha
class_teacher = teacher              
teacher = 'sir Ahmed raza'  #02-jaga data #yhn update krny par naya data aya hay porana nahin kyu ky string immutable hota
print(teacher)
print(class_teacher)

# '''Past Bar refrence may Python my hmeesha data ka refrence pass hota hay kyu ky ye high level programing 
# language hy list ky case may refrence chalta hy yani mutable variable may '''
# lit:list=[1,2,3,4] # refrence dea mtlb yhi data
# abc:list=lit       # yhn bh agya
# lit.append(5)
# print(lit)
# print(abc)


# text = "café"
# b1 = text.encode('utf-8')
# b2 = text.encode('latin-1')

