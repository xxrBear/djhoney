from django.test import TestCase, Client

from apps.user.models import User


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """设置测试数据"""
        User.objects.create(nickname='吴彦祖')
        cls.client = Client()

    def test_register_user(self):
        """测试注册接口"""
        response = self.client.post('/register/', data={'nickname': 'jack chen'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, 'utf8'), '注册成功')

    def test_namesake_user(self):
        """测试同名用户注册"""
        response = self.client.post('/register/', data={'nickname': '吴彦祖'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, 'utf8'), '注册失败')
