# Python translation of this algorithm:
# https://www.mrexcel.com/forum/excel-questions/668043-calculating-average-wind-speed-direction.html

# Please ensure that magnitude.txt and direction.txt files are present near the directionsAverage.py
# Mag = Magnitude   Dir = Direction
# Mag nr of lines must be equal with Dir nr of lines!

import math
import codecs


def VelX(mag, dir):
    pi = math.atan(1)*4
    return mag * math.cos(2 * pi * (90 - dir) / 360)


def VelY(mag, dir):
    pi = math.atan(1)*4
    return mag * math.sin(2 * pi * (90 - dir) / 360)


def ATAN2(x, y):
    pi = math.atan(1)*4

    if(x == 0):
        Rad = 2 * math.atan((math.sqrt(x * x + y * y) - y))
    else:
        Rad = 2 * math.atan((math.sqrt(x * x + y * y) - y) / x)

    if (Rad < 0):
        Rad = Rad + pi * 2       
    return Rad


def polarCoord(x, y):
    pi = math.atan(1)*4

    if(x == 0):
        if(y == 0):
            rAlpha = 0
        else:
            rAlpha = 90 - ((y / y) * 90)
    else:
        rAlpha = 360 + (180 / pi * ATAN2(x, y))

    if(rAlpha < 0):
        rAlpha = rAlpha + 360
    elif (rAlpha > 360):
        rAlpha = rAlpha - 360        
    return rAlpha


def calculate(magnitudes, directions):
    velX_result = []
    velY_result = []
    for i in range (0, len(magnitudes)):
        result = VelX(magnitudes[int(i)], directions[int(i)])
        velX_result.append(result)

        result = VelY(magnitudes[int(i)], directions[int(i)])
        velY_result.append(result)

    average_velX_result = sum(velX_result) / len(velX_result)
    average_velY_result = sum(velY_result) / len(velY_result)

    weighted_velocity = math.sqrt(average_velX_result**2 + average_velY_result**2)
    weighted_direction = polarCoord(average_velX_result, average_velY_result)
    return weighted_velocity, weighted_direction


def write_result(weighted_velocity, weighted_direction):
    with open("output.txt", 'w') as output_file:
        output_file.write("weighted_velocity: \n" + str(weighted_velocity) + "\n\n")
        output_file.write("weighted_direction: \n" + str(weighted_direction) + "\n")


def main():
    with open("magnitude.txt", 'r') as input_magnitude:
        raw_magnitudes = [line.strip() for line in input_magnitude]
        magnitudes = [float(i) for i in raw_magnitudes]

        with open("direction.txt", 'r') as input_direction:           
            raw_directions = [line.strip() for line in input_direction]
            directions = [float(i) for i in raw_directions]
        
            write_result(*calculate(magnitudes, directions))


if __name__== "__main__":
  main()