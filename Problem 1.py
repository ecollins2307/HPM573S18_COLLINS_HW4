# HW 4, Problem 1

# load NumPy, requires Anaconda to be installed locally and chosen as the interpreter
import numpy as numpy

# create Game class
class Game(object):
    def __init__(self, flip_probability):
        self.flip_probability = flip_probability #probability of heads

    # create Simulate function
    def Simulate(self, number_of_flips, number_of_realizations):
        self.number_of_flips = number_of_flips
        self.number_of_realizations = number_of_realizations

        gamecost = -250 # cost of playing the game
        totalwinnings = 0 # initialize total winnings

        for j in range(0, self.number_of_realizations):
            fliplist = "" # create an empty string

            for i in range(0, self.number_of_flips): # iterate through 20 flips, treating 1's as heads and 0's as tails
                fliplist = fliplist + str((numpy.random.binomial(1, self.flip_probability))) #per https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html, add each flip to fliplist

            winnings = gamecost+(100*(fliplist.count("001"))) # find the number of Tails, Tails, Heads, multiply by fifty, add to cost of game to find winnings
            totalwinnings = totalwinnings + winnings # add all the realizations of winnings together

        averagewinnings = '${:,.2f}'.format((totalwinnings/self.number_of_realizations)) # find the average winnings
        print("Expected reward: ", averagewinnings) # print the average winnings

# Running above code

# Initialize an even 50-50 game
fiftyfiftyflip = Game(0.5)
# Run the simulation
fiftyfiftyflip.Simulate(20, 1000)
