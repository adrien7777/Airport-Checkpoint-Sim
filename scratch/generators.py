def countdown():
    for n in range (3, 0, -1):
        yield n

#for n in countdowm():
#   print(n)

g = countdown()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#What does yield do that return doesn't?

#yield pauses a function, allowing it to be resumed later,
#and gives back one results at a time. While return permanently ends
#the function and returns a single value (object) at once

#What happened on the 4th next() call, and why?

#StopIteration exception was raised because the generator had no more values to yield.

#Why might "pause and resume later" be useful for simulating 
#a passenger waiting in queue?

#Each passenger can be its own generator. Yield allows them to pause their activity
#(when a passenger is waiting for baggage, or for a security check). This pause can also
#allow other events to occur while the passenger waits. They can then resume where they left off and the total
#wait time can be tracked.