print("Hello World")
print("I am your new calculator")
print("Ask me out")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. POWER")

operation = input()

if operation == "1":
    num1 = input ("First number: ")
    num2 = input ("Second number: ")
    print("Your answer is " + str(int(num1) + int(num2)))
    #code for addition
elif operation == "2": 
    num1 = input ("First number: ")
    num2 = input ("Second number: ")
    print("Your answer is " + str(int(num1) - int(num2)))
    #code for subtraction
elif operation == "3" :
    num1 = input ("First number: ")
    num2 = input ("Second number: ")
    print("Your answer is " + str(int(num1) * int(num2)))
    #code for multiplication 
elif operation == "4":
    num1 = input ("First number: ")
    num2 = input ("Second number: ")
    print("Your answer is " + str(int(num1) / int(num2)))
    #code for division 
elif operation == "5":
    num1 = input ("First number: ")

    print("Your answer is " + str(int(num1) ** int(2)))
    #code for exponential
else: 
    print("Oh Oh! Invalid Entry")
    