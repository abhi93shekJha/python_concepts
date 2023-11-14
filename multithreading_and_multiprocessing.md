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


