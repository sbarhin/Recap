# Script to authenticate withdrawal
def user_inpt():  # input function
    user = int(input("Enter your pin: "))
    return user


def authenticate(x):  # code for authentication
    for i in range(3):  # Number of chances
        if user_inpt() != pin:
            x -= 1
            if x == 0:
                print("Sorry, you have wrongfully entered your pin three times. Try again later ")
                break
            print(f"Wrong pin entered. You will be logged out after {x} unsuccessful attempts")
        else:
            print("Login successful.Please proceed to make withdrawal.")
            break


pin = 2022  # Reference pin
authenticate(3)
