from mpi4py import MPI
import numpy as np

#
# run `mpiexec -n 5 python example.py`
#

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)
    
# Define MPI message tags
tags = enum('READY', 'DONE', 'EXIT', 'START')

# Initializations and preliminaries
comm = MPI.COMM_WORLD   # get MPI communicator object
size = comm.size        # total number of processes
rank = comm.rank        # rank of this process
status = MPI.Status()   # get MPI status object

if rank == 0:
    # Master process executes code below
    tasks = range(10)
    task_index = 0
    
    num_workers = size - 1
    closed_workers = 0

    results = dict()
    
    print("Master starting with %d workers" % num_workers)
    
    while closed_workers < num_workers:

        data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        source = status.Get_source()
        tag = status.Get_tag()

        #print(source, tag)
        
        if tag == tags.READY:
            
            # Worker is ready, so send it a task
            if task_index < len(tasks):
                comm.send(tasks[task_index], dest=source, tag=tags.START)
                print("Sending task %d to worker %d" % (task_index, source))
                task_index += 1
            else: 
                comm.send(None, dest=source, tag=tags.EXIT)
                
        elif tag == tags.DONE:
            
            print("Got data from worker %d" % source)
            if source not in results:
                results[source] = []
            results[source].append(data)
            
        elif tag == tags.EXIT:
            
            print("Worker %d exited." % source)
            closed_workers += 1

    print("Master finishing")

    print(results)
    
else:
    # Worker processes execute code below
    name = MPI.Get_processor_name()
    
    print("I am a worker with rank %d on %s." % (rank, name))

    while True:

        comm.send(None, dest=0, tag=tags.READY)
    
        data = comm.recv(source=0, tag=MPI.ANY_SOURCE, status=status)
        #source = status.Get_source()
        tag = status.Get_tag()

        #print(source, tag)

        if tag == tags.START:

            # create some example array
            data = np.array([data])
            result = data**2
            comm.send(result, dest=0, tag=tags.DONE)
            
        elif tag == tags.EXIT:
            
            comm.send(None, dest=0, tag=tags.EXIT)
            break
    
