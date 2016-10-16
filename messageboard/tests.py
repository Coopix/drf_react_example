from dateutil import parser
from rest_framework.test import APITestCase

from .models import Message
from .factories import MessageFactory

class MessageListTestCase(APITestCase):

    def test_unauthenticated_user_can_list_all_messages(self):
        messages = MessageFactory.create_batch(20)
        self.client.force_authenticate(user=None)

        response = self.client.get('/api/messages/')

        self.assertEqual(200, response.status_code)
        returned_bodies = [msg['body'] for msg in response.data]
        for message in messages:
            self.assertTrue(message.body in returned_bodies)


class MessageCreateTestCase(APITestCase):

    def test_unauthenticated_user_can_create_message(self):
        self.client.force_authenticate(user=None)
        payload = {'body': 'Tis but a scratch!'}

        response = self.client.post('/api/messages/', payload, format='json')

        self.assertEqual(201, response.status_code)
        self.assertTrue(response.data.get('url'))
        self.assertTrue(response.data.get('created'))
        self.assertEqual(payload['body'], response.data.get('body'))


class MessageRetrieveTestCase(APITestCase):

    def test_unauthenticated_user_can_retrieve_existing_message(self):
        message = MessageFactory.create()
        self.client.force_authenticate(user=None)

        response = self.client.get('/api/messages/{}/'.format(message.id))

        self.assertEqual(200, response.status_code)
        self.assertEqual(message.body, response.data.get('body'))
        self.assertEqual(
            message.created,
            parser.parse(response.data.get('created'))
        )
        self.assertTrue(response.data.get('url'))


class MessageModifyTestCase(APITestCase):

    def test_unauthenticated_user_can_modify_existing_message(self):
        message = MessageFactory.create(body='Good afternoon!')
        payload = {'body': 'Good night!'}
        self.client.force_authenticate(user=None)

        response = self.client.patch('/api/messages/{}/'.format(message.id),
            payload,
            format='json')

        self.assertEqual(200, response.status_code)
        message.refresh_from_db()
        self.assertEqual(payload['body'], message.body)


class MessageDestroyTestCase(APITestCase):

    def test_unauthenticated_user_can_destroy_existing_message(self):
        message = MessageFactory.create()
        self.client.force_authenticate(user=None)

        response = self.client.delete('/api/messages/{}/'.format(message.id))
        self.assertEqual(204, response.status_code)
        self.assertRaises(Message.DoesNotExist, message.refresh_from_db)
