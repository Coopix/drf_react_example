from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Message

class MessageSerializer(HyperlinkedModelSerializer):
    """
    Responsible for serializing and deserializing message objects.
    """
    class Meta:
        model = Message
        fields = ('url', 'created', 'body')
        read_only_fields = ('url', 'created')


