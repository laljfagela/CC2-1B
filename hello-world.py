#Enter Name 
name=input("What is your name? ")

#Enter Age 
age_input=input("What is your age? ") #input , user put something 

age = int (age_input) #int converts string to numbers 
age_next_year = age + 1 

modulo = 5%3

pi = 3.1416 

print(f"Hello,",name , end= " & ")
print(f"Hello,{name}!")  #string {str} prints the text or characters 
print(f"Hello,",name , sep="$$$$$")
print(f"My age next year is", age_next_year)
print(f"Pi value is" , pi)
print(f"5 modulo 3 is", modulo)

#*objects - receives objects 
#sep = separator 
