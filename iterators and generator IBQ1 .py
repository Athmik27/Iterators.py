#Create a custom iterator that generates numbers from 1 to 10.
class Number:
    def __init__(self):
        self.num=1
        #pass
    def __iter__(self):
        #self.num=1
        return self
    def __next__(self):
        #in __next__ never put for loop
            if self.num<=10:
                value=self.num
                self.num+=1
                return value
            else:
                raise StopIteration
num=Number()
for i in num:
    print(i)
        
# # # generate an even number from 2 to 20
class Even_Number:
    def __init__(self):
        self.num=2
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            value=self.num
            self.num+=2
            return value
        else:
            raise StopIteration
evn_num=Even_Number()
for i in evn_num:
    print(i)

#odd num from 1 to 19
class Odd_Number:
    def __init__(self):
        pass
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=19:
            value=self.num
            self.num+=2
            return value
        else:
            raise StopIteration
odd_num=Odd_Number()
for i in odd_num:
    print(i)

# #Create a custom iterator that generates numbers from 10 down to 1.
class Number:
    def __init__(self):
        pass
    def __iter__(self):
        self.num=10
        return self
    def __next__(self):
        if self.num>=1:
            value=self.num
            self.num-=1
            return value
        else:
            raise StopIteration

num=Number()
for i in num:
    print(i)

#     #Create a custom iterator that generates the squares of numbers from 1 to    10 
class Square_Number:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            value=self.num ** 2 # value=2 ** self.num gives you power of 2
            self.num+=1
            return value
        else:
            raise StopIteration
sq_num = Square_Number()
for i in sq_num:
    print(i)

# #fibonacci series (imp )
def Fibonacci_Series(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input("enter the value:"))
for i in Fibonacci_Series(n):
    print(i)

