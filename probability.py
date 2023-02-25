import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **color):
        self.contents = []
        for (color,amount) in color.items():
            for count in range(amount):
                self.contents.append(color)
    def __str__(self):
        return str(self.contents)
        
    def draw(self, numberOfBalls):
        if len(self.contents) < numberOfBalls:
            return self.contents
        removed_balls =[]
        for theBall in range(numberOfBalls):
            indexNumber = random.randrange(len(self.contents))
            removed_balls.append(self.contents[indexNumber])
            self.contents.pop(indexNumber)
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successCount = 0
    for experiment_number in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        drawnBall = hatCopy.draw(num_balls_drawn)
        if does_dictContain(make_dict(drawnBall), expected_balls):
            successCount += 1
    return successCount/(num_experiments +1)

def does_dictContain(dictActual, dictExpected):
    for color, amount in dictExpected.items():
        try:
            try:
                dictActual[color]
            except:
                return False
            difference = dictActual[color] - amount
            if difference<0:
                return False
        except:
            continue
    return True

def make_dict(list):
    dictionary = {}
    for color in list:
        try:
            dictionary[color] += 1
        except:
            dictionary[color] = 1
    return dictionary

hat = Hat(blue=3,red=2,green=6)

probability = experiment(
    hat=hat, 
    expected_balls={"blue":2,"green":1}, 
    num_balls_drawn=4, 
    num_experiments=1000)

print(probability)