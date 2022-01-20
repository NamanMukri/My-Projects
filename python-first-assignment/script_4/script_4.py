def bmi_script_4(age,height,weight):
    
    return round(weight/(height*height),1)

if __name__ == '__main__':
     age= int(input("Hi Argo, What is your Age?"))
     height = float(input("What is your Height in metres?"))
     weight = int(input("What is your Weight in Kg?"))
     res= bmi_script_4(age,height, weight)
     print(f"The BMI is {res}")