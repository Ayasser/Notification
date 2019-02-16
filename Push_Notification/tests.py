from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import send_notification
from .models import Notification
from Customer.models import Customer,City,Language

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        self.user = User.objects.create_user(
            username='ayasser', email='ayasser@gmail.com', password='top_secret')
        self.notification = Notification.objects.create(header='test')
        self.city = City.objects.create(name_en='cairo',name_ar='cairo')
        self.language = Language.objects.create(language='engilsh')

        self.customer = Customer.objects.create(
            first_name='ahmed',last_name='yasser',birth_date='1995-04-04',phone_number='01233434553',
            email='ayasser@g.com',language=self.language,city=self.city)


    def test_details(self):
        request = self.factory.get('/sendnotification/?customer_ids=1&notification_id=1')

        request.user = self.user

        request.user = AnonymousUser()

        response = send_notification(request)
        self.assertEqual(response.status_code, 200)
