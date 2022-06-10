# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True

# light_switch()
# light_switch()

def userNumber():
    user_input = input("Enter a number: ")
    try:
        {user_input} is (int(user_input))
        print(user_input)
    except:
        print("Invalid input")
        userNumber()


userNumber()
