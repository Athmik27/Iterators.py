#creating an iterator to generate an number in increasing order.
class Number_Counting:
    # creating an constructor through init
    def __init__(self): #self refers to current object
        self.start=1
        
        #We use __init__() when we want to give initial values to an object when the object is created.
    
    def __iter__(self):
        
        return self
        
    
    def __next__(self):
        if self.start>5:
            raise StopIteration
        number=self.start
        self.start+=1
        return number

num_counting=Number_Counting()
for i in num_counting:
    print(i)

########. or ###########

#creating an iterator to generate an number in increasing order.
class Number_Counting:
    # creating an constructor through init
    def __init__(self): #self refers to current object
        
        pass #We use __init__() when we want to give initial values to an object when the object is created.
    
    def __iter__(self):
        self.start=1
        return self
        
    
    def __next__(self):
        if self.start>5:
            raise StopIteration
        number=self.start
        self.start+=1
        return number

num_counting=Number_Counting()
for i in num_counting:
    print(i)
