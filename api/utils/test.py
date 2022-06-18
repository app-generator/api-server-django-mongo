from rest_framework.test import APISimpleTestCase


# Using APISimpleTestCase to avoid the database been flushed at each test.
# For more information, check
# https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#advanced-features-of-transactiontestcase.

class CustomAPITestCase(APISimpleTestCase):
    databases = '__all__'
