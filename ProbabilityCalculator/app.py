import copy
import random

class Hat:
    def __init__(self,**kwargs):  #allows us to get multiple args and keys as a dictionary
        self.kwargs = kwargs
        self.content = list()
        
        for key,value in kwargs.items():
            for i in range(value):
                self.content.append(key)
        
        print (self.content)
        
    def draw(self,draw_number):
        remain_content = list()
        if draw_number > len(self.content):
            return self.content
        for i in range(draw_number):
            removed = self.content.pop(int(random() * len(self.content)))
            remain_content.append(removed)
        return remain_content
    

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_copy = copy.deepcopy(expected_balls)
        colour_balls = copy.deepcopy(num_balls_drawn)
        
        for colour in colour_balls:
            if colour in expected_copy:
                expected_copy[colour]-=1
        if(all(x <= 0 for x in expected_copy.values())):
            count +=1
            
    probability = count / num_experiments
    return probability
