from django.test import TestCase

from apps.user.models import User


class UserTest(TestCase):

    def test_create_user(self):
        user = User.objects.get_or_create(nickname='韩信')
        self.assertEqual(user[0].nickname, '韩信')
