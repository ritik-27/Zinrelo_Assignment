import unittest

from assign_class import AcmeWine,Order,User

test_data=[
    {
    "ID":1,
    "Name":"Jessi", 
    "BirthDay":"9/24/1958", #valid
    "Email":"JessiSRobinson@trashymail.com",#valid
    "State":"FL",#valid
    "ZipCode":"33025"#valid
    },
    {
        "ID":2,
        "Name":"Alice",
        "BirthDay":"2/12/2018", #invalid
        "Email":"Alice.abc@gmail.com", #valid
        "State":"TX", #valid
        "ZipCode":"31539" #valid
    },
    {
        "ID":3,
        "Name":"Robin",
        "BirthDay":"2/12/2000", #valid
        "Email":"Robin..@gmail.com", #invalid
        "State":"CT", #invalid
        "ZipCode":"31539" #valid
    },
    {
        "ID":4,
        "Name":"Dennis",
        "BirthDay":"2/9/2000", #valid
        "Email":"Dennis@gmail.com", #valid
        "State":"FL", #valid
        "ZipCode":"31249" #invalid
    }
]


class TestOrders(unittest.TestCase):
    
    def test_processFile(self):
        pass
    
    # def setUp(self):
    #     self.new_order = AcmeWine()
        
    
    # def test_is_valid_state(self):
    #     pass
    
    # def test_is_valid_zipcode(self):
    #     pass
    
    # def test_is_valid_birthday(self):
    #     pass
    
    # def test_is_valid_age(self):
    #     pass
    
    # def test_is_valid_email(self):
    #     pass



if __name__ == '__main__':
    unittest.main()