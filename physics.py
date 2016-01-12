import math
import numpy


screenSizeX = 1.778 #relative sizes of the screen of the tablet. The distances are given as a reference to these units of measurements
screenSizeY = 1


class Resolutions(object):

    spaceResolution = 30
    speedResolution = 30
    gradientResolution = 30

    def __init__(self, space, speed, gradient):
        self.spaceResolution = space
        self.speedResolution = speed
        self.gradientResolution = gradient


class ReferenceGrid(object):

    minDistance = 0
    maxDistance = math.sqrt((2*screenSizeX)**2 + (2*screenSizeY)**2)

    minSpeed = 0
    maxSpeed = 4

    def __init__(self, resolution):
        interval = (self.maxDistance - self.minDistance) / resolution.spaceResolution
        self.space = numpy.arange(self.minDistance, self.maxDistance, interval)

        interval = (self.maxSpeed - self.minSpeed) / resolution.speedResolution
        self.speed = numpy.arange(self.minSpeed, self.maxSpeed, interval)


def referenceSpaceCreator(resolution):

    global screenSizeX
    global screenSizeY

    minDistance=0
    maxDistance = math.sqrt((2*screenSizeX)**2 + (2*screenSizeY)**2)

    interval = (maxDistance - minDistance) / resolution

    space = numpy.arange(minDistance, maxDistance, interval)

    return space


def speedGridCreator(resolution):

    minSpeed=0
    maxSpeed = 10

    interval = (maxSpeed - minSpeed) / resolution

    space = numpy.arange(minSpeed, maxSpeed, interval)

    return space
