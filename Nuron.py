import math
import random
class Nuron:
    def __init__(self, number_of_inputs,inputs):
        self.number_of_inputs = number_of_inputs
        self.weights = []
        self.inputs = inputs
        self.bias = random.uniform(-5, 5) 
        for i in range(number_of_inputs):
            self.weights.append(random.uniform(-10, 10) )
        
    def Z(self):
        z = 0
        for i in range(self.number_of_inputs):
            z += self.weights[i] * self.inputs[i]
        z += self.bias
        return z
    
    def sigmoid(self):
        return 1 / (1 + math.exp(-self.Z()))
    
    def differentiationOfSigmoid(self):
        return self.sigmoid() * (1 - self.sigmoid())
    
    def differentiationOfZ(self,target): # w1674368   x468287  y4893804
        index = target[1:]
        if target.toLower().contains("w"):
            return self.inputs[index]
        elif target.toLower().contains("y") or target.toLower().contains("x") :
            return self.weights[index]

    # Z = w1*x1 + w2*x2 + w3*x3 + b




    # Z = w1*y1 + w2*y2 + w3*y3 + b