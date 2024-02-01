### Decorator Design Pattern
- It is used to add additional functionality to an existing object funtions.
- We can wrap around an existing functionality by injecting a wrapper object.
```python
from abc import ABC, abstractmethod

class Sender(ABC):
  @abstractmethod
  def send(self):
    pass

class EmailSender(Sender):

  def __init__(self, communicator=None):
    self.communicator = communicator

  def send(self):
    if self.communicator is not None:
      self.communicator.send()
    print("Sending email!!")

class SMSSender(Sender):

  def __init__(self, communicator=None):
    self.communicator = communicator
  
  def send(self):
    if self.communicator is not None:
      self.communicator.send()
    print("Sending sms!!")  

class TweetSender(Sender):

  def __init__(self, communicator=None):
    self.communicator = communicator
  
  def send(self):
    if self.communicator is not None:
      self.communicator.send()
    print("Sending tweet!!")

sms_sender = SMSSender()
email_sender = EmailSender(sms_sender)
email_sender.send()
# Sending sms!!
# Sending email!!
```
