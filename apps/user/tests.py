from django.test import TestCase, Client

from apps.user.models import User


class UserTest(TestCase):

    def test_register_user(self):
        client = Client()
        response = client.post('/register/', data={'nickname': 'jack chen'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, 'utf8'), '注册成功')

    def test_namesake_user(self):
        client = Client()
        User.objects.create(nickname='吴彦祖')
        response = client.post('/register/', data={'nickname': '吴彦祖'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, 'utf8'), '注册失败')
