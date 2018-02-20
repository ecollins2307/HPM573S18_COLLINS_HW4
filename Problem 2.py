# HW 4, Problem 2
# Just copied the code from Problem 1, only changed the Game probability when running the code at the end

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

        for j in range(0, self.number_of_realizations): # iterate through realizations
            fliplist = "" # create an empty string

            for i in range(0, self.number_of_flips): # iterate through flips, treating 1's as heads and 0's as tails
                fliplist = fliplist + str((numpy.random.binomial(1, self.flip_probability))) #per https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html, add each flip to fliplist

            winnings = gamecost+(50*(fliplist.count("001"))) # find the number of Tails, Tails, Heads, multiply by fifty, add to cost of plahing the game to find winnings
            totalwinnings = totalwinnings + winnings # add all the realizations of winnings together

        averagewinnings = '${:,.2f}'.format((totalwinnings/self.number_of_realizations)) # find the average winnings
        print("Expected reward: ", averagewinnings) # print the average winnings

# Running above code

# Initialize a game with head probability of 0.4
fortysixtyflip = Game(0.4)
# Run the simulation
fortysixtyflip.Simulate(20, 1000)
