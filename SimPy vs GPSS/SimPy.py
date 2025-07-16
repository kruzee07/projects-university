# NAME-  SAMAKSH MONGA
#               KRUTARTH GHUGE

##################################### PROJECT 1_SimPy_example  ##########################

import simpy
import random

# Define input parameters
ARRIVAL_RATE = 1.5  # customers per minute
SERVICE_RATE = 2    # customers per minute
SIMULATION_TIME = 100  # total simulation time in minutes

# Define simulation environment
class QueueSystem:
    def __init__(self, env, arrival_rate, service_rate):
        self.env = env
        self.queue = simpy.Store(env)  # create a queue object in the simulation environment
        self.server = simpy.Resource(env, capacity=1)  # create a resource object representing the server
        self.arrival_rate = arrival_rate  # set the arrival rate of customers
        self.service_rate = service_rate  # set the service rate of the server

    def customer_arrival(self):
        customer_id = 0
        while True:
            # generate customer arrivals according to an exponential distribution with the specified arrival rate
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            customer_id += 1
            # when a customer arrives, initiate the serving process
            self.env.process(self.serve_customer(customer_id))

    def serve_customer(self, customer_id):
        with self.server.request() as request:
            # request access to the server
            yield request
            # simulate service time for the customer
            yield self.env.timeout(random.expovariate(self.service_rate))
            # print a message indicating that the customer has been served
            print(f"Customer {customer_id} served at time {self.env.now}")

# Run simulation
env = simpy.Environment()  # create a simulation environment
queue_system = QueueSystem(env, ARRIVAL_RATE, SERVICE_RATE)  # create an instance of the QueueSystem class
env.process(queue_system.customer_arrival())  # initiate the customer arrival process
env.run(until=SIMULATION_TIME)  # run the simulation until the specified simulation time
