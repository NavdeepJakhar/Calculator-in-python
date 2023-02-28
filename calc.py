# Basic Calculator

# 5 functions - addition, subtraction, multiplication, division, modulus
def addition(n1,n2):
    print("Addition of",n1,"and",n2,'=',n1+n2)

def subtraction(n1,n2):
    print("Subtraction of",n1,"and",n2,'=',n1-n2)

def multiplication(n1,n2):
    print("Multiplication of",n1,"and",n2,'=',n1*n2)

def division(n1,n2):
    print("Division of",n1,"and",n2,'=',n1/n2)

def modulus(n1,n2):
    print("Modulus of",n1,"and",n2,'=',n1%n2)

    
    
# This is the main() function.
print("--------- CALCULATOR ---------\n(Choose the corresponding number to the operation you want to perfrom.)\n")
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Modulus\n-------------------------------')

ch=int(input("Enter your choice : "))
if ch<0 and ch>5:
    print("Invalid Choice")
    quit()

n1=int(input("\nPlease enter the numbers => \nFirst number : "))
n2=int(input("Second number : "))
print('-------------------------------')

if ch==1:
    addition(n1,n2)
elif ch==2:
    subtraction(n1,n2)
elif ch==3:
    multiplication(n1,n2)
elif ch==4:
    division(n1,n2) 
elif ch==5:
    modulus(n1,n2)       

print('-------------------------------')