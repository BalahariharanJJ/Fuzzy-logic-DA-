#1
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#2
car_distance = ctrl.Antecedent(np.arange(0, 101, 1), 'car_distance')
car_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'car_speed')

#3
traffic_light_color = ctrl.Consequent(np.arange(0, 101, 1), 'traffic_light_color')

#4
car_distance['close'] = fuzz.trimf(car_distance.universe, [0, 0, 50])
car_distance['medium'] = fuzz.trimf(car_distance.universe, [0, 50, 100])
car_distance['far'] = fuzz.trimf(car_distance.universe, [50, 100, 100])

car_speed['slow'] = fuzz.trimf(car_speed.universe, [0, 0, 50])
car_speed['medium'] = fuzz.trimf(car_speed.universe, [0, 50, 100])
car_speed['fast'] = fuzz.trimf(car_speed.universe, [50, 100, 100])

#5
traffic_light_color['red'] = fuzz.trimf(traffic_light_color.universe, [0, 0, 50])
traffic_light_color['green'] = fuzz.trimf(traffic_light_color.universe, [0, 50, 100])

#6
rule1 = ctrl.Rule(car_distance['close'] | car_speed['fast'], traffic_light_color['red'])
rule2 = ctrl.Rule(car_distance['medium'] & car_speed['medium'], traffic_light_color['green'])
rule3 = ctrl.Rule(car_distance['far'] | car_speed['slow'], traffic_light_color['green'])

#7
traffic_control = ctrl.ControlSystem([rule1, rule2, rule3])

#8
traffic_simulator = ctrl.ControlSystemSimulation(traffic_control)

#9
traffic_simulator.input['car_distance'] = 40
traffic_simulator.input['car_speed'] = 80

#10
traffic_simulator.compute()

#11
traffic_light_color_output = traffic_simulator.output['traffic_light_color']

#12
if traffic_light_color_output <= 50:
    traffic_light_text = 'Red'
else:
    traffic_light_text = 'Green'

#13
print("Traffic Light Color Output (Numerical Value):", traffic_light_color_output)
print("Traffic Light Color Output (Text):", traffic_light_text)

car_distance.view()
car_speed.view()
traffic_light_color.view()
