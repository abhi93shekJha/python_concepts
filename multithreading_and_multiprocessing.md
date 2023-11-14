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
  
