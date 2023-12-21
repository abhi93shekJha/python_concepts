### Registers
- These are used in a process to store and get values quickly during a program execution.
- It stores operators and operands for computaion, memory address to access data, program counters etc. to help quickly get access.
- It is a faster access than main memory.

### Stack
- To access data in LIFO manner.
- Generally methods are placed in stack in order of their execution.
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
- In python multithreading is only concurrent unlike java where is it parallel as well.

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
### Creating thread by subclassing theading.Thread
```python
import threading
class MyThread(threading.Thread):
  def run():
    print("Hello from a separate thread!!")

my_thread = MyThread()
my_thread.start()
# wait for my_thread to finish
my_thread.join()
```
### ThreadPoolExcecutor
- We should not always create and destroy a separate thread (as we did above) for ad-hoc tasks. If there are many ad-hoc tasks.
- This is a resource and time consuming process. As threads have their own stack, register and creating and destroying is time taking process.
- We should have pool of worker threads to execute bulk of tasks as it comes. ThreadPoolExecutor helps with this.

```python
from concurrent.futures import ThreadPoolExecutor
import time
def my_fun(thread_num):
  time.sleep(3)
  print(f'Thread {thread_num} is executing!!')
  print(f"Thread {thread_num} finished executing!!")
  return thread_num

if __name__ == "__main__":
  # using context manager is a good practice, as it closes automatically
  with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(my_fun, [0, 1, 2, 3, 4, 5], timeout=10)
    # this results is an iterable and gives us output sequentially 
    # according to input passed to map()
    # timeout will wait for 10 seconds for the tasks to complete, otherwise raises TimeoutError()
    for result in results: # this blocks
      # result contains what is returned from the function
      print(result)   # waits and then prints

  # using submit, returns a Future object
  with ThreadPoolExecutor(max_workers=5) as executor:
    # submit is a non blocking call
    future1 = executor.submit(my_fun, 0)
    future2 = executor.submit(my_fun, 1)

    # these two are blocking calls
    print(future1.result(timeout=5))  # timeout is optional 
    print(future2.result())
    
  print("Main done!")
```

### Race condition
- This happens when a memory is shared among multiple threads or we can say when multiple threads enter critical section.
- Below example will show an object being shared among two threads and how it leads to inconsistent state of data.
```python
from concurrent.futures import ThreadPoolExecutor
import time
class Data:
  def __init__(self):
    self.data = 0
  
  def update(self):
    local_var = self.data
    time.sleep(1)   # this will make first thread wait, and second one will get old(not modified) self.data value, causing inconsistency
    local_var += 1
    self.data = local_var

if __name__=="__main__":
  obj = Data()
  # obj.update()
  with ThreadPoolExecutor(max_workers=2) as executor:
    # both the below threads will execute the same object's method
    executor.submit(obj.update)
    executor.submit(obj.update)
    
  # After this obj.data should be 2, but it is 1
  # Note here that first the above two threads finish before main thread finishes, because of using context manager
  # context manager ensures the closing of threads
  print(obj.data)  #prints 1
```
### Fixing Race condition
- We can use locks (mutex) shown in below example (threading.Lock(), it should be shared as well)
```python
from concurrent.futures import ThreadPoolExecutor
import time
import threading
class Data:
  def __init__(self):
    self.data = 0
    self.__lock = threading.Lock()
  
  def update(self):
    with self.__lock:  # this is it, it will make the thread enter with a lock
      local_var = self.data
      time.sleep(1)   
      local_var += 1
      self.data = local_var

if __name__=="__main__":
  obj = Data()
  with ThreadPoolExecutor(max_workers=2) as executor:
    # both the below threads will execute the same object's method
    executor.submit(obj.update)
    executor.submit(obj.update)
    
  print(obj.data)  # prints 2 now
```
### Deadlock
- Occurs when a thread waits for the lock, which is locked by another thread and both wait for each other to finish.
- this condition blocks both the threads forever.
```python
import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
  with lock1:
    print("Thread 1 working!!")
    time.sleep(.1)  # this will give time for 2nd thread to run
    with lock2:  # this lock is with another thread
      print("Thread 1 won't reach here!!")

def fun2():
  with lock2:
    print("Thread 2 working!!")
    time.sleep(.1)
    with lock1:  # this lock is with another thread
      print("Thread 1 won't reach here!!")

thread1 = threading.Thread(target=fun1)
thread2 = threading.Thread(target=fun2)

thread1.start()
thread2.start()
```
### Producer and Consumer problem
- A producer produces data into a buffer and consumer uses it.
- We can get an exception in case the buffer is full and producer tries to push more to it.
- Similarly if buffer is empty and consumer tries to consume.
- This problem arises when there are multiple producers and consumers. When a producer checks that an space is present to produce (in the buffer), and execution goes to another producer, and this other producer finishes producing. This makes the previous paused producer try to produce to an already full buffer, cauring error.
- Same problem happens with multiple consumers.
- We can also say, this happens because of race condition, where a thread already enters the critical section and reads bad data to produce or consume.
```python
import threading
import random
import time
import queue

class Buffer():
  def __init__(self, size):
    self.size = size
    self.buffer = queue.Queue(maxsize=size) # fixed buffer

  def add_item(self, item):
    if self.buffer.not_full:
      self.buffer.put(item, block=False)
    else:
      pass

  def remove_item(self):
    if self.buffer.not_empty:
      return self.buffer.get(block=False)
    else:
      pass

class Producer(threading.Thread):
  def __init__(self, buffer):
    super().__init__()
    self.buffer = buffer

  def run(self):
    while True:
      item = random.randint(1, 101)
      self.buffer.add_item(item)
      print(f"Producer put {item} in the buffer")
      # random.uniform() generates a float in range given, excluding 0.5
      time.sleep(random.uniform(0.1, 0.5))

class Consumer(threading.Thread):
  def __init__(self, buffer):
    super().__init__()
    self.buffer = buffer

  def run(self):
    while True:
      item = self.buffer.remove_item()
      print(f"Consumer took {item} from the buffer")
      time.sleep(random.uniform(0.1, 0.5))

buffer = Buffer(10)
for i in range(10):
  producer = Producer(buffer)
  consumer = Consumer(buffer)
  producer.start()
  consumer.start()
```
- This can be solved by synchronizing the critical section.
- Another way is using semaphore shown below.
```python
import threading
import random
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed

class Buffer():
  def __init__(self, size):
    self.size = size
    self.buffer = []
    self.mutex = threading.Lock()
    self.empty = threading.Semaphore(self.size)
    self.full = threading.Semaphore(0)

  def add_item(self, item):
    with self.empty:
      with self.mutex:
          self.buffer.append(item)
      self.full.release()  

  def remove_item(self):
    with self.full:
      with self.mutex:
        item = self.buffer.pop(0)
      self.empty.release()
      return item

def producing_thread(buffer, item):
  time.sleep(1)
  print(f"Producer added {item}")
  buffer.add_item(item)

def consuming_thread(buffer):
  item = buffer.remove_item()
  time.sleep(1)
  print(f"Consumer consumed {item}!!")

buffer = Buffer(10)
with ThreadPoolExecutor(max_workers=20) as executor:
  producer_tasks = [executor.submit(producing_thread, buffer, i) for i in range(10)]

  # Wait for all producer tasks to complete
  for future in as_completed(producer_tasks):
      future.result()

  # Now submit the consumer tasks
  consumer_tasks = [executor.submit(consuming_thread, buffer) for _ in range(10)]

  # Wait for all consumer tasks to complete
  for future in as_completed(consumer_tasks):
      future.result()
```
