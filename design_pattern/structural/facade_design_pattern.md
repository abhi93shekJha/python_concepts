### Facade Design Pattern
- We expose a simplied interface to client for a complex set of implementations.
- This is used for exposing libraries interfaces or a third party API.
- For example, placing order is not a single step process, it will involve making payment, getting payment status, updating order details in DB, updating analytics, sending emails, generating invoice, etc.
- We use facade design pattern to hide these implementations inside a simple looking interface, example below.
```python
from dataclasses import dataclass

class PaymentProcessor:
  pass
class DatabaseProcessor:
  pass
class AnalyticsProcessor:
  pass
class EmailProcessor:
  pass
  
class MakeOrder:
  process_payment: PaymentProcessor
  update_db: DatabaseProcessor
  update_analytics: AnalyticsProcessor
  send_email: EmailProcessor

  def process_order(self):
    print("work with PaymentProcessor")
    print("work with DatabaseProcessor")
    print("work with AnalyticsProcessor")
    print("work with EmailProcessor")

# Simplified interface exposed to client
class ProcessOrder():
  def __init__(self):
    # will have to provide all the interfaces here as a constructor
    self.make_order = MakeOrder()

  def place_order(self):
    self.make_order.process_order()

# client's code
process_order = ProcessOrder()
process_order.place_order()
```
