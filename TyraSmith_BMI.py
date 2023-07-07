def bmi():
    input("Welcome to the body mass index calculator. Click enter to begin.: ")
    while True:
        try:
            while True: 
                ques1=(input("Would you like to use imperial or metric units?: "))
                if ques1.lower() == "imperial" or ques1.lower() == "i":
                    height = float(input("What is your height in inches?: "))
                    weight = float(input("What is your weight in pounds?: "))
                    bmi = (weight / (height ** 2) * 703)
                    answer = round(bmi, 1)
                    print("Your body mass index is",answer )
                elif ques1.lower() == "metric" or ques1.lower() == "m":
                    height = float(input("What is your height in centimeters?: "))
                    weight = float(input("What is your weight in kilometers?: "))
                    height2 = height / 100
                    bmi = (weight / (height2 ** 2))
                    answer = round(bmi, 1)
                    print("Your body mass index is",answer )
                else: 
                    input("Please choose between imperial and metric. ")
                    continue
                
                output = ["underweight", "healthy","overweight", "obese"]
                if answer < 18.5:
                    print("Your BMI is", output[0])
                elif answer > 18.5 and answer < 24.8:
                    print("Your BMI is", output[1])
                elif answer > 25 and answer < 29.9:
                    print("Your BMI is", output[2])
                else:
                    print("Your BMI is unhealthy")
                    
            ques1 = int(ques1)
                
        except ValueError: 
                print("Stop trying to break my code. Please input a number.")
                continue
                
        
        
bmi()

