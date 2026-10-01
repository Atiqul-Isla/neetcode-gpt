class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        
        function = init*init
        

        x_new = init
        x_old = x_new

        for i in range(iterations):

            derivative = 2*x_old

            x_new = x_old - learning_rate*derivative

            x_old = x_new
        
        x_new = round(x_new, 5)

        return x_new

