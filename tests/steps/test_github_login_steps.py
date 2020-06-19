"""
This module contains step definitions for githubservice.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import pytest, pylenium, conftest
from pytest_bdd import scenario, scenarios, given, when, then, parsers


# Shared Variables

GitHub_login_url = 'https://github.com/login'
user = 'KTJ-Demo'
password = 'Dog.Bone1'


# Scenarios

scenarios('../features/github_login.feature')

# Given Steps

@given('the user is a valid Github user')
def gh_given_valid_user(py):
    py.visit(GitHub_login_url)
    print("Given")  

# When Steps

@when('the user logs in to Github with a valid user')
def gh_user_logs_in(py):
    py.get_xpath("//input[@id='login_field']").type(user)
    py.get_xpath("//input[@id='password']").type(password)
    py.get_xpath("//input[@value='Sign in']").click()
    print("When")

# Then Steps

@then('the user is logged into the github website')
def gh_user_is_logged_in(py):
    print("Then")