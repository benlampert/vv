import datetime

from django.utils import timezone
from django.test import TestCase

from vendors.models import Vendor

class VendorMethodTests(TestCase):

    def test_was_added_recently_with_future_date(self):
        """
        was_added_recently() should return False vendors whose
        added_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_vendor = Vendor(added_date=time)
        self.assertEqual(future_vendor.was_added_recently(), False)