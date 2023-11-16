### Registers
- These are used in a process to store and get values quickly during a program execution.
- It stores operators and operands for computaion, memory address to access data, program counters etc. to help quickly get access.
- It is a faster access than main memory.

### Stack
- To access data in LIFO manner.
- Generaly methods are placed in stack in order of their execution.
- And the local variables contained in the methods.

### Process
- It is a program in execution.
- Many processes run by os in the backgroud.
- It has it's own memory space (heaps, code, data (static or global), files).
- It also has its own register and stack.
- A program contains instructions and it is run by a process.
- Multiple processes can run a single program.

## Threads
- It is a lightweight process.
- A single process has multiple threads.
- A thread is a unit of execution within a process.
- They share memory space (heaps, code, data (static or global), files). That is why synchronization and locking is needed to avoid inconsistency.
- They have their own registers(program counters) and stacks(functions with local variables).
  
### Processes vs Threads

| Processes                               | Threads                                    |
| ----------------------------------------| ------------------------------------------ |
| 1. These are called heavyweight processes and they have their own memory space. | 1. These are called lightweight processes as they share memory space. |
| 2. Context Switching is slow in processes. | 2. Context switching is faster among threads. |
| 3. Processes have their own code, data/files, heaps, stacks, and registers. | 3. Threads share code, data/files, heaps, but have their own stacks and registers. |
| 4. Processes are independent of each other. Communication is slower. | 4. Threads are interdependent as they share resources. Communication is faster. |
| 5. Example: Opening two different browsers. | 5. Example: Opening tabs in the same browser. |


### Concurrency
- It is not parallel execution. Multiple threads can work on multiple tasks by jumping from on task to another (context switching). But at one time only one thread runs.
- Context switching is time consuming.
- A single core can only execute one thread at a time concurrently.
- It is generally helpful when there is heavy I/O operations (reading, writing to a file, making a network request etc.).
- In python multithreading in only concurrent unlike java where is it parallel as well.

### Parallelism
- Here multiple threads can run concurrently and at the same time.
- Use multiple cores in a cpu.
- Java automatically achieves this using threads. Python uses multiple processes to achieve this.

## Points about thread
- Deamon threads is closed by interpreter as soon as main program finishes. Deamon thread creation shown in below example. 
- Calling join on a thread pauses the calling thread and first finishes the joined thread.
- When the program ends, python interpreter runs __shutdown method. It calls join method on all the running non-deamonic threads.
- It means it has to run all the unfinished threads to completely shutdown the program.

```python
import time
import threading
def my_fun(par1, par2="default"):
  start_time = time.time()
  time.sleep(1)
  print(f'hello after sleep!! {par1}, {par2}')
  end_time = time.time()
  time_taken = end_time - start_time
  print("total time taken: {:.2f}".format(time_taken))


if __name__ == "__main__":
  thread1 = threading.Thread(target=my_fun, args=(1,))
  thread2 = threading.Thread(target=my_fun, args=(2,))
  thread1.start()
  thread2.start()
  deamon_thread = threading.Thread(target=my_fun, args=("deamon",))
  deamon_thread.daemon = True   # this deamon thread will end as soon as main ends, won't print anything
  deamon_thread.start()
  print("Main done!!")
'''
Above code output:
Main done!!
hello after sleep!! 1, default
total time taken: 1.00
hello after sleep!! 2, default
total time taken: 1.00
'''
```
Thread is selected randomly by os. Output is not guaranteed. Shown in the example below.
```python
import time
import threading
def my_fun(thread_num):
  print(f'Thread {thread_num} is executing!!')
  time.sleep(1)
  print(f"Thread {thread_num} finished executing!!")


if __name__ == "__main__":
  thread_pool = list()
  for i in range(0, 5):
    thread = threading.Thread(target=my_fun, args=(i,))
    thread.start()
    thread_pool.append(thread)

  for thread in thread_pool:
    thread.join()

  print("Main done!")
'''
Output:
Thread 0 is executing!!
Thread 1 is executing!!
Thread 2 is executing!!
Thread 3 is executing!!
Thread 4 is executing!!
Thread 0 finished executing!!
Thread 2 finished executing!!
Thread 1 finished executing!!
Thread 3 finished executing!!
Thread 4 finished executing!!
Main done!
'''
```
### ThreadPoolExcecutor
- We should not always create and destroy a separate thread (as we did above) for ad-hoc tasks. If there are many ad-hoc tasks.
- This is a resource and time consuming process. As threads have their own stack, register and creating and destroying is time taking process.
- We should have pool of worker threads to execute bulk of tasks as it comes. ThreadPoolExecutor helps with this.



