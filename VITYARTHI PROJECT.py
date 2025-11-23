ht = float(input("Enter your height in inches "))
wt = float(input("Enter your weight in lbs "))

def BMI(ht,wt):
    bmi = (wt/(ht**2))*703
    if(bmi < 16):
        return "severly underweight" , bmi
    elif(bmi>=16 and bmi<18.5):
        return "underweight", bmi
    elif(bmi>=18.5 and bmi<25):
        return "healthy" , bmi
    elif(bmi>=25 and bmi<30):
        return "overweight" , bmi
    elif(bmi>=30):
        return "obese" , bmi

quote , bmi = BMI(ht,wt)
print("Your bmi is : {} and you are : {}".format(bmi,quote))
