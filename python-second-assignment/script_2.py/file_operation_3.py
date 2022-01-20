import os
def write_to_file(file_name, file_contents):
  try:
    f= open(f"{file_name}.txt",'w+',encoding = 'utf-8') 
    f.write(file_contents)
    print(f"A file named {file_name}.txt is created with “{file_contents}” as its contents")

      
  finally:
    f.close()
    
     # Add code to save data in variable file_contents to file named file_name

if __name__ == '__main__':
    file_name = input("Enter the name of file: ")
    file_contents = input("Enter the contents to be stored in a file: ")
    write_to_file(file_name, file_contents)