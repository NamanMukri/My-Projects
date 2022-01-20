def bmi_script_5(height, weight):
     return round(weight/(height*height),1)

if __name__ == '__main__':
     name = input("What is your Name:")
     height = float(input("Hi "+name +", What is your Height in metres?"))
     weight = int(input("What is your Weight in Kg?"))
     res=bmi_script_5(height, weight)
if res<18.5:
  print(f"Your BMI is {res} which means you are Underweight")
elif 18.5<=res<25:
  print(f"Your BMI is {res} which means you are Normal")
elif 25<=res<30:
  print(f"Your BMI is {res} which means you are Overweight")
else:
  print(f"Your BMI is {res} which means you are Obese")