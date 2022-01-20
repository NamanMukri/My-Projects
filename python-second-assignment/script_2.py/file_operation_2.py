def file_process(file_name):
     if 1<=file_name<=10:
       path= f"numbers/{file_name}.txt"
       try:
         f= open(path,'r',encoding = 'utf-8') 

         for line in f:
           print(f"Here are contents for {file_name}.txt: {line}", end = '\n')  
       finally:
         f.close()
     else:
       print("Please select number between 1 and 10")

       
     # Add code to read numbers/<file_name>.txt and print its content


if __name__ == '__main__':
    file_name = int(input("Enter a number between 1 and 10: "))
    file_process(file_name)