# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_secret_env_source import V1SecretEnvSource


class TestV1SecretEnvSource(unittest.TestCase):
    """ V1SecretEnvSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1SecretEnvSource(self):
        """
        Test V1SecretEnvSource
        """
        model = kubernetes.client.models.v1_secret_env_source.V1SecretEnvSource()


if __name__ == '__main__':
    unittest.main()
