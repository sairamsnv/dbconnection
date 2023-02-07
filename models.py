import pymongo
from passlib.hash import sha512_crypt as sha
#from cryptography.fernet import Fernet
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['Netdb']
mydata=db.information
#collection....
collection = mydata['sample']
#key = Fernet.generate_key()
#fernet = Fernet(key)

class db:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def authencate(self):
        x = []

        cur = collection.find({"username":self.username})
        for i in cur:
            x.append(i)
            if bool(x) == True:
                updated=Di_update(x)
                        #mes1=updated['username']
                mes=updated['password']

                        #decMessage = fernet.decrypt(mes).decode()
                flag=sha.verify(self.password,mes)
                if flag == True:
                    return "suc"
                else:
                    return "unsuc"

            else:
                return "incorret username"
    def add_username(self):
        x=[]
        cur = collection.find({"username":self.username})
        for i in cur:
            x.append(i)
        if bool(x) == True:
            return "alredy taken"
        else:
            # be encoded to byte string before encryption
            #encMessage = fernet.encrypt(password.encode())
            password = sha.hash(self.password)
            emp_record = {
                "username":self.username,
                "password":password,
                }

        #Insert collection....
        collection.insert_one(emp_record)
        return "suc created"








def Di_update(vil):
    result = {}
    for d in vil:
        result.update(d)
    return result

