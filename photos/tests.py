from django.contrib.auth.models import User
from django.test import TestCase
from photos.models import Photo
import unittest


class PhotoTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('FanHongfei', 'fanghongfei@tongji.cn', 'fanpassword')
        user2 = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
        user3 = User.objects.create_user('Stephen', 'stephen@comiccoon.gr', 'stephenpassword')
        user4 = User.objects.create_user('Lucas', 'frisbee@staff.gr', 'lucaspassword')
        user5 = User.objects.create_user('Miguel', 'lennon@mexican.mx', 'miguelpassword')
        Photo.objects.create(owner=user, name="tongji", url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546935308&di=84ca078b16bb66bd853f2f1eb7c8a786&imgtype=jpg&er=1&src=http%3A%2F%2Fpic31.photophoto.cn%2F20140508%2F0007020193468004_b.jpg", description="Tongji logo", created_at="2018-12-26 05:51:50", modified_at="2018-12-30 00:00:17", license="Free of Charges", visibility="PUBLIC")
        Photo.objects.create(owner=user2, name="baidu", url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546431600&di=00de56a62975767db2f9d2b95c8a4747&imgtype=jpg&er=1&src=http%3A%2F%2Fpic.kekenet.com%2F2015%2F0328%2F74181427517545.jpg", description="Baidu logo", created_at="2018-12-28 01:51:17", modified_at="2018-12-31 12:51:17", license="AA", visibility="PUBLIC")
        Photo.objects.create(owner=user3, name="laptop", url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546935363&di=01cb252d835b69747afb7d883b75c6c5&imgtype=jpg&er=1&src=http%3A%2F%2F2b.zol-img.com.cn%2Fproduct%2F189%2F919%2Fcexd04Zm6vKQc.jpg", description="Laptop logo", created_at="2018-12-29 04:00:17", modified_at="2018-12-30 15:51:17", license="Free of Charges", visibility="PRIVATE")
        Photo.objects.create(owner=user4, name="headphones", url="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=512089496,521298707&fm=26&gp=0.jpg", description="Headphones logo", created_at="2014-12-26 08:51:17", modified_at="2018-12-26 09:51:17", license="Amayuelas", visibility="PUBLIC")
        Photo.objects.create(owner=user5, name="keyboard", url="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=141531330,3558427081&fm=26&gp=0.jpg", description="Keyboard logo", created_at="2017-02-22 04:51:17", modified_at="2018-01-26 04:51:17", license="Free of Charges", visibility="PUBLIC")

    def test_new_photo(self):
        tongji = Photo.objects.get(name="tongji")
        baidu = Photo.objects.get(name="baidu")
        laptop = Photo.objects.get(name="laptop")
        headphones = Photo.objects.get(name="headphones")
        keyboard = Photo.objects.get(name="keyboard")
        self.assertEqual(tongji.pk, 1)
        self.assertEqual(baidu.pk, 2)
        self.assertEqual(laptop.pk, 3)
        self.assertEqual(headphones.pk, 4)
        self.assertEqual(keyboard.pk, 5)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()