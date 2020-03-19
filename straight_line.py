# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro')
# plt.ylabel('Y-axis')
# plt.xlabel('X-axis')
# plt.show()

# ? To make a program to accept two co-ordinates and then give
# !1.gradient
# !2.Y-intercept
# !3.Equation
# !4.midpoint
# !5.parallel line's equation
# !6.perpendicular lines


class Line:

    def __init__(self, one, two):
        self.co1 = one
        self.co2 = two

    # *Finding gradient

    def grad(self):
        x = self.co1[0] - self.co2[0]
        y = self.co1[1] - self.co2[1]
        if y == 0:
            self.grad = 0
        else:
            self.grad = int(x/y)
        return f'the gradient of the line is {self.grad}'

    # * Finding Y-intercept
    def y_intercept(self):
        g = self.grad * self.co1[0]
        self.y_intercept = self.co1[1]-g
        return f'the Y intercept of the line is {self.y_intercept}'

    # * State the Equation
    def equ(self):
        return f'The equation of the line is y = {self.grad}x + {self.y_intercept}'

    # * find midpoint of line
    def mid(self):
        x = self.co1[0] + self.co2[0]
        y = self.co1[1] + self.co2[1]
        self.mid = [x/2, y/2]
        return f'the mid-point of the line is {self.mid}'

    # * parallel line equation

    def parallel_line(self, co3):
        self.co1 = co3
        g = self.grad * self.co1[0]
        self.y_intercept = self.co1[1]-g
        return f'The equation of the parallel line that passes through the co-ordinates {self.co1} is y = {self.grad}x + {self.y_intercept}'

    # * perpendicular line equation

    def perpen_line(self, co3):
        self.co1 = co3
        if self.grad == 0:
            self.grad = 0
            g = self.grad * self.co1[0]
            self.y_intercept = int(self.co1[1]-g)
            return f'The equation of the perpendicular line that passes through the co-ordinates {self.co1} is y = 0 + {self.y_intercept}'
        else:

            self.grad = int(-1/self.grad)
            g = self.grad * self.co1[0]
            self.y_intercept = int(self.co1[1]-g)
            return f'The equation of the perpendicular line that passes through the co-ordinates {self.co1} is y = {self.grad}x + {self.y_intercept}'


trial = Line([8, 9], [9, 8])
print(trial.grad())
print(trial.y_intercept())
print(trial.equ())
print(trial.mid())
print('Please pass in a value at the bottom of the code, else pre-stored value will run in place')
print(trial.parallel_line([4, 5]))
print('pass co-ordinates for perpendicular line\'s points')
print(trial.perpen_line([7, 8]))
