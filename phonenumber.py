#contact book
import math
import json
contact={}
try:
    with open("wow1.json", "r") as f:
     contact = json.load(f)
except ( json.decoder.JSONDecodeError, FileNotFoundError):
     contact={}
c=1
def add():
    name=input("Enter name ")
    num=input("Enter number ")
    contact[name]=num
def delete():
    a=input("What to delete ")
    try:
         del contact[a]
    except  KeyError as e:
         print("Not Found Name")
def edit():
         name=input("Enter Name ")                               
         contact[name]=input("Input Number")
while c==1:
    print("press 0 to add contact")
    print("1 to edit contact")
    print("2 to delete contact")
    print("3  to view contact book")
    print("4  to exit the program")
    q=abs(int(input()))
    if q==0:
        add()
    if q==1:
        edit()
    if q==3:
        print(contact)
    if q==2:
        delete()
    if q==4:
         print("Thanks")
         with open("wow1.json", "w") as f:
             json.dump(contact,f)
             c=2
    elif q>4:
         print("Error Retryy")
 