# import requests
# import json
# x=requests.get("https://api.merakilearn.org/courses")
# re=x.json()
# print(re)
# with open("cour.json","w") as f:
#     d=json.dump(re,f,indent=4)
# # print(d)
# s=open("cour.json","r")
# n=s.read()
# da=json.loads(n)
# # print(da)
# i=0
# while i<len(da):
#     print(str(i+1),da[i]["name"],da[i]["id"])
#     i+=1
# input=int(input("Enter the Number :"))
# print(da[input-1]["name"])
# add=da[input-1]["id"]
# x1=requests.get("https://api.merakilearn.org/courses/"+str(add)+"/exercises")
# re1=x1.json()
# with open("details.json","w") as h:
#     det=json.dump(re1,h,indent=4)
# print(det)
# s1=open("details.json","r") 
# n1=s1.read()
# da1=json.loads(n1)
# i=0
# while i<len(da1["course"]["exercises"]):
#     print(str(i+1),da1["course"]["exercises"][i]["name"])
#     i+=1
# user=int(input("enter the topic"))    
# list2=[] 
# # list3=[] 
# j=0
# k=1
# for j in re1["course"]["exercises"]:
#     if j["parent_exercise_id"]==None:
#         # j=j+1
#         list2.append(j)
#         print(i," ",j["name"])
#         list2.append(j)     



# def calculate (num1, num2=4):
#     res = num1 * num2
#     print(res)

# calculate(5, 6)

# str = "pynative"
# print (str[1:3])


# var= "James Bond"
# print(var[2::-1])



# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)


# var = "James" * 2  * 3
# print(var)


# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)


# a=30
# b=9
# print(a*b)

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# a=5
# b=2
# print(a**b)



# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
# print(listOne == listTwo)
# print(listOne is listTwo)

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)





# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )


# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# for x in range(0.5, 5.5, 0.5):
#       print(x)

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))




# print(type({}) is set)



# x = 75
# def myfunc():
#     x = x + 1
#     print(x)

# myfunc()
# print(x)


# print(type(0xFF))


# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)

# def func1():
#     x = 50
#     return x
# func1()
# print(x)


# print(type({}) is set)
# print(type([])is list)



# x = 10
# y = 50
# if x ** 2 > 100 and y < 100:
#     print(x, y)


# print(33 == 33.0)



# num=3
# while True:
#    if (num%0o12 == 0):
#       break
# print(num)
# num += 1



# What is web scraping?
# What is a beautiful soup?
# What is an HTML parser?
# Read about pip,pprint, and package.
# What is find and find all?



