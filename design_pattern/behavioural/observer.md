### Observer Design Pattern
- Simply put, when state of an object changes, we may want to trigger some event.
- For example, let's say we have a Bitcoin Tracker class, and value of bitcoin changes within the class.
- As soon as, it changes in update_price, we may call events(method) like, send_sms, send_email, send_tweet, etc.
- This violates SRP.
- Another way can be, we can have a different class that will continuosly poll to check if the value of bitcoin has changed. It will trigger events, as soon as it finds changed value.
- This is correct but heavily resouce consuming.
- So we use observer design pattern, to fix the above mentioned problems. Implemented below.
- A good anomaly is, if we want to buy an iphone and waiting for it to arrive at a specific outlet, either I can go daily there to enqire about it which is wasteful, or, the shopkeeper of the outlet will send all of its customers a mail as soon as Iphone arrives. But this is also wasteful. To solve this, let's say, only interested customers (who will be buying) will register themselves with the shop, and the shopkeeper will only notify (send emails) to the registered customers (this sounds efficient).
- So the outlet is observable (Subject) and the customers are Observers.
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Bitcoin:
  price: int

class Observable():

  def __init__(self):
    self.observers = list() # we can have a set here for efficiency
    
  def add_observer(self, observer):
    if observer not in self.observers:  # with set, this will be faster
      self.observers.append(observer)

  def remove_observer(self, observer):
    if observer in self.observers:
      self.observers.remove(observer)

  def notify_observers(self, new_price):
    for observer in self.observers:
      observer.notify(new_price)

class BitcoinTracker(Observable):
  def __init__(self):
    super().__init__()
    self.bitcoin = Bitcoin(10)

  def update_price(self, new_price):
    self.bitcoin.price = new_price
    self.notify_observers(new_price)

class Observer(ABC):
  @abstractmethod
  def notify(self, message):
    pass

class EmailSender(Observer):
  def notify(self, message):
    print(f"Sending email with message {message}")

class SmsSender(Observer):
  def notify(self, message):
    print(f"Sending sms with message {message}")

class TweetSender(Observer):
  def notify(self, message):
    print(f"Sending tweet with message {message}")

# Client code
bitcoin_tracker = BitcoinTracker()
bitcoin_tracker.add_observer(EmailSender())
bitcoin_tracker.add_observer(SmsSender())
bitcoin_tracker.add_observer(TweetSender())

bitcoin_tracker.update_price(20)
# Sending email with message 20
# Sending sms with message 20
# Sending tweet with message 20

bitcoin_tracker.update_price(30)
# Sending email with message 30
# Sending sms with message 30
# Sending tweet with message 30
```
