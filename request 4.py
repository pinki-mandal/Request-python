import requests
import json
url=requests.get("https://api.merakilearn.org/courses")
data=url.json()
print(data)
b=open("new.json","w")
c=json.dump(data,b,indent=4)
serial_no=0
for i in range(0,len(data)):
    print(serial_no+1,".",data[i]["name"],"id:",data[i]["id"])
    serial_no+=1
print()    
course_name=int(input("enter the course name which is learn from"))
print(data[course_name-1]["name"])
print(course_name)
url2=requests.get("https://api.merakilearn.org/courses"+str(data[course_name-1]["id"])+'/exercise')
data1=url2.json()
print(data1)
b=open("new1.json","w")
c=json.dump(data1,b,indent=4) 
   
    