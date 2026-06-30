import uuid
class User:
    def __init__(self, username:str, email:str, password:str, first_name:str, last_name:str, age:int, img_url:str|None):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.img_url = img_url
