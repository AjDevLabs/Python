import os
file = "contacts.txt"
contacts = []

# if file does not exist create file
if not os.path.exists(file):
        db = open(file,'w')
 
with open(file,'r') as f:
        for line in f:
                l = line[:-1]
                d = eval(l)
                contacts.append(d)
        

def create():
        name=input("Enter the name")
        mobile=input("Enter the number")
        email=input("Enter the e-mail")
        contact = {'name':name,'mobile':mobile,'email':email,'blocked':False}
        print(contact)
        contacts.append(contact)
        print("\nContact Saved!")
    
def edit():
        i = search(input("Enter Mobile no. to be searched : "))
        d = contacts[i]
        d['name'] = input("Enter New Name : ")
        d['mobile'] = input("Enter New Mobile : ")
        d['email'] = input("Enter New Mobile : ")
        contacts.pop(i)
        contacts.append(d)
        
def display():
 #       print(type(contact))
        for contact in contacts:
                print("Name : ",contact['name'])
                print("Mobile :",contact['mobile'])
                print("email : ",contact['email'])
                print("blocked : ",contact['blocked'])
                print()
                
def delete():
        i = search(input("Enter Mobile Number  to be deleted :"))
        contacts.pop(i)
        print("Contact has been sucessfully deleted!")

    
def block():
        i = search(input("Enter Mobile NO. : "))
        d = contacts[i]
        d['blocked']=True
        contacts.pop(i)
        contacts.append(d)

        
        
def show_block():
         for contact in contacts:
                if(contact['blocked']):
                        print("Name : ",contact['name'])
                        print("Mobile :",contact['mobile'])
                        print("email : ",contact['email'])
                        print("blocked : ",contact['blocked'])
                        print()

def search(mobile):
        index = 0
        while index<len(contacts):
                contact = contacts[index]
                if(contact['mobile']==mobile):
                        return index;
                index+=1
        return 0

ch = 1
while 1:
    print("\n\n\n")
    print("**********WELCOME TO THE NEW CONTACT BOOK**********")
    print("1.Create the contact\n2.Edit the contact\n3.Display the contact info\n4.Delete the contact\n5.Block a number\n6.Show the list of blocked numbers\n7.Exit")
    cb=int(input("Enter the choice:"))
    if cb==1:
        print("\n")
        create()
    elif cb==2:
        edit()
    elif cb==3:
        display()
    elif cb==4:
        delete()
    elif cb==5:
        block()
    elif cb==6:
        print("list Block Numbers")
    elif cb==7:
        with open(file,"w") as f:
                for contact in contacts:
                        f.write(str(contact))
                        f.write("\n")
        exit()
    else:
        print("\nInvalid Entery!")


