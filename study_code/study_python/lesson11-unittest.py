#>38 unittest: function
# example 1
#in file name_function.py has a function named get_formatted_name need tests:
def get_formatted_name(first,last,middle=''):
    """generate a full name"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
#in test file test_name_function.py, we can test the function above:
import unittest
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    """test name_funtion.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('bruce','chen')
        self.assertEqual(formatted_name,'Bruce Chen')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('bruce','dosu','chen')
        self.assertEqual(formatted_name,'Bruce Chen Dosu')
unittest.main()
#>39 unittest: class
# example 1
# in file survey.py has a class named AnonymousSurvey need tests:
def AnonymousSurvey():
    """collect survey answers"""
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_question(self):
        print(self.question)
    def store_response(self,new_response):
        self.resonses.append(new_response)
    def show_result(self):
        print('show survey result:')
        for response in self.resonses:
            print('--'+response)
#in test file test_survey.py, we can test the class above:
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """test survey.py's class """
    def test_store_single_response(self):
        question="what language you can speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_responses(self):
        question="what language you can speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Japanese']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()
# example 2: setUp()
# class is the same as example 1, test file is different
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """test survey.py's class """
    def setUp(self):
        """create a list of response for convenient usage"""
        question = "what language you can speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Japanese']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn('self.responses[0]',self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,my_survey.responses)
unittest.main()
#other assertion: assertEqual/assertNotEqual/assertTrue/assertFalse
#/assertIn/assertNotIn
