# ASSIGNMENT: The below is a common design pattern that can be cleaned up.
# We have a lengthy mathematical operation that uses a few pieces of
# information several times in order to mutate a value. This code organization
# isn't inherently wrong, but it does result in some pretty messy callsites,
# especially once we introduce nested function calls in compound_op_it().
# 
# The goal of this assignment is to refactor the below into a class: 
# 1) Shared arguments between functions should become instance variables of the class
# in order to minimize clutter (because now they won't have to be arguments
# to each function). 
# 2) The class should have a function self.complicated_math_operation()
# that accomplishes everything complicated_math_operation() currently does.
# 3) There's a design decision lurking in here! Should we make the starting_value
# an instance variable of the class that each function call mutates, or should we
# keep the current structure where complicated_math_operation() accepts a starting value
# and repeatedly mutates it? Leave a comment explaining which one you chose
# and under what circumstances that might make sense. There's no right answer! 

import math

class homework_4:

    def __init__(self,starting_value, min_value, max_value, coefficient):
        self.starting_value = starting_value
        self.min_value = min_value
        self.max_value = max_value
        self.coefficient = coefficient


    def complicated_math_operation(self):
        res = self.starting_value
        res = self.multiply_it()
        res = self.add_it()
        res = self.sqrt_it()
        res = self.compound_op_it()
        return res

    def multiply_it(self):
        return max(self.min_value, min(self.max_value, self.starting_value * self.coefficient))

    def add_it(self):
        return max(self.min_value, min(self.max_value, self.starting_value + self.coefficient))
    
    def sqrt_it(self):
        return max(self.min_value, min(self.max_value, math.pow(self.starting_value, -self.coefficient)))

    def compound_op_it(self):
        return self.add_it(
            self.multiply_it(self.starting_value, self.min_value, self.max_value, self.coefficient),
            self.min_value,
            self.max_value,
            self.coefficient
        )

