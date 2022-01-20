def process_string(sentence):
     capitalize = sentence.upper()
     lower=sentence.lower()
     cap_first=sentence.capitalize()
     replace1=sentence.replace("d","h")
     replace2=sentence.replace("o","zm")
     occurence=sentence.count("a")
     length=len(sentence)-sentence.count(" ")
     print(f"Capitalize: {capitalize} \nLower: {lower} \nCapitalize first letter:{cap_first} \nReplace all d by h: {replace1} \nReplace all o by zm: {replace2} \nFind no, of times a occurred: {occurence} \nCount no. of letters string has: {length}" )


if __name__ == '__main__':
    sentence = input("Enter a long sentence:")
    process_string(sentence)