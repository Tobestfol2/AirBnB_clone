import models
from models.base_model import BaseModel

b1 = BaseModel()
b1.name = "test"
s1 = models.storage
s1.new(b1)
s1.save()
s1.reload()
print(s1.all())
