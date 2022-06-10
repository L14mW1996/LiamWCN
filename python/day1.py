# import random
# #imports random library

# greeting = "Hello world" #declaring greeting variable as string

# print(len(greeting))#prints length of string defined as greeting

# w_amount = 100
# account_num = 12345678

# def cash_withdrawal(amount, accnum): #defining cash withdrawal function
#     print(f"Withdrawing {amount} from account {accnum}") #print string with text and properties

# cash_withdrawal(w_amount, account_num) #defining properties
# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# coffee_order[1]= "Ann - Vanilla latte"

# print(coffee_order[2]) #Prints out third item from list, as it starts counting from 0

# for i in coffee_order:
#     print (i)          #prints list

# for i in range(0,11,1): #prints to 10 in integers of 1
#     print(i)

# for x in range (0,21,2): #prints to 20 in integers of 2
#     print(x)

# n = 0 #defining n as 0
# while n <10: #when n is less than 10
#     n += 1 #add 1 to n
#     print(n) #print n
# #loop stops when number reaches 10

str1 = str(54)

print(str1)

print("What is your name?")
name = input()

if name:
    print(f"Hello {name}, how are you?")
else:
    print ("You did not give me your name!")

def add_up(): 
    num1 = input("What is the first number you'd like to add up? \n") 
    num2 = input("What is the second number you'd like to add up? \n") 
    try: 
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!") 
    except: 
        print("\n ERROR: please input only numerical values. \n") 
        print("**************************** \n") 
        add_up() 
add_up() 

