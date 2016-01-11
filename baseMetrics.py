import math

def speed(x, y, dt):

    return math.sqrt(math.pow(x,2) + math.pow(y,2)) / dt


def slidingSpeed(x, y, t, step):

    if len(x) != len(y) | len(x) != len(t):

        print('Error: X, Y and time vectors must have matching dimensions')
        return 0

    else:

        speed_vector = []
        i = 0

        while (i + step) < len(x):

            dx = x[i+step] - x[i]
            dy = y[i+step] - y[i]
            if t[i+step] - t[i] != 0:
                dt = t[i+step] - t[i]
            else:
                print('Warning: there was a timestep calculation that gave value 0. Previous timestep has been used '
                      'instead.')
            speed_vector.append(math.sqrt(math.pow(dx, 2) + math.pow(dy, 2)) / dt)
            i += step
        return speed_vector



def gradient():

    print('whatever2')


def slidingGradient():

    print('whatever2')