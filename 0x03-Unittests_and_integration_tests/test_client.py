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
                 mocked_function: MagicMock) -> None:
        """ Test the org method of the GithubOrgClient class"""
        mocked_function.return_value = MagicMock(
            return_value=expected_output)
        githubClient = GithubOrgClient(org_name)
        self.assertEqual(githubClient.org(), expected_output)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self) -> None:
        """ test public repos url method"""
        with patch(
                "client.GithubOrgClient",
                new_callable=PropertyMock,
        ) as mock:
            mock.return_value = {
                'repos_url': "https://a[i.github.com/orgs/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("Google")._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """test the public_repos method"""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
