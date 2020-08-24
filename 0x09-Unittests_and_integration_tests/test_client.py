#!/usr/bin/env python3
""" Suite test client.py
"""
import unittest
from parameterized import parameterized, param
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test Github Org Client class """

    @parameterized.expand([
        param(org="google", test_payload={"payload": True}),
        param(org="abc", test_payload={"payload": False})
    ])
    def test_org(self, org, test_payload):
        """ test GithubOrgClient.org """
        with unittest.mock.patch('client.get_json',
                                 return_value=test_payload) as mock_method:
            github_org_client = GithubOrgClient(org_name=org)
            response = github_org_client.org
            self.assertEqual(response, test_payload)
            mock_method.assert_called_once()
