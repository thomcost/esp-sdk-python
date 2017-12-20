# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.integrations_service_now_api import IntegrationsServiceNowApi


class TestIntegrationsServiceNowApi(unittest.TestCase):
    """ IntegrationsServiceNowApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.integrations_service_now_api.IntegrationsServiceNowApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Create a ServiceNow Integration
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single ServiceNow Integration
        """
        pass

    def test_update(self):
        """
        Test case for update

        Update a ServiceNow Integration
        """
        pass


if __name__ == '__main__':
    unittest.main()
