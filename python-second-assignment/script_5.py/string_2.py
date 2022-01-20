def append_ing(sentence):
  last_char=sentence[-3:]
 
  output=""
  if last_char=="ing":
    output=sentence+"ly"
    print("Output: ",output)
  else:
    output=sentence+"ing"
    print("Output: ",output)
  


if __name__ == '__main__':
    sentence = input("Enter a string:")
    append_ing(sentence)