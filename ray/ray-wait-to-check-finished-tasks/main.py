# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.13

# [python - Is there a way to do actions as soon as a process is finished processing instead of waiting for all to finish? - Stack Overflow](https://stackoverflow.com/questions/71825004/is-there-a-way-to-do-actions-as-soon-as-a-process-is-finished-processing-instead/)

import time
import ray

@ray.remote
def function(i):
    time.sleep(i)
    return i

print('create tasks')

# create tasks
all_tasks = [function.remote(i) for i in range(4)]

print('wait for results')

# run loop to get all results
while all_tasks:

    # wait for (at least one) finished tasks (and other tasks)
    finished, all_tasks = ray.wait(all_tasks, num_returns=1, timeout=None)
    
    for task in finished:
        result = ray.get(task)
        print('result:', result)
        
    print('len(all_tasks):', len(all_tasks))

