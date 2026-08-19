# generate an infinite iterator for infinite numbers.
class Number:
    def __init__(self):
        self.number=1
    def __iter__(self):
        return self
    def __next__(self): # if we need to generate an finite number we must use if with else condition.
        number=self.number
        self.number+=1
        return number
num=Number()
for i in num:
    print(i)