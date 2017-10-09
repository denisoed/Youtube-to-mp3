from django.test import TestCase
from django.test import Client
from .forms import YoutubeForms
from .tasks import *
from django.test.utils import override_settings
from django.core import mail

class TestCalls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_main_template_is_loaded(self):
        """ Get main.html template """
        response = self.client.get('/')
        self.assertTemplateUsed('main.html')
        self.assertEquals(response.status_code, 200)

    def test_success_template_is_loaded(self):
        """ Check redirect on success.html """
        response = self.client.get('/accept_data')
        self.assertTemplateUsed('success.html')
        self.assertEquals(response.status_code, 302)


class CheckInputData(TestCase):

    def setUp(self):
        self.normal_user_data = {
            'email': 'denisoed93@gmail.com',
            'url': 'https://www.youtube.com/watch?v=l32bsaIDoWk'
        }
        self.negative_user_data = {
            'email': '',
            'url': 'https://www.youtube.com/watch?v=l32bsaIDoWk'
        }

    def test_of_received_data(self):
        """ Return True if all fields are filled """
        form = YoutubeForms(self.normal_user_data)
        self.assertTrue(form.is_valid())

    def test_of_received_empty_data(self):
        """ Return False if the fields are not filled """
        form = YoutubeForms(self.negative_user_data)
        self.assertFalse(form.is_valid())

class TestSendMail(TestCase):

    def setUp(self):
        self.correct_mail = ('Subject', 'Message', 'example@gmail.com', 'recipient_list=False')
        self.not_correct_mail = ('Subject', 'Message', 'example@gmail.com', 'recipient_list=False')

    @override_settings(EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
    def test_correct_email_content(self):
        success_send_mail = mail.EmailMessage('Subject', 'Message', 'denisod93@gmail.com', ['denisoed@gmail.com'])
        success_send_mail.send()
        print(mail.outbox)
        self.assertEqual(len(mail.outbox), 0)

