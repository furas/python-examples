#!/usr/bin/env python2

#
# https://pythonhosted.org/mpi4py/usrman/tutorial.html
#
# mpiexec -n 5 python test-mpi.py
#

import requests
from mpi4py import MPI

# --- functions ---

def build_ranges(value, numsplits, rank):
    
    print '[RANK: %d ] build_ranges: %s/%s' % (rank, value, numsplits)
    
    ranges = []

    for i in range(numsplits):
        if i == 0:
            start = i
        else:
            start = int(round(1 + i * value/(numsplits*1.0), 0))

        end = int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))
            
        ranges.append((start, end))

    return ranges

 
def get_file_data(url, data_range, rank):
    
    print '[RANK: %d ] get_file_data: %s' % (rank, data_range)
    
    response = requests.get(url, headers={'Range': 'bytes=%s-%s' % data_range})
    data = response.content
    
    return data


def merge(filename, data, data_range, rank):

    offset, end = data_range
    
    print '[RANK: %d ] merge: %s-%s' % (rank, offset, end)

    fh = MPI.File.Open(comm, filename, amode)
    fh.Write_at_all(offset, data)
    fh.Close()
 
# --- main ---
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numr = comm.Get_size()
amode = MPI.MODE_WRONLY|MPI.MODE_CREATE

print '[RANK: %d ] starting: %d/%d' % (rank, rank, numr)

# ---------------------------------------------------------------------

# --- doesn't work ---
#url = 'http://2u.fileshare.ro/download/3172391991/JerryCo+Feat.+Sanziana+Niculae+-+Esti+Tot+Ce+Am+%28+Original+Radio+Edit+%29+%5B+AlegeMuzica.Info+%5D.mp3'

# --- works ---
url = 'http://greenteapress.com/thinkpython/thinkpython.pdf'
#url = 'http://www25.zippyshare.com/d/RTtv9Zv1/30183/Andra%20feat.%20David%20Bisbal%20-%20Without%20You%20%40%20PeMuzica.Com.mp3'
#url = 'http://broadcast.lds.org/churchmusic/MP3/1/2/nowords/271.mp3'

filename = url.split('/')[-1]
 
# - different proceses -
 
if rank == 0:
    if not url:
        print "Please Enter some url to begin download."
 
    # - get file size -

    response = requests.head(url, headers={'Accept-Encoding': 'identity'})
    size_in_bytes = response.headers.get('content-length', None)

    print '[RANK: %d ] %s bytes to download.' % (rank, size_in_bytes)

    if not size_in_bytes:
        print "Size cannot be determined."
        exit()
        
    # - generate ranges -
    
    byte_ranges = build_ranges(int(size_in_bytes), numr, rank)

    print '[RANK: %d ] byte_ranges: %s' % (rank, byte_ranges)

    # - send ranges -
    
    for itm in range(1, len(byte_ranges)):
        req = comm.isend(byte_ranges[itm], dest=itm, tag=itm)
        req.wait()

    # - "receive" range - 

    data_range = byte_ranges[0]

else:
    # - receive range - 

    req = comm.irecv(source=0, tag=rank)
    data_range = req.wait()

# - all processes -

print '[RANK: %d ] data_range: %s' % (rank, data_range)

# - download -
 
data = get_file_data(url, data_range, rank)

# - merge -

merge(filename, data, data_range, rank)

# - end -

print '[RANK: %d ] ending: %d/%d' % (rank, rank, numr)
