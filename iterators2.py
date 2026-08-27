#generate an iterator to get a power of 2.
class My_Number:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        if self.num>self.max:
            raise StopIteration
        else:
            result=2**self.num
            self.num+=1
            return result
my_num=My_Number(5)
for i in my_num:
    print(i)
#both gives same output but with different range
class Square_Number:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            value=2 ** self.num 
            self.num+=1
            return value
        else:
            raise StopIteration
sq_num = Square_Number()
for i in sq_num:
    print(i)
