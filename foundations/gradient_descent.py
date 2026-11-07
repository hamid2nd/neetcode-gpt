class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        #this is a convex objective function, so minimum is when gradient = 0, so we will iterate until gradient =0 
        x = init 
        for i in range(iterations):
            derivative = 2*x
            update = -(learning_rate * derivative)
            x = x + update
        x = round(x,5)
        return x 
