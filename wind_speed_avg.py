# Python translation of this algorithm:
# https://www.mrexcel.com/forum/excel-questions/668043-calculating-average-wind-speed-direction.html

# Please ensure that magnitude.txt and direction.txt files are present near the wind_speed_avg.py, in the input folder
# Mag = Magnitude   Dir = Direction
# Magnitude nr of lines must be equal with Direction nr of lines!


import csv
import math
import os
import sys
from typing import List


# constants
MAGNITUDE = "magnitude"
DIRECTION = "direction"
FORMAT = ".txt"
RESULT_FILE = "result.csv"
WEIGHTED_VELOCITY = "weighted_velocity"
WEIGHTED_DIRECTION = "weighted_direction"



def VelX(mag, dir):
    pi = math.atan(1) * 4
    return mag * math.cos(2 * pi * (90 - dir) / 360)


def VelY(mag, dir):
    pi = math.atan(1) * 4
    return mag * math.sin(2 * pi * (90 - dir) / 360)


def ATAN2(x, y):
    pi = math.atan(1) * 4

    if x == 0:
        Rad = 2 * math.atan((math.sqrt(x * x + y * y) - y))
    else:
        Rad = 2 * math.atan((math.sqrt(x * x + y * y) - y) / x)

    if Rad < 0:
        Rad = Rad + pi * 2
    return Rad


def polarCoord(x, y):
    pi = math.atan(1) * 4

    if x == 0:
        if y == 0:
            rAlpha = 0
        else:
            rAlpha = 90 - ((y / y) * 90)
    else:
        rAlpha = 360 + (180 / pi * ATAN2(x, y))

    if rAlpha < 0:
        rAlpha = rAlpha + 360
    elif rAlpha > 360:
        rAlpha = rAlpha - 360
    return rAlpha


def calculate(magnitudes, directions):
    velX_result = []
    velY_result = []
    for i in range(0, len(magnitudes)):
        result = VelX(magnitudes[int(i)], directions[int(i)])
        velX_result.append(result)

        result = VelY(magnitudes[int(i)], directions[int(i)])
        velY_result.append(result)

    average_velX_result = sum(velX_result) / len(velX_result)
    average_velY_result = sum(velY_result) / len(velY_result)

    weighted_velocity = math.sqrt(average_velX_result ** 2 + average_velY_result ** 2)
    weighted_direction = polarCoord(average_velX_result, average_velY_result)
    return {
        WEIGHTED_VELOCITY: weighted_velocity,
        WEIGHTED_DIRECTION: weighted_direction,
    }


def write_to_csv(results: List[dict]):
    with open(os.path.join("output", RESULT_FILE), "w") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(["result_index", WEIGHTED_VELOCITY, WEIGHTED_DIRECTION])
        for index, result in enumerate(results, 1):
            csv_writer.writerow([index, result[WEIGHTED_VELOCITY], result[WEIGHTED_DIRECTION]])


def compute_wind_speed(magnitude_file: str, direction_file: str):
    with open(os.path.join("input", magnitude_file), "r") as input_magnitude:
        raw_magnitudes = [line.strip() for line in input_magnitude]
        magnitudes = [float(i) for i in raw_magnitudes]

        with open(os.path.join("input", direction_file), "r") as input_direction:
            raw_directions = [line.strip() for line in input_direction]
            directions = [float(i) for i in raw_directions]

            return calculate(magnitudes, directions)


def main():
    try:
        files_count: str = sys.argv[1]
    except IndexError:
        files_count = ""

    results: List[dict] = []
    if files_count:
        for file_num in range(1, int(files_count) + 1):
            magnitude_filename = MAGNITUDE + str(file_num) + FORMAT
            direction_filename = DIRECTION + str(file_num) + FORMAT
            results.append(compute_wind_speed(magnitude_filename, direction_filename))

    if not files_count:
        magnitude_filename = MAGNITUDE + FORMAT
        direction_filename = DIRECTION + FORMAT
        results.append(compute_wind_speed(magnitude_filename, direction_filename))

    write_to_csv(results)

if __name__ == "__main__":
    main()
