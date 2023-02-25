import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **color):
        self.name = color


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return True



random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
