#requirements

The simulation shall accept the number of open lanes and potentially other variables as 
configuration inputs [R1]

The simulation shall produce identical, correct results when run twice with the same 
random seed [R2]

The simulation shall record arrival, service start, service end, and departure times 
for every passenger at the queue [R3]

The simulation shall sort and validate bad inputs such as zero lanes or a negative rate
for the data [R4]

The simulation shall save the results of the simulation into a database with identifiying
details such as a run ID, timestamp, and other recorded data [R5]

The simulation shall operate the queue as a first come, first served system [R6]

The simulation shall run for the average day period of an airport ranging from a 4 to 8 
hour window of operation [R7]

The simulation shall run a configurable number of indepedent replications each with
a different seed and report the mean and a 95% confidence interval for each metric [R8]

The simulation shall report average wait time, a 95th percentile wait time, maximum queue
length, and passengers served for each run. [R9]

The simulation shall support a warm-up period that is excluded from reported statistics
and data. [R10] 
