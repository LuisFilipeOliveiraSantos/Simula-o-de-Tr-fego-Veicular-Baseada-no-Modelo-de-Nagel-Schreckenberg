from random import uniform, shuffle
import matplotlib.pyplot as plt
import numpy as np


road_length = 500         
num_iterations = 500     
traffic_density = 0.48     
max_speed = 2           
slowdown_probability = 0.2 


num_cars = int(traffic_density * road_length)
initial_state = [0] * num_cars + [-1] * (road_length - num_cars)
shuffle(initial_state)


states = [initial_state]

for _ in range(num_iterations):
    previous_state = states[-1]
    current_state = [-1] * road_length

    for position in range(road_length):
        if previous_state[position] > -1:
            current_speed = previous_state[position]

            distance = 1
            while previous_state[(position + distance) % road_length] < 0:
                
                distance += 1
            tentative_speed = min(current_speed + 1, distance - 1, max_speed)
            new_speed = (
                max(tentative_speed - 1, 0)
                if uniform(0, 1) < slowdown_probability
                else tentative_speed
            )
            current_state[(position + new_speed) % road_length] = new_speed

    states.append(current_state)


visual_matrix = np.zeros(shape=(num_iterations, road_length))
for col in range(road_length):
    for row in range(num_iterations):
        visual_matrix[row, col] = 1 if states[row][col] > -1 else 0

plt.imshow(visual_matrix, cmap="Greys", interpolation="nearest")
plt.show()
