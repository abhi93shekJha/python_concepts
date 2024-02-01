### Adapter Design Pattern
- As the name suggests, it works as an adapter to expose a common interface for varying types of interfaces.
- An example can be, if we are using different types of payment implementations with different third party libraries, all of them will have their own interfaces.
- We can create adapters for these third party interfaces forcing them to expose same method names. Example below,
```python
from abc import ABC, abstractmethod

class PayUPayment():
  def make_payment(self):
    print("Paying using PayUMoney.")

  def payu_payment_status(self):
    return 123

class StripePayment():
  def pay(self):
    print("Paying using Stripe.")

  def get_payment_status(self):
    return True

class PaymentAdapter(ABC):
  
  @abstractmethod
  def pay_money(self):
    pass

  @abstractmethod
  def check_payment_status(self):
    pass

class PayUAdapter(PaymentAdapter):
  def __init__(self):
    self.payU = PayUPayment()

  def pay_money(self):
    self.payU.make_payment()
  
  def check_payment_status(self):
    status = self.payU.payu_payment_status()
    return str(status)
    
class StripeAdapter(PaymentAdapter):
  def __init__(self):
    self.stripe = StripePayment()

  def pay_money(self):
    self.stripe.pay()

  def check_payment_status(self):
    status = self.stripe.get_payment_status()
    return str(status)

def process_payment(adapter):
  adapter.pay_money()
  print(adapter.check_payment_status())

pay_u_adapter = PayUAdapter()
process_payment(pay_u_adapter)  
# Paying using PayUMoney.
# 123

stripe_adapter = StripeAdapter()
process_payment(stripe_adapter)
# Paying using Stripe.
# True
```
