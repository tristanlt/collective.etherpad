import unittest2 as unittest
from collective.etherpad.tests import base, fake
from collective.etherpad import api


class UnitTestAPI(base.UnitTestCase):
    """Lets test the api module"""

    def setUp(self):
        super(UnitTestAPI, self).setUp()
        self.context = fake.FakeContext()
        self.request = fake.FakeRequest()
        self.api = api.HTTPAPI(self.context, self.request)
        self.load_fake()

    def load_fake(self):
        self.api._registry = fake.FakeRegistry()
        self.api._settings = fake.FakeEtherpadSettings()
        self.api._portal_url = "http://nohost.com"

    def test_update(self):
        self.api.update()
        self.assertEqual(self.api.uri, "http://nohost.com/pad/api/1.2/")
        self.assertEqual(self.api.apikey, "PLONEAPIKEY")

    def test_get_api(self):
        names = api.IEtherpadLiteClient.names()
        for name in names:
            method = self.api._get_api(name)
            self.assertTrue(method is not None)
            self.assertTrue(hasattr(method, '__call__'))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)