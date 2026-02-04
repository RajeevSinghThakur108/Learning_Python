# lists properties
#  mutable
#  ordered 
#  duplicate 
#  multiple type of data (Heterogeneous)
#  Dynamic Size

lst = ["water" , "air" , "soil"]

# print(lst[0])


# lst.append("roak")
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])
# print(lst)


# a=[]
# b=[1,2,3]
# c=["rajeev", "singh" , 26]
# d=["a" , "b" , 2 , True]


# d.append(c)
# d.extend(b)

# # print(d)

# for i , v in enumerate(d):
#     print(v)


# nums = [1,2,3]
# nums.append([4, 5])
# nums.extend([6,7])
# print(nums)

# data = ["apple", 10, "banana", 5, 3.5, "cherry"]
# check = True
# for i in data:
#     if(type(i) == str):
#        print(i)


# for i in data:
#     if isinstance(i,str):
#         print(i)


# tasks = ["wake up", "exercise", "study"]

# tasks.append("breakfast")
# tasks.remove("exercise")
# # tasks[len(tasks)-1] = "study python"
# tasks[tasks.index("study")] =  "study python"

# print(tasks) 


# cart = ["apple", "banana", "milk", "bread"]

# cart.insert(2, "eggs")
# cart.pop()
# cart[cart.index("banana")] = "orange"

# print(cart)

# marks = [45, 78, 88, 32, 90]
# for i in marks:
#     if i <= 40:
#         marks.remove(i)
# marks = [i for i in marks if i<40]

# marks.extend([75,85])
# marks.sort(reverse=True)
# print(marks)



# marks = [45, 78, 88, 32, 90]

# marks = [i for i in marks if i >= 40]

# marks.extend([75, 85])
# marks.sort(reverse=True)

# print(marks)




# employees = [
#     ["Raj", 28],
#     ["Anita", 35],
#     ["John", 24],
#     ["Meena", 30]
# ]

# employees = [emp for emp in employees if emp[1] >= 30]

# print(employees)


# nums = [10, 20, 30, 40, 50]

# new = [i for i in nums if i>25]
# print(new)

# nums = [1, 2, 3, 4, 5]
# new=[]
# for i in nums:
#     new.append(i*i)
# print(new)

nums = [1, 11, 3, 4, 5, 6, 7]

# for i in nums:
#     if i % 2 != 0:
#         nums.remove(i)
# print(nums)

# nums = [1, 2, 3, 4, 5, 6, 7]
# nums=[i for i in nums if i % 2 == 0]
# print(nums)


# data = [10, "a", 20, "b", 30, "c"]
# l1 = [i for i in data if isinstance(i, str)]
# l2 = [i for i in data if isinstance(i, int)]
# print(l1)
# print(l2)


# data = [10, "a", 20, "b", 30, "c"]

# l1=[]
# l2=[]
# for i in data:
#     if isinstance(i, str):
#         l1.append(i)
#     else:
#         l2.append(i)

# print(l1)
# print(l2)

# nums = [1, 2, 2, 3, 4, 4, 5, 1]
# r=[]
# for i in nums:
#     if i  not in r:
#         r.append(i)

# print(r)


# nums = [1, 2, 3, 4, 5]

# r=[]
# for i in range(len(nums)-1 , -1 ,-1):
#     r.append(nums[i])
# print(r)


nums = [1, 2, 3, 4, 5] # [5, 1, 2, 3, 4]

# p = 1
# r=[]
# n=len(nums)

# for i in range(0, n-p,1):
#     r.append(nums[i])
# r.insert(0,nums[n-p])

# print(r)
p=1
n=len(nums)
e=nums.remove(n)
nums.insert(0,e)
print(nums)








        
   

