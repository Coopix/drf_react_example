import random
import string
import factory

from .models import Message

def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))

class MessageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Message

    body = factory.LazyAttribute(lambda t: random_string(2000))
