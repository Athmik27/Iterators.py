class Number: # here we generate an code with help of infinite iterrator.
    def __init__(self):
        self.number=1
    def __iter__(self):
        return self
    def __next__(self):
        number=self.number
        self.number+=1
        return number
num=Number()
for i in num:
    print
