import os
import time
import sys


def clean():
    if sys.platform == "linux" or "mac" in sys.platfrom:
        os.system("clear")
    elif "win" in sys.platform:
        os.system("cls")


while True:
    clean()
    print("================ welcome to my simple calculator ================")
    print("by : Hasban Fardani\n\n")
    operation = input("please select the operation (+, -, x, :, %) or q for quit: ", )
    if operation == "q":
        clean()
        print("thank you for using this calculator")
        break
    elif operation not in ["+", "-", "x", ":", "%"]:
        print("operation not found, please enter the correct operation")
        time.sleep(2)
        clean()
        continue
    else:
        num1 = int(input("enter a number      : ", ))
        num2 = int(input("enter second number : ", ))
        if operation == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == "x":
            print(f"{num1} x {num2} = {num1 * num2}")
        elif operation == ":":
            print(f"{num1} : {num2} = {num1 / num2}")
        elif operation == "%":
            print(f"{num1} % {num2} = {num1 % num2}")

        while True:
            cont = input("\ncontinue (y/n)? ", )
            if cont == "n" or cont == "N":
                clean()
                break
            elif cont == "y" or cont == "Y":
                clean()
                break
            else:
                continue

        if cont == "n" or cont == "N":
            clean()
            print("thank you for using this calculator")
            break
