welcome = "Welcome to Code Nation"
welcome_length = len(welcome)

def length_check(x):
    if(x % 2) == 0:
        print("The string length is even")
    else: print("The string length is odd")

length_check(welcome_length)

alphabet = [
    "A ",
    " B ",
    " C ",
    " D ",
    " E ",
    " F ",
    " G ",
    " H ",
    " I ",
    " J ",
    " K ",
    " L ",
    " M ",
    " N ",
    " O ",
    " P ",
    " Q ",
    " R ",
    " S ",
    " T ",
    " U ",
    " V ",
    " W ",
    " X ",
    " Y ",
    " Z "
]

user_letter = int(input("Enter a number between 1 and 26: "))
print (alphabet[user_letter -1])