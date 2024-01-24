### Mutiprocessing in python
- As we know that in python, because of GIL (Global Interpreter Lock), only one thread is allowed to execute at a time in interpreter.
- Unlike Java or other programming languages which allows multiple threads to run parallely inside multiple CPU cores, python can only run one thread at a time.
- When we run multithreading in python, the tasks run concurrently instead of running parallely.
- Multithreading, however, is useful for utilising waiting time at the time of I/O bound operations (reading/writing to a file, waiting for a network response).
- Here tasks are run concurrently by multiple thread, by taking turn with context switching.
- Multiprocessing is helpful running tasks parallely.
- It is useful for speeding up CPU intensive tasks (complex calculations, anything that takes up RAM etc.).
- In multiprocessing, each process will have its own interpreter and all prcesses run indepedently. However, we have ways to communicate with data
within processes. 
```python
import multiprocessing
import time

def func(pause_time):
  print(f"Sleeping for {pause_time} seconds")
  time.sleep(pause_time)

if __name__=="__main__":

  start_time = time.time()
  p1 = multiprocessing.Process(target=func, args=(1.5,))
  p2 = multiprocessing.Process(target=func, args=(1.5,))

  p1.start()
  p2.start()

  # join() will make current process wait until running process finishes
  p1.join()   
  p2.join()
  end_time = time.time()

  print(f"Time taken: {end_time-start_time}")  # prints, Time taken: 1.513805866241455
```
- We are now creating 10 threads. Note that this will also take almost 1.6 seconds only, even if I don't have 10 cores in my CPU.
- This is because processes have their ways of distributing tasks internally.
```python
import multiprocessing
from multiprocessing import process
import time

def func(pause_time):
  print(f"Sleeping for {pause_time} seconds")
  time.sleep(pause_time)

if __name__=="__main__":

  start_time = time.time()
  processes = []
  for _ in range(0, 10):
    p = multiprocessing.Process(target=func, args=(1.5,))
    p.start()
    processes.append(p)
    # We are not writing join() here, it will make the execution sequential (taking around 15 seconds), as if we are executing 10 methods in the same process.
    # This is because, as soon as join() is encountered, main process pauses and waits for joined process to finish.
    # So, if we write join here, firstly first process will finish, then after its execution second will finish and after this 3rd and so on.
    # but if we separate join, like below, all processes will be started and then all of them will be joined, so the main will pause and will wait for all
    # of them to finish first.

  for p in processes:
    p.join()
    
  end_time = time.time()

  print(f"Time taken: {end_time-start_time}")  # prints, 1.6041760444641113
```
### Using concurrent.futures.ProcessPoolExecutor
- It is exactly same as using ThreadPoolExecutor. Explaination present in multithreading explaination [here](multithreading.md)
```python
import concurrent.futures
import time
def my_fun(thread_num):
  print(f'Thread {thread_num} is executing!!')
  time.sleep(3)
  print(f"Thread {thread_num} finished executing!!")
  return thread_num

if __name__ == "__main__":

  # using context manager is a good practice, as it closes automatically
  with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
    start_time = time.time()
    results = executor.map(my_fun, [0, 1, 2, 3, 4, 5], timeout=10)
    # this results is an iterable and gives us output sequentially,
    # according to input passed to map()
    # timeout will wait for 10 seconds for the tasks to complete, otherwise raises TimeoutError() (optional)
    for result in results: # this line is blocking, (we get results according to input passed).
      # result contains what is returned from the function
      # We can catch exceptions here using try, catch
      print(result)   # waits and then prints
    end_time = time.time()
    print(f"Time taken by map {end_time-start_time}") # 3.14 seconds
  # using submit with result, It returns a Future object
  with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    # submit is a non blocking call
    future1 = executor.submit(my_fun, 0)
    future2 = executor.submit(my_fun, 1)

    # these two are blocking calls
    # We should be using try catch here.
    print(future1.result(timeout=5))  # timeout is optional 
    print(future2.result())

  # using concurrent.futures.as_completed method, it will give the result in the order they are finishing.
  with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    start_time = time.time()
    tasks = [1, 2, 3, 4, 5]
    futures = [executor.submit(my_fun, task) for task in tasks]
    for future in concurrent.futures.as_completed(futures):
      try:
        result = future.result()
        print(f"Using {result}")
      except Exception as e:
        print(e)
    end_time = time.time()
    print(f"Time taken by submit {end_time-start_time}") # 3.03 seconds
  print("Main done!")
  # NOTE: executor.map or executor.submit will not throw any exception, even if the function throws an exception,
  # It throws exception when we try utilizing the returned result
  # Also, with context managers being used, there is no need to add join, It will first wait for all the threads
  # to finish and then execute main thread.
```
