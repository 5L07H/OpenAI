import math
import numpy
global rewards
rewards = []
def assignreward(var):
  global rewards
  if var is float or int:
    rewards.append(var)
   else:
    raise "inproper type for assignreward()"
    
  
