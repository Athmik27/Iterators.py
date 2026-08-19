# generate an code for getting square of an number using generators 
def number_square(number):
    for i in range(number):
        yield i*i
num_square=number_square(5)
for i in num_square:
    print(i)


# by using generator expression
number_square=(i*i for i in range(1,6))
print (list(number_square))

#generate an code for reversing an string using generators 
def reverse_string():
    text="John Doe"
    for i in text[::-1]:
        yield i
for letter in reverse_string():
    print(letter)

# same code without using slicing
def reverse_string():#without passing any argument
    text="John Doe"
    for char in range(len(text)-1,-1,-1):
        yield text[char]
for letter in reverse_string():
    print(letter)


# same code without using slicing
def reverse_string(text):#with passing any argument
    
    for char in range(len(text)-1,-1,-1):
        yield text[char]
for letter in reverse_string("John Doe"):
    print(letter)


# generate an square without using the argument in the function
def number_square():
    number=5
    for i in range(number):
        yield i*i
num_square=number_square()
for i in num_square:
    print(i)   
