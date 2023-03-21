# Author: Sijie Yu
# Course: SSW-567A

from GithubApi import getApi
from GithubApi import getCommits

from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
import unittest

@patch("GithubApi.requests.get")
def test_getting_GithubApi(mock_get):
    mock_get.return_value.ok = True
    responseForApi = getApi()
    responseForCommits = getCommits()

    assert_is_not_none(responseForApi)
    assert_is_not_none(responseForCommits)


