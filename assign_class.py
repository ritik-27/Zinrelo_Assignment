import csv
# import datetime
from datetime import datetime,date
# import datetime

class AcmeWine:
    valid_orders=[]
    invalid_orders=[]
    
        
    def process_file(self,filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                order_id=row["ID"]
                name=row["Name"]
                birthday=row["Birthday"]
                email=row["Email"]
                birthday=datetime.strptime(row["Birthday"], '%m/%d/%Y')
                zipcode=row["ZipCode"]
                state=row["State"]
                
                order=Order(order_id,name,birthday,email,state,zipcode)
                
                if order.validate_order():
                    self.valid_orders.append(order_id)
                else:
                    self.invalid_orders.append(order_id)
                
        with open('valid.csv', 'w') as valid_file:
            writer=csv.writer(valid_file)
            writer.writerow(['order_ids for Valid Orders'])
            writer.writerows(zip(self.valid_orders))
        with open('invalid.csv', 'w') as invalid_file:
            writer=csv.writer(invalid_file)
            writer.writerow(['order_ids for Invalid Orders'])
            writer.writerows(zip(self.invalid_orders))
            
        print("\nAll Orders processed successfully\n")
        print("valid orders count   : ",len(self.valid_orders))
        print("invalid orders count: ",len(self.invalid_orders))


class Order:

    def __init__(self,id,name,birthday,email,state,zipcode):
        self.id=id
        self.user=User(name,birthday,email,state,zipcode)
        
    def validate_order(self):
        return self.user.is_valid_state() and self.user.is_valid_zipcode() and self.user.is_valid_birthday() and self.user.is_valid_age() and self.user.is_valid_email()
    

class User:
    def __init__(self,name,birthday,email,state,zipcode):
        self.name=name
        self.birthday=birthday
        self.email=email
        self.state=state
        self.zipcode=zipcode
    
    # condition_1
    def is_valid_state(self):
        return self.state not in ['NJ','CT','PA','MA','IL','ID','OR']
    
    # condition_2
    def is_valid_zipcode(self):
        for i in range(len(self.zipcode)-1):
            if abs(int(self.zipcode[i]) - int(self.zipcode[i+1]))==1:
                return False
        return True
    
    # # condition_3
    def is_valid_birthday(self):
        if (self.birthday.weekday()== 0 and self.birthday.day<=7):
            return False
        else: 
            return True
                    
    
    # condition_4
    def is_valid_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age>=21
    
    # condition_5
    def is_valid_email(self):
        import re
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(re.fullmatch(regex,self.email))


csv_file='orders.csv'
store_1=AcmeWine()
store_1.process_file(csv_file)
