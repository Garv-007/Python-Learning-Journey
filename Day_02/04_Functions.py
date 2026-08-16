#Earlier we are doing primitive approach now we are using functional approach later we use object oriented approach

def hello():
    print("Hello how are you?")
hello()

# Function with parameters and arguments
def add(a,b):
    print(a+b)
add(10,20)



# 1. Positional — order matters
def add(a, b):
    return a + b
add(5, 3)       # → 8

# 2. Default — works even without passing a value
def greet(name="Guest"):
    print(f"Hello {name}")
greet()            # Hello Guest
greet("Akarsh")  # Hello Akarsh

# 3. Keyword — pass in any order
def info(name, age):
    print(f"{name} is {age}")
info(age=25, name="Akarsh")  # order doesn't matter
