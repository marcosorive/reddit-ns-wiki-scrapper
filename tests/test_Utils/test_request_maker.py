import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../src')
from request_maker import get_test_file, get_text_body_from_url


