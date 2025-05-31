class Library:
    #jb bh koi function class ky undr bna ho usy method khty hain
    # jo cheez self k sath declare hoti hy wo class ko refer krti hy
    def __init__(self , name , location): #__init__ is a constructor , name is called local variable, parameter
        self.name = name       # self.name is an instance variable     
        self.location = location

#function ko call krna obj khlata hy , Just a convention or placeholder name.
obj = Library('The Library' , 'Karachi') 
#yhn hum __init__ ko call ni kea blky Library ko call kyu ky constructor fun ko call python krta hy
