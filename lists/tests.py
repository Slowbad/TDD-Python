from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_matsh(self):
        self.assertEqual(2, 3)
