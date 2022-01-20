import os
try:
  f= open("sample.txt",'r',encoding = 'utf-8') 
#perform file operations
  for line in f:
    print(line, end = '\n')  
finally:
  f.close()
