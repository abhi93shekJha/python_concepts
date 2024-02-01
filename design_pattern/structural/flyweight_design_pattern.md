### Flyweight Design Pattern
- Very useful, when we have heavy objects and it is taking lot of RAM memory.
- For example, lets say we have a bullet object in a Game and there are 200 persons playing and every person gets 400 bullets.
- Since the bullet object will have an image field also along with other fields so the size of bullet object could be around 1 KB.
- And for 8000 bullets, size will be around 8 MB.
- If no. of players increases this can increase too much to store.
- Flyweight along with Registory removes this problem. It divides the attributes of the object into an extrinsic state(the attributes that will be changing) and intrinsic state (attributes that will remain constant and change for only few objects).
```python
from dataclasses import dataclass

@dataclass
class Bullet:
  type: str
  img: str

@dataclass  
class FlyingBullet:
  x: int
  y: int
  bullet: Bullet

class BulletRegistory():
  def __init__(self):
    self.registory = dict()

  def add_bullet(self, bullet):
    if bullet.type not in self.registory:
      self.registory[bullet.type] = bullet

  def remove_bullet(self, bullet):
    if bullet.type in self.registory:
      del self.registory[bullet.type]

  def get_bullet(self, bullet_type):
    return self.registory.get(bullet_type, None)


bullet_1 = Bullet(type="small", img="dsafsadf")
bullet_2 = Bullet(type="medium", img="dsafsadf")
bullet_3 = Bullet(type="large", img="dsafsadf")

bullet_registory = BulletRegistory()
bullet_registory.add_bullet(bullet_1)
bullet_registory.add_bullet(bullet_2)
bullet_registory.add_bullet(bullet_3)

flying_bullet_1 = FlyingBullet(x=0, y=0, bullet=bullet_registory.get_bullet("small"))
print(flying_bullet_1)
# FlyingBullet(x=0, y=0, bullet=Bullet(type='small', img='dsafsadf'))

flying_bullet_2 = FlyingBullet(x=5, y=5, bullet=bullet_registory.get_bullet("small"))
print(flying_bullet_2)
# FlyingBullet(x=5, y=5, bullet=Bullet(type='small', img='dsafsadf'))
``` 
