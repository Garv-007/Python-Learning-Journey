# a={10:100,20:200,30:300,40:400}

# print(a[10])   # Accesing dict values using keys

# a[50]=500   # creating the new value in dictionary
# print(a)


# a[10]=1000
# print(a)       #Updating the key values which is already existing




#METHODS: 
# b={10:100,20:200,30:300,40:400}

# # b.clear()  # remove all values

# c=b.fromkeys([10,20],50)
# print(c)            # changes will be in new dictiory not in orignal ones

# print(b.get(10))  # get values using keys

# print(b.items()) # give all key values in tuple form

# print(b.keys())  # give all keeys in list form
# print(b.values()) # give all values in list form 

# print(b.pop(40))  # remove a specified key
# print(b)

# # print(b.popitem())   #remove last value from dict

# b.update({10:1000})
# print(b)         # updating any values of key also u can create new key:value




# Traversing loops
 
# b={10:100,20:200,30:300,40:400}

# for i in b:
#     print (f"key {i}: values {b[i]}")
          










#QUESTIONS:
# Q1: Merge two dictionaries into one.
# d1 ={"a":10,"b":20,"c":30}
# d2 ={"d":40,"e":50,"f":60}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)


# Q2: Sum all values in a dictionary.
# d1 ={"a":10,"b":20,"c":30}
# sum=0
# for i in d1:
#     sum=sum +d1[i]
# print(sum)


# Q3:Count the frequency of each element in a list using a dictionary.
# c=["a","b","a","c","b","a"]
# d={}
# for i in c:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


# Q4: Combine two dicts, adding values for common keys
d1 ={"a":10,"b":20,"c":30}
d2 ={"d":40,"e":50,"f":60}

for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)