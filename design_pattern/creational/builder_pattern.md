### Builder Design Pattern
### When creating a complex object (having multiple attributes), we can have below problems.
- We may want multiple constructors, to initiate the object with different set of attributes. This leads to a problem called telescoping constructor antipattern. This will force client to open the class and look for which all constructor are present when creating the class.
- We will also want to validate the attributes for correctness before creating an object and throw an exception if validation fails. It should not be done inside constructor, as it may bring difficulty to maintain, extend or test the code later on.
- We should also make our complex objects immutable to not bring any issues later on in the code. Immutability means the object should not change after it is created.

### We can implement below solution but these are not very efficient.
- We can pass in a dictionary to constructor and use it to initialize our attributes. Obviously, it will have two problems, firstly, the client will always have to open the class to see what all keys to provide for the dictionary, secondly, we can pass in any value to the dictionary (int at the place of str) which will throw error.
- In python, we can have default parameters, and keyword arguements, which will solve the problem of having multiple constructor. Now we can only have one constructor and give default values using default parameters. And using keyword arguements we can pass in any value to any parameter irrespective of order, so possibilty of passing wrong value to wrong arguement is gone. But this technique will not solve the problem of having validation logic inside constructor, which can become complex over time.

### Builder pattern fixes all of the above issues.
```python
from dataclasses import dataclass

@dataclass
class Database:

  host: str
  port: int
  username: str
  password: str

  @staticmethod
  def builder():
    return Database.Builder()
    
  class Builder:
    def __init__(self) -> None:
      self.host_val = None
      self.port_val = None
      self.username_val = None
      self.password_val = None
      
    def host(self, host):
      self.host_val = host
      return self

    def port(self, port):
      self.port_val = port
      return self

    def username(self, username):
      self.username_val = username
      return self

    def password(self, password):
      self.password_val = password
      return self

    def __validate_host(self):
      return True
    
    def build(self):
      if not self.__validate_host():
        return Exception("Wrong host!!")

      return Database(host=self.host_val, port=self.port_val, username=self.username_val, password=self.password_val)


db_builder = Database.builder().port(8000).host("localhost").username("Abhishek").password("1234")

db = db_builder.build()
print(db.port) #prints, 8000
  
```
- Now, we can add validation logic out of constructor.
- Also, the object can be make immutable, by making the attributes private for Database class and only exposing getters.
- Also, we can only initialize the attributes which are mandatory and add this logic in build method.
- The methods that are returning self inside Builder class are called 'fluent interface'.
