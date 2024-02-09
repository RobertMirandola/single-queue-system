import random
import matplotlib.pyplot as plt

# For reference: 

# Little's law: L (average number of items in queue) = throughput (long term arrival rate) * service time

departure_rate = 0.75
arrival_rates = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
average_queue_delay = [] # list to keep track of queue length for each lambda
average_num_items_in_queue = [] # list to keep track of average num of items in queue
expected_queue_delay = [] # list to calculate theoretical expected delay
queue = [0]

# To calculate delay, take average_num_items_in_queue / arrival rate

# q(k+1) = q(k) + a(k) - d(k)
# a(k) ~ 1 w.p lambda and 0 w.p 1-lambda
# if q(k) + a(k) > 0, then d(k) = 1 w.p mu and 0 w.p. 1-mu

def check_next_item(arrivals, departures, count):
  # Utilize above equation
  next_queue_value = queue[count] + arrivals - departures
  
  # Add next queue value if greater than 0 (mainly for initial case)
  if(next_queue_value > 0):
    queue.append(next_queue_value)
  else:
    queue.append(0)
    
for arrival_rate in arrival_rates:
  for count in range(10**6):
    arrival_random_variable = random.uniform(0 ,1)
    departure_random_variable = random.uniform(0, 1)
    
    # Build the a(k)
    if arrival_random_variable < arrival_rate:
      arrival = 1
    else:
      arrival = 0
      
    # Build the d(k)
    if departure_random_variable < departure_rate:
      departure = 1
    else:
      departure = 0
      
    check_next_item(arrival, departure, count)
    
  # Calculate queue length and average queue length
  queue_length = len(queue)
  average_num_items_in_queue.append(sum(queue) / queue_length)
  queue = [0]
  
for i in range(len(arrival_rates)):
  # Compute actual queueing delay
  average_queue_delay.append(average_num_items_in_queue[i] / arrival_rates[i])
  
  # Compute theoretical queueing delay
  row = (arrival_rates[i] * (1 - departure_rate)) / (departure_rate * (1 - arrival_rates[i]))
  expected_queue_delay.append((1 / arrival_rates[i]) * (row / (1 - row)))
  
  
# Plot results
plt.title('Expected Queueing Delay vs Arrival Rate (λ)')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Expected Queueing Delay')
plt.plot(arrival_rates, average_queue_delay)
plt.plot(arrival_rates, expected_queue_delay)
plt.legend(['actual', 'theoretical'])
plt.show()


