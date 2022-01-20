import json
import itertools 
def json_parse(json_string):
     
    #print("Json: ",json_string)
    value=0
    # parse json and calculate 
    
    data=json.loads(json_string)
    N=3
    out = dict(itertools.islice(data.items(), N))
    print("Json: ",out)
    for i in out:
      value=value+int(out[i])
    print("Total Marks:", value )


if __name__ == '__main__':
    # code for reading json file
    # Assign json data  to variable json_string
    f= open('subjects.json',"r")
    json_string = f.read()
    f.close()
    json_parse(json_string)