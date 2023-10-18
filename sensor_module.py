import math
from sample_data import *

sensor_range = 2
sensor_position = (0,0)
data = sample_data1


for i in range(len(data)):
    for j in range(len(data[0])):
        x_length = sensor_position[0] - j #가로축 길이
        y_length = sensor_position[1] - i      #세로축 길이
        cell_length = math.sqrt(pow(x_length, 2) + pow(y_length, 2))
        
        if  cell_length < sensor_range:
            data[i][j] += 1

print(data)