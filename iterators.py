#creating an iterator to generate an number in decreasing order.
class Number_Countdown:
    # creating an constructor through init
    def __init__(self,start): #self refers to current object
        self.start=start
    # creates an iterator through iter
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<=0:
            raise StopIteration
        number=self.start
        self.start-=1
        return number

num_countdown=Number_Countdown(5)# Create an iterator object of the Number_Countdown class and give 5 to its constructor.
for i in num_countdown:
    print(i)



