import math
import numpy


screenSizeX = 1.778 #relative sizes of the screen of the tablet. The distances are given as a reference to these units of measurements
screenSizeY = 1


def referenceSpaceCreator(resolution):

    global screenSizeX
    global screenSizeY

    minDistance=0
    maxDistance = math.sqrt((2*screenSizeX)**2 + (2*screenSizeY)**2)

    interval = (maxDistance - minDistance) / resolution;

    space = numpy.arange(minDistance, maxDistance, interval)

    return space
