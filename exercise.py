import json
import requests
url=requests.get('https://api.merakilearn.org/courses')
re=url.json()
with open("courses.json","w")as file:
    json.dump(re,file,indent=4)
r=open("courses.json","r")
read=r.read()
data=json.loads(read)
print()
print("welcome to navgurukul and learn basic programming language")
print()

k=1
for i in data:
    print(k,".",i["name"],i["id"])
    k+=1
    
user=int(input("enter the program number:"))
print(data[user-1]["name"],data[user-1]["id"])
print()
file1=data[user-1]["name"]+"_ "+data[user-1]["id"]+".json" 
link2=requests.get("http://api.merakilearn.org/courses/"+data[user-1]["id"]+"/exercises").json()
with open(file1,"w") as f:
    json.dump(link2,f,indent=4)

ret= open(file1,"r").read()
deta = json.loads(ret)

main_list=[]
b=1
b1=1
for i in deta["course"]["exercises"]:
    print(b,i["name"])
    print("  ",i["slug"])
    b+=1
    main_list.append(i)
    
with open("main_file.json","w") as write:
    json.dump(main_list,write,indent=4) 
    
topic=int(input("enter the topic"))
topic=topic-1
i=0
while i<len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"]) 
    print()
    i+=1
while topic <= len(deta["course"]["exercises"]):
    next_previuos = input("previous or next(p&n):")
    if  next_previuos == "p" and next_previuos!= "n":
        topic-=1
        if next_previuos == "p" and topic >1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else :
            i = 0
            while i < len(deta):
                print(str(i+1),deta["course"]["exercises"][i]["name"])
                i+=1                
    elif  next_previuos == "n" and next_previuos!="p":
        topic+=1
        if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
                print(deta["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(deta["course"]["exercises"][topic]["content"]):
                    print(deta["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(deta["course"]["exercises"]):
            print("topic is completed.")
            break
    else:
        print("wrong user_input ")
        break

          
     
        
    




