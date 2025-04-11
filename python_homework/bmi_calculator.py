def bmi_calculator(weight,height):
    BMI = round(weight / ((height/100)**2),1)
    return BMI
print(bmi_calculator(70,175))