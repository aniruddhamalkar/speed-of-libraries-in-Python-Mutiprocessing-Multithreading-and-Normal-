# speed-of-libraries-in-Python-Mutiprocessing-Multithreading-and-Normal-
This repository is intended to check the speed of well know libraries in Python
Due to the global interpretation lock in Python unlike Java the python can able to process only one thread at a time, due to heap space overlapping.
The threading uses theads where as multiprocessing uses processes. 
Python memory manager provide same heap space to all the threads. As each thread tries to write in head space at same time there are chences of heap space bleeding, leaking overflow and merging with another threads.
To avoid such heap space overlapping Python provide Global interpertation lock which ensures only one thread is processed at  a time and only on thread write the shared memory at a time. The thread are switched on Time Division Multiplexing to provide user essaence of multiple threads are processed at a time.
As only one thread processed at a time multithreading in Python tends to be slow.
To avoid such Python has created mutiprocessing library which maps tasks to the processes. These processes have it own heap which does not cause any interference with other processes. As the processes are processed sperately and writen into sperate memory. Makes optimal use of the resources in the computer.
The mutiprocessing library in Python is way faster than the other type of libraries. 
This program is intended to provide the user essence of multitherading, multiprocessing and their process timing.
