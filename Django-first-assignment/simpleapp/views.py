from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#find Square
@csrf_exempt
def find_square1(request):
    if request.method=="GET":
        data=request.GET.get('number')      
        
        try:            
            input=list(request.GET.keys())
            if input!=[]:
                if input[0] == 'number':        
                    return HttpResponse(f"The Square of {data} is {int(data)*int(data)}")
                else:
                    return HttpResponse("Send Parameter in url")
            else:
                return HttpResponse("Send Parameter in url")
        except:
            return HttpResponse("Send Parameter in url")  
    
    elif request.method=="POST":
        
        abc=(request.POST)
        a=list(abc.values())
        if list(abc.keys())[0]=="number":
            return JsonResponse({"data": "Square of Number {} is {}".format(a[0],int(a[0])*int(a[0])) })
        else:
             return HttpResponse("Send Parameter number in data")  
    elif request.method=="PUT":
        url_1=request.path
        return HttpResponse(f"Send Parameter as {url_1}< number >")
    elif request.method=="DELETE":
        url_2=request.path
        return HttpResponse(f"Send Parameter as {url_2}< number >")
    
@csrf_exempt
def find_square2(request,number):
    if request.method=="PUT":
        return JsonResponse({"data": f"Square of Number {number} is {number*number}"})
    if request.method=="DELETE":
        return JsonResponse({"data": f"Square of Number {number} is {number*number}"})

#check Pallindrome
@csrf_exempt
def check_palindrome1(request):
    if request.method=="GET":
        data=request.GET.get('string')
        
        try:
            input=list(request.GET.keys())
            if input!=[]:        
                if input[0] == 'string':
                    if data==data[::-1]:        
                        return HttpResponse(f"<b>{data}</b> is a palindrome ")
                    else:
                        return HttpResponse(f"<b>{data}</b> is not a palindrome ")
                else:
                    return HttpResponse("Send Parameter string in URL to check palindrome")
            else:
                return HttpResponse("Send Parameter string in URL to check palindrome")
        except:
            return HttpResponse("Send Parameter string in URL to check palindrome")  
    
    elif request.method=="POST":
        try:
            a=request.path
            qdict=(request.POST)        
            data=list(qdict.values())        
            if data!=[]: 
                str1=data[0]
                if list(qdict.keys())[0]=="string":
                    if str1==str1[::-1]:        
                        return JsonResponse({"result": f"<b>{str1}</b> is a palindrome "})
                    else:
                        return JsonResponse({"result": f"<b>{str1}</b> is not a palindrome "})            
                else:
                    return HttpResponse("Send Parameter string in data to check palindrome")
            else:                                     
                return HttpResponse("Send Parameter string in data to check palindrome")
        except ValueError:
             return HttpResponse("Send Parameter string in data to check palindrome")

        
    elif request.method=="PUT":
        url_1=request.path
        return HttpResponse(f"Send Parameter as {url_1}< string >")
    elif request.method=="DELETE":
        url_2=request.path
        return HttpResponse(f"Send Parameter as {url_2}< string >")
    
@csrf_exempt
def check_palindrome2(request,string):
    if request.method=="PUT":       
        if string==string[::-1]:        
            return JsonResponse({"result": f"<b>{string}</b> is a palindrome "})
        else:
            return JsonResponse({"result": f"<b>{string}</b> is not a palindrome "})  
    elif request.method=="DELETE":
        if string==string[::-1]:        
            return JsonResponse({"result": f"<b>{string}</b> is a palindrome "})
        else:
            return JsonResponse({"result": f"<b>{string}</b> is not a palindrome "})
#Add array
@csrf_exempt
def add_array(request):
    if request.method=="GET":       
        input=list(request.GET.keys())            
        try:
            if input[0] == 'array':
                new_data=request.GET.get('array').split(",")                 
                add=sum([int(i) for i in new_data])       
                return JsonResponse({"sum":f"{add}"})
            else:
                return HttpResponse("Send Parameter array as comma seperated numbers 2,3,4,5")           
        except:
            return HttpResponse("Send Parameter array as comma seperated numbers 2,3,4,5")  
    
    elif request.method=="POST":        
        qdict=(request.POST)       
        data=list(qdict.values())
        print(data)     
        if data!=[]: 
            num=data[0].split(",")
            if list(qdict.keys())[0]=="array":               
                add1=sum([int(x) for x in num])        
                return JsonResponse({"sum": f"{add1}"})                            
            else:
                return HttpResponse("Send Parameter array in data as comma seperated numbers 2,3,4,5")
        else:                                     
            return HttpResponse("Send Parameter array in data as comma seperated numbers 2,3,4,5")
