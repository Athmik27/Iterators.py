#code to generate even numbers using iterator
class Even_Number(): # class Even Number: is also correct if we want to inherit then we use class Even Number():
    def __init__(self,max):
        self.number=2
        self.max=max
    def __iter__(self):
            
            return self
    def __next__(self):
            if (self.number>self.max):
                raise StopIteration
            else:
                number=self.number
                self.number+=2
                return number
evn_num=Even_Number(10)
for i in evn_num:
    print(i)

#generate an fibonacci series using iterator
def Fibonacci_Series(n):
     a=0
     b=1
     for i in range(n):
        yield a
        a,b = b,a+b
          
n=int(input("Enter the number of terms in the Fibonacci series: "))
for number in Fibonacci_Series(n):
    print(number)
