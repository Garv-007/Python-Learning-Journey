# a=[12,23,45,66,67,54,99]

# print(a)



# fruits = ["apple", "banana", "mango"]

# print(fruits[0])    # apple
# print(fruits[-1])   # mango
# print(fruits[0:2])  # ['apple', 'banana']

# fruits[1] = "grape"  # mutation — lists allow this!



#Traversing on List:
a=[10,20,30,40,50]

#ON VALUES:

# for i in a:
#     print(i)

#ON INDEX:

# for i in range(0,len(a)):
#     print(a[i])


# Methods:--

lst = [3, 1, 4, 1, 5]

# dir(list)
# lst.append("help")  #Add at the end 

# lst.insert(0,99)    #Add value in list at given index

# lst.pop()  # dlt last  value default but u can give index to pop

# lst.remove(5)   # dlt any value from list

# lst.clear()  # Remove all elements from list

# lst.sort()  #sort default in ascending
# lst.sort(reverse=True)

# lst.reverse()  #reverse the elemnts of list
# len(lst)  # return the total elem in list








#QUESTIONS:

# Q1: Print all positive and negative elements separately.

# ls= [3, -1, 4, -5, 9]
# pos=[]
# neg=[]

# for i in ls:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"positive: {pos} negitive: {neg}")
    

# Q2: Find the mean (average) of all list elements.
# MEan- sum of all value/ total values

# ps= [10,20,30,40]
# sum =0 
# for i in ps:
#     sum=sum+i

# print(f"{sum/len(ps)}")


# Q3: Find the greatest element and print its index.

# gs= [4, 8, 2, 9, 1]
# large=gs[0]
# index=0 

# for i in range(len(gs)):
#     if a[i]>large:
#         large=a[i]
#         index=i

# print(large)


# Q4: Find the second greatest element.

# ts=[1,7,2,9,1,8]
# lar=ts[0]
# sec_large=ts[0]

# for i in ts:
#     if i>lar:
#         sec_large=lar
#         lar=i
#     elif i>sec_large:
#         sec_large=i
# print(sec_large)



# Q5: Check if the list is already sorted.

js=[10,20,30,40,50,60]

for i in range(len(js)-1):
    if js[i] >js[i+1]:
        print("your list is not sorted")
        break
else:
    print("sorted list")