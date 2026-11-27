import random
import simpy

ARRIVAL_RATE = 1 / 60 # ONE PASSENGER EVERY 60 SECONDS
SERVICE_RATE = 1 / 45 #SERVICE TAKES 45 SECONDS, ON AVERAGE
SIM_TIME = 8 * 60 * 60 #SIMULATE 8 HOURS, IN SECONDS

waits = []

def passenger(env,server):
    arrival_time = env.now

    with server.request() as req:
        yield req
        waits.append(env.now - arrival_time)
        yield env.timeout(random.expovariate(SERVICE_RATE))

def arrivals(env,server):
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        env.process(passenger(env, server))


random.seed(42)
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)
env.process(arrivals(env,server))
env.run(until=SIM_TIME)

print("Passengers served:", len(waits))
print("Average wait (s):", sum(waits) / len(waits))

"""
Verification: M/M/1 theory predicts an averag ewaiting time of 135s ((λ = 1/60, μ = 1/45, ρ = 0.75))
8-hour run (Seed 42): 192 s 
1000-hour run: 128 s, within ~ 5% of theory
"""