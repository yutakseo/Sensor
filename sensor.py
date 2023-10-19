import math, os, sys

__file__ = os.getcwd()
__root__ = os.path.dirname(__file__)

mapdata_dir_path = os.path.join(__root__,"MapData")
sys.path.append(mapdata_dir_path)

from TEST_DATASET import *
from matplotlib import pyplot as plt


class Sensor:
    def __init__(self, map_data, sensor_position, coverage):
        self.map_data = map_data
        self.sensor_position = sensor_position
        self.coverage = coverage
        
    def deploy_sensor(self):    
        for i in range(0, len(self.map_data)):
            for j in range(0, len(self.map_data[0])):
                x_length = self.sensor_position[0] - j #가로축 길이
                y_length = self.sensor_position[1] - i      #세로축 길이
                cell_length = math.sqrt(pow(x_length, 2) + pow(y_length, 2))

                if cell_length <= self.coverage:
                    self.map_data[i][j] += 10
                    
        return self.map_data
    





