from QUEUEME import *

# remeber in client site we dont use any varables in the serversied  with __Front bc they are protected we cant access them
q_obj = QUEUE(10)

for word in ["hi",34,43,"sdf","df","fsdf","dfg"]:
     q_obj.equeue(word)

print(f" the lenght {len(q_obj)} and the num {q_obj}")

while not q_obj.isEmpty(): # not is used to negate the condition.
     print(f"this is deque {q_obj.dequeue()}")
     



     

