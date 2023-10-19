import math
from sample_data import *
from createArray import *
from TEST_DATASET import *


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

                if cell_length <= sensor_range:
                    data_map[i][j] += 10
                    
        return data_map
    

#<test_data>
sensor_range = 30
data_map = rectangle_140by140



#인스턴스1 생성 - 센서(2,2)
sensor_position = (50,46)
test_instance = Sensor(data_map, sensor_position, sensor_range)
#print(test_instance.deploy_sensor())
data_map = test_instance.deploy_sensor()
'''
#인스턴스2 생성 - 센서(0,0)
sensor_position = (90,70)
test_instance2 = Sensor(data, sensor_position, sensor_range)
#print(test_instance2.deploy_sensor())
data = test_instance2.deploy_sensor()
'''
#결과
visual_array("결과", data_map)

