from unittest import TestCase
from assign_class import User
from datetime import datetime,date




class TestUser(TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        print('this is test class')
        cls.new_user=User('adwin',datetime.strptime('9/29/2000','%m/%d/%Y'),'adwin@gmail.com','FL','2468')
        
    # Condition 1 : No wine can ship to New Jersey [NJ], Connecticut[CT], Pennsylvania[PA], Massachusetts[MA], Illinois[IL], Idaho[ID] or Oregon[OR]
    def test_should_return_true_for_01_valid_state(self):                    
        self.new_user.state='AL' 
        result=self.new_user.is_valid_state()
        self.assertTrue(result)
        '''Valid states are = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
                                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]'''
        
    def test_should_return_false_for_02_invalid_state(self): 
        self.new_user.state='NJ'
        result=self.new_user.is_valid_state()
        self.assertFalse(result)
        '''Invalid states are = ['NJ','CT','PA','MA','IL','ID','OR']'''
        
        
    # Condition 2 : Wine can not ship to any zipcode that has two consecutive numbers next to each other
    def test_should_return_true_for_03_valid_zipcode(self):
        self.new_user.zipcode='24681'     #no consecutive digits are present in zipcode
        result=self.new_user.is_valid_zipcode()
        self.assertTrue(result)
        
    def test_should_return_false_for_04_invalid_zipcode(self):
        self.new_user.zipcode='234681'    #consecutive digits are present in zipcode
        result=self.new_user.is_valid_zipcode()
        self.assertFalse(result)
        
    
    # Condition 3 : Wine can not ship to anyone born on the first Monday of the month
    def test_should_return_false_for_05_first_monday_of_month(self):
        self.new_user.birthday=datetime.strptime('7/3/2023','%m/%d/%Y') #3rd july 2023 the first Monday of the month
        result=self.new_user.is_valid_birthday()
        self.assertFalse(result)
        
    def test_should_return_true_for_06_not_first_monday_of_month(self):
        self.new_user.birthday=datetime.strptime('7/27/2023','%m/%d/%Y')  #27th July 2023 is not first monday of month
        result=self.new_user.is_valid_birthday()
        self.assertTrue(result)
    
    
    # Condition 4 : Everyone ordering must be 21 or older
    def test_should_return_true_for_07_valid_age(self):
        self.new_user.birthday=datetime.strptime('7/27/2002','%m/%d/%Y') #21 yrs old
        result=self.new_user.is_valid_age()
        self.assertTrue(result)
        
    def test_should_return_false_for_08_invalid_age(self):
        self.new_user.birthday=datetime.strptime('9/29/2018','%m/%d/%Y') #5 yrs old
        result=self.new_user.is_valid_age()
        self.assertFalse(result)
        
    
    #Condition 5 : Email address must be valid 
    def test_should_return_true_for_09_valid_email(self):
        self.new_user.email='xys@email.com'    
        result=self.new_user.is_valid_email()
        self.assertTrue(result)
        
    def test_should_return_false_for_10_invalid_email(self):
        self.new_user.email='xys'    
        result=self.new_user.is_valid_email()
        self.assertFalse(result)
