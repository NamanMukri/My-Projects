import sys

print(type(sys.argv))
name= sys.argv[1]
height= float(sys.argv[2])
weight= int(sys.argv[3])
print("Name: ", name)
print("Height: ", height)
print("Weight: ", weight) 
def bmi_script_5(height, weight):
     return round(weight/(height*height),1)

res=bmi_script_5(height, weight)

if res<18.5:
  print(f"Your BMI is {res} which means you are Underweight")
elif 18.5<=res<25:
  print(f"Your BMI is {res} which means you are Normal")
elif 25<=res<30:
  print(f"Your BMI is {res} which means you are Overweight")
else:
  print(f"Your BMI is {res} which means you are Obese")