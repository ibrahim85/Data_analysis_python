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
            dt = t[i+step] - t[i]
            speed_vector.append(math.sqrt(math.pow(dx, 2) + math.pow(dy, 2)) / dt)
            i += step
        return speed_vector







def gradient():

    print('whatever2')


def slidingGradient():

    print('whatever2')