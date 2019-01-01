from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from photos.views import HomeView


class UserTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='dede', email='jacob@', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/customer/details')

        # Recall that middleware are not supported. We simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Simulates an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Used for class-based views.
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)