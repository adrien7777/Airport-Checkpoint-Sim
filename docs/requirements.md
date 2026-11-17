# Requirements

The simulation shall accept the number of open lanes, run time, and arrival rate as 
configuration inputs. [R1]

T1: The sim will accept two lanes, a run time of 240 minutes, and an arrival rate of
1.0 passenger per minute as inputs without any errors. The simulation will echo 
these three inputs in its outputs, serve passengers in only lanes 1 and 2, generate
no events after 240 minutes, and log the number of passengers still in queue or in 
service at the end of the 240 minute run time. Total arrivals will fall between 194 
to 286 passengers. {R2}

The simulation shall produce identical results when run twice with the same 
random seed. [R2]

T2: The queue utilizing the same seed of 45, with two open lanes, a run time of 240
minutes in simulation, an arrival rate of 1.0 passenger per minute shall produce
exact arrival times, service start and end times, and departure times utilizing 
two independent simulation runs with the simulation from scratch and two new
generators for the seed. {R2}

The simulation shall record arrival, service start, service end, and departure times 
for every passenger at the designated checkpoint. [R3]

T3: The simulation will run two lanes, have a run time of 240 minutes, and an 
arrival rate of 1.0 passengers per minute. After the simulation, the passenger logs
will have one record of each passenger who arrived, with each record containing the
arrival time, service start and end time, and departure time. Passengers still in 
service or in queue at run time 240 minutes will be logged and marked incomplete. 
The number of passenger rows will match the number of total passengers. {R3}

The simulation shall identify and reject bad inputs such as zero lanes or a negative rate
for the data. [R4]

T4: The simulation will only accept valid inputs, lanes must be a positive integer,
run times must exceed 0, and arrival rate must be greater than 0, rejecting all 
other configuration inputs. In the case of bad inputs such as zero lanes, non-numeric
inputs, blank inputs, negative rates, the simulation will log the inputs with the 
error's input name, error message, store them in an error log, then end the 
simulation with no further events generated and no passenger row added. {R4}

The simulation shall save the results of the simulation into a database with identifiying
details such as a run ID, timestamp, and seed. [R5]

T5: The simulation will save arrival times, service start and end times, and 
departure times into a dedicated SQL database, with a unique run ID, result 
timestamps, and seed utilized. There will be a run record and passenger rows linked 
to it. The total number of passenger rows will match the total number of arrivals.{R5}

The simulation shall operate the queue as a first come, first served system. [R6]

T6: Using inputs of two lanes, a run time of 240 minutes, a seed of 45, and an 
arrival rate of 1.0 passengers per minute, the simulation will serve passengers in 
the same order that they arrived in, with no passenger overtaken or passed. A query 
through the passenger log will not return any rows that have mismatched pairings. {R6}

The simulation shall run for the average day period of an airport from either a 4 or an 8 
hour window of operation. [R7]

T7: The simulation with a seed of 45, a 2 lane, 1.0 passenger per minute arrival rate configuration
will run a total simulation time for both tests of 240 minutes and of 480 minutes and stop exactly 
at the end of the allocated time with no more events after the declared window of
operation, ensuring that the final event timestamp is less than or equal to the 
chosen run time. {R7}

The simulation shall run a configurable number of indepedent replications each with
a different seed and report the mean and a 95% confidence interval for each metric. [R8]

T8: The simulation with a 2 lane setup, 1.0 passenger/min rate, and 240 minute run time 
will run 30 distinct, independent replications each with a different chosen seed and will output a 95%
confidence interval for average service time, and average total time in system using 
data from reported mean, lower, and upper bounds. Recomputing this data will match the
reported values. Only passengers who have completed the service will be recorded and data from passengers still in service
or still in queue will be excluded from the averages. {R8} 

The simulation shall report average wait time, a 95th percentile wait time, maximum queue
length, and passengers served for each run. [R9]

T9: The simulation with an initial configuration of 2 lanes, a runtime of 240 minutes,
1.0 passenger/min, and a seed of 45 will report the average wait time, 95th percentile wait time interpolated,
maximum queue length, and passengers served for each run. Averages recomputed will match
reported values, maximum queue length will be computed using timestamps reported in the passenger logs
,passenger rows with recorded service will match the reported data for passengers served for each run.
Wait time is service start minus arrival and only passengers that have been serviced
will be counted in the data. {R9}


The simulation shall support a warm-up period that is logged but excluded from reported
statistics and data. [R10]

T10: Using two lanes, a runtime of 240 mins, an arrival rate of 1.0 passengers per minute,
a seed of 45, and a warmup period of 60 simulation minutes. The simulation will run the normal 240 minutes
and then echo the warmup input. Passengers that arrive before the 60 minute mark will
be counted in the passenger logs but excluded from averages. Recomputing the metrics reported will
exclude passenger data if their arrival time is before the 60 minute mark. Two runs with
different warm-up data should report back different passenger data. {R10} 
