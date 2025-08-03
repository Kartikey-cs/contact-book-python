q=0
i=2
import math
def ask():
    global q
    try:
      q=int(input("Input Positive Number "))
    except:
      print("Try Again")
      ask()
ask()
def condition():
    global i,q
    if q <=1:
     print("DUMB DUMB")
     ask()
     condition()
    elif q>=1:
       while i<q:
         if q%i==0:
          print("Not Prime")
          i=q+1
         else:
          i+=1
condition()
if i==q:
  print("Prime")