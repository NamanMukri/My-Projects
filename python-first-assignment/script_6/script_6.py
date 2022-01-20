numbers=[1,2,3,4,5]
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
num=['222','100','85','500','300']
len_1=len(numbers)
len_2=len(days)
for i in numbers:
  print(i)

i=0
while i<len_1:
  print(numbers[i])
  i += 1

for i in range(len_2):
  print(days[i])

i=0
while i<len_2:
  print(days[i])
  i += 1
sum=0
for i in range(len(num)):
  sum=sum+int(num[i])
print("The sum from for loop: ", +sum)

i=0
sum=0
while i<len(num):
  sum=sum+int(num[i])
  i += 1
print("The sum from while loop: ", +sum)