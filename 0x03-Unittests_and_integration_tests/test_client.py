#!/usr/bin/env python3
"""Defines test cases for client class mtehods"""
import unittest
from unittest.mock import (
    Mock,
    patch,
    MagicMock,
    PropertyMock,
)
from client import GithubOrgClient
from typing import (
    List,
    Dict,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """Class for the GithubOrgClient class test methods
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name: str, expected_output: dict,
                 mocked_function: MagicMock):
        """ Test the org method of the GithubOrgClient class"""
        mocked_function.return_value = MagicMock(
            return_value=expected_output)
        githubClient = GithubOrgClient(org_name)
        self.assertEqual(githubClient.org(), expected_output)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
