
# Documentation

   [mpi4py documentation](https://pythonhosted.org/mpi4py/usrman/tutorial.html)

    http://pythonhosted.org/mpi4py/

# Running (on Linux)

    $ mpiexec -n 5 python script.py


# Install (on Linux Mint based on Ubuntu)

Version 2.0.0

    apt install libopenmpi-dev
    pip install mpi4py

Module `mpi4py` needs file `mpi.h` to compile. It can be found in `libopenmpi-dev` and similar.
    
There is also older version 1.3.1 in Linux repository which doesn't need compilation

    apt install python-mpi4py
    apt install python3-mpi4py


---

Other packages with `mpi.h`: [Ubuntu packages]([http://packages.ubuntu.com/search?searchon=contents&keywords=mpi.h&mode=exactfilename&suite=lucid&arch=any)

---

- [MPICH](http://www.mpich.org/)
- [MPI tutorial](http://mpitutorial.com/)
