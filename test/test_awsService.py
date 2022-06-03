import sys
from scripts import awsService
import pytest

def test_aws_service_init():
	awsService.aws_service()

def test_user_login():
	awsService.aws_service().user_login('test-user')
