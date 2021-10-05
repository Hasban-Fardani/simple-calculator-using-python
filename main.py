import os
import time
import sys

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    YELLOWBG = '\33[103m'
    FAIL = '\033[91m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

def clean():
    print(colors().CLEAR)
    if sys.platform == "linux" or "mac" in sys.platform:
        os.system("clear")
    elif "win" in sys.platform:
        os.system("cls")


while True:
    clean()
    print(colors().BLUE,colors().BOLD,"================ welcome to Hasban calculator ================\n\n", colors().CLEAR)
    operation = input(colors().YELLOW+"please select the operation (+, -, x, :, %) or q for quit >> "+colors().CYAN, )
    if operation == "q":
        clean()
        print(colors().YELLOWBG +"thank you for using this calculator" + colors().CLEAR)
        break
    elif operation not in ["+", "-", "x", ":", "%"]:
        print(colors().FAIL+"operation not found, please enter the correct operation", colors().CLEAR)
        time.sleep(2)
        clean()
        continue
    else:
        num1 = int(input(colors().CLEAR+"enter a number      : "+colors().CYAN, ))
        num2 = int(input(colors().CLEAR+"enter second number : "+colors().CYAN, ))
        if operation == "+":
            print(f"{colors().GREEN}{num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            print(f"{colors().GREEN}{num1} - {num2} = {num1 - num2}")
        elif operation == "x":
            print(f"{colors().GREEN}{num1} x {num2} = {num1 * num2}")
        elif operation == ":":
            print(f"{colors().GREEN}{num1} : {num2} = {num1 / num2}")
        elif operation == "%":
            print(f"{colors().GREEN}{num1} % {num2} = {num1 % num2}")

        while True:
            cont = input(colors().YELLOW + "\ncontinue (y/n)? " + colors().CYAN, )
            if cont == "n" or cont == "N":
                clean()      
                print(colors().GREEN + "thank you for using this calculator")
                break
            elif cont == "y" or cont == "Y":
                clean()
                break
            else:
                continue

clean()