import os
import time
import sys


def clean():
    if sys.platform == "linux":
        os.system("clear")
    elif "win" in sys.platform:
        os.system("cls")


while True:
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
            lanjut = input("\nlanjut (y/n)? ", )
            if lanjut == "n" or lanjut == "N":
                clean()
                break
            elif lanjut == "y" or lanjut == "Y":
                clean()
                continue

        if lanjut == "n" or lanjut == "N":
            clean()
            print("thank you for using this calculator")
            break
