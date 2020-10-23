class Hat:
    # Input a variable amount of colors with kwargs:
    def __init__(self, **kwargs):
        contents = []
        for key, value in kwargs.items():
            # Repeat the colour string the number of times of its value:
            contents.extend(repeat(key,value))
        self.contents = contents
    
    def draw(self,number):
        balls_drawn = []
        # In case of selecting all (or more) balls than existing, show
        # all the balls in the hat
        if len(self.contents) <= number:
            return self.contents
        # Each time a ball is extracted from the hat, it selects a random ball,
        # add it to the group of balls drawn and removed from the group of
        # the balls in the hat:
        for i in range(number):
            extracted = random.choice(self.contents)
            balls_drawn.append(extracted)
            self.contents.pop(self.contents.index(extracted))
        return(balls_drawn)
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):  
    # Add a counter to check number of "successful" experiments:
    counter = 0
    # Do a number of experiments:
    for i in range(num_experiments):
        # Do a deep copy of the hat input in its class:
        copyhat = copy.deepcopy(hat)
        # Draw a number of balls selected in the input:
        hat_drawn = copyhat.draw(num_balls_drawn)
        # Create a variable to know later if a concret experiment was "successful":
        true = True
        # Check if there is at least a number of expected balls.
        # To do so check if the number of strings in hat.contents of an expected
        # color  is lesser than the number input in the expected_balls dictionary
        for key in expected_balls.keys():
            if hat_drawn.count(key) < expected_balls[key]:
                # In case the expectation is not met, the experiment is not "successful"
                true = False
                break
        # If the previous loop didn't break, it means that the experiment is "successful"
        if true == True:
            # In that case, a sucessful experiment is added to the counter:
            counter += 1
    # The probability is calculated with the number of succesful experiments and the
    # total of experiments done:
    probability = counter/num_experiments
    return probability
