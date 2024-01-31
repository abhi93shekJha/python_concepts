### Strategy Pattern
- We use it when we have multiple ways to execute a task.
- We generally use it, when we have multiple algorithms to run based on some condition Ex.- Payment Gateway.
- We can write a single method with if-else to execute multiple logics, but it violates SRP and OCP.
- Another obvious way is to create an interface and multiple classes to accomodate multiple logics.
- This looks okay, but poses two problems, 
  1. Not easy to frequently change at runtime as strategies (logics) grows in future.
  2. Prone to code duplication.
- Strategy pattern solves all of the above problems. Implementation below.
- Strategy solves problem 1, since we can easily change only the strategy and inject it to main class implementing the main logic (MakePayment in this case), and it changes the behaviour.
- Strategy is solving problem 2 by, only making strategies of the changing logic, and rest of the code goes to class having main logic (MakePayment in this case). We can thoughtfully create only required core strategies and set the strategy.
- If we are simply using classes to inherit from an interface and adding logic to a method, above two solution will become complex to implement. Strategy pattern gives us really cleaner way to do this.
```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
  
  @abstractmethod
  def pay(self):
    pass
    
class CreditCardPaymentStrategy(PaymentStrategy):

  def pay(self):
    print("Paying using Credit card")

class UPIPaymentStrategy(PaymentStrategy):

  def pay(self):
    print("Paying using UPI")

class MakePayment:

  def __init__(self, payment_strategy, amount):
    self.payment_strategy = payment_strategy
    self.amount = amount

  def set_strategy(self, strategy):
    self.payment_strategy = strategy
    
  def pay_amount(self):
    self.payment_strategy.pay()
    

# client code
cc_payment_strategy = CreditCardPaymentStrategy()
upi_payment_strategy = UPIPaymentStrategy()

payment = MakePayment(upi_payment_strategy, 100)
payment.pay_amount()  # Paying using UPI

payment.set_strategy(cc_payment_strategy)
payment.pay_amount()   # Paying using Credit card

```
