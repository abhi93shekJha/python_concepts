## Writing about Prototype Design Pattern

Write it when object creation is a time taking process and we need lots of object without spending time. (eg. Training Dataset object creation, Game object creation)

We can change only needed attributes and can have the same other attributes in the copied instances.

Idea is to create a copy or deepcopy of the existing object. We can use registory design pattern (sometimes called factory here) also to keep the instances in a map and return according to some type.

1. Creating an interface (using ABC) 'Clonable' with abstract clone method.
2. Implement the interface 'Clonable' in the class for which we need many objects in very less time.  






