


def multiple_print(func):
  def func_wrapper(text,count):
	  for i in range(count): func(text,count)
      
  return func_wrapper


def text_statement(text,count):
  print(text)
    
    
if __name__ == '__main__':
  text = input("What do you want to print?")
  count = int(input("How many times do you want to print the statement?"))

  text_statement1 = multiple_print(text_statement)
  text_statement1(text, count)





