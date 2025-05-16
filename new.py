# num = 15
# if num > 10:
#     print("Number is greater than 10")
# else:
#     print("Number is less than or equal to 10") 
#     #Next we see the use of Variables and lists
# # Variables and Lists   
# being_grownup = ["responsibility", "independence", "decision-making", "accountability"]
# print("Being a grown-up means having the following qualities:")
# for quality in being_grownup:
#     print(quality)
# # Next we see the use of Functions
# # Functions
# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Alice"))
name = any
answer = any
age = any
id_number = any
username = any
service = any
rosponses = any
print("Please enter your name")
name= str(input())
print("Welcome", name) 
print("Kindly register yourself by entering your ID Number")
id_number = int(input())
if id_number == id_number:
       print("Welcome", name)
else:
       print("Kindly put in the right information asked for")
       print("Please enter your ID Number")
       id_number = int(input())
print("Please enter your username")
username = input()
if username == username:
       print(username,"Welcome to Our website")
       print("are you here to vote")
answer = input()
if answer == "yes":
               print("Please enter your age")
elif answer == "no":
                print("Kindly state the service you are looking for")
                service = str(input())  
                if service == "vote":
                    print("Please enter your age")
                    age = int(input())
                    if age > 18:
                        print("You are ledgible to vote")
                    elif age == 18:
                        print("You are eligible to vote.Thank you for your Participance.")
                    else:
                        print("You are not eligible to vote. We hope you will be able to vote next time")
                elif service == "other":
                        print("Ask the clerk for any other services you need. Thank you for your time")
                else :print("Specify the service you are looking for")
if answer == "yes":
    print("Please enter your age")      
    age = int(input())
    if age > 18:
        print("You are ledgible to vote")
    elif age == 18:
        print("You are ligible to vote.Thank you for your Participance.")
    else:
        print("You are not eligible to vote. We hope you will be able to vote next time")
responses = input()
print("You are most welcome")