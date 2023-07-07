from math import sqrt
def calculator():
    reply1 = input("Would you like to perform a calculation? " )
    def calculation():
        def operations():
                print("1. Add")
                print("2. Subtract")
                print("3. Multiply")
                print("4. Divide")
                print("5. Exponent")
                print("6. Square Root")

            
        if(reply1) == "yes":
            print("Choose an operation:")
            operations()
            print("Type the number of the operation you wish to perform: ")
            reply2 = input()
            if(reply2) == "1":
                x = input("Type your first number: ")
                y = input("Type your second number: ")
                sum = int(x) + int(y)
                print("The sum is:", sum)
            elif(reply2) == "2":
                x = input("Type your first number: ")
                y = input("Type your second number: ")
                difference = int(x) - int(y)
                print("The difference is:", difference)
            elif(reply2) == "3":
                x = input("Type your first number: ")
                y = input("Type your second number: ")
                product = int(x) * int(y)
                print("The product is:", product)
            elif(reply2) == "4":
                x = input("Type your first number: ")
                y = input("Type your second number: ")
                quotient = int(x) / int(y)
                if x == 0 or y == 0:
                    print("0")
                else:
                    print("The quotient is:", quotient)
            elif(reply2) == "5":
                x = input("Type your base number: ")
                y = input("Type your power number: ")
                answer = int(x) ** int(y)
                print("The answer is:", answer)
            elif(reply2) == "6":
                x = input("Type your number: ")
                answer = sqrt(int(x))
                print("The square root of", x, "is:", answer)
            else:
                print("That's all I offer. Log off.")
        else:
            print("That's all I offer. Log off.")
            
        reply3 = input("Would you like to perform another calculation? ")
        if(reply3) == "yes":
            calculation()
        else:
            print("Toodles!")
        
            
    calculation()
    
        
    
            
calculator()
