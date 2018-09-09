### Contacts-book-application

##### Developed in Flask-Restplus-swagger integration

##### Database 

MongoDB

Configure properties

`properties/configuration.json`

`"MONGO_URI": "mongodb://localhost:27017/contacts_book"`

`"MONGO_DATABASE": "contacts_book"`

#### Deploy in python 2.7 environment

`$ sudo apt-get install python-pip`

`$ sudo pip install virtualenv`

#### Create Python virtual env

`$ virtualenv contact-book-venv`

#### Activate virtual env
`$ source contact-book-venv/bin/activate`

#### Install required packges

`$ pip install -r requirements`

#### Start the app

Help

`$ python index.py --help`

start 

`$ python index.py`

#### Populate data

`GET request`

`http://localhost:5000/populate/data` make a request

#### Who can access the app (rbac_users)

See `rbac_users` in mongodb or `app/api/resources/populate_data.py`

data = [
            
            {"firstname": "harish",  "lastname": "singh", "username": "harish",  "password": "harish",  "roles": ["ADMIN", "USER"]},
            {"firstname": "ram",     "lastname": "gond",  "username": "ram",     "password": "ram",     "roles": ["ADMIN"]},
            {"firstname": "mohan",   "lastname": "yadav", "username": "mohan",   "password": "mohan",   "roles": ["ADMIN"]},
            {"firstname": "sanjeev", "lastname": "kumar", "username": "sanjeev", "password": "sanjeev", "roles": ["USER"]},
            {"firstname": "john",    "lastname": "singh", "username": "john",    "password": "john",    "roles": ["USER"]}
        ]
        
#### Available contacts

data = [

            {"firstname": "ram",    "lastname": "singh", "emailid": "a@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "yadav", "emailid": "b@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "gond",  "emailid": "c@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "kumar", "emailid": "d@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "kumar", "emailid": "e@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "f@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "g@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "h@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "i@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "j@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "k@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "l@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "m@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "n@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "o@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "p@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "q@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "ram",    "lastname": "singh", "emailid": "r@gmail.com",  "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "singh", "emailid": "abc@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "saxena", "emailid": "xyg@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "dude", "emailid": "har@gmail.com", "phone": "+91-789087977"},
            {"firstname": "shyam",  "lastname": "singh", "emailid": "shy@gmail.com", "phone": "+91-789087977"}
        ]
        
#### Test with Swagger UI

`http://localhost:5000/`

#### For testing end points Generate jwt token

`http://localhost:5000/<username>/<password>` <---- A rbac user
`http://localhost:5000/ram/ram` is ADMIN

![alt text](https://github.com/sandhyalalkumar/contacts-book-secure-ws/blob/master/generate_token.png)

Copy the generated token and pass it to API key with double quote

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhbSIsInBhc3N3b3JkIjoicmFtIiwiZXhwIjoxNTM2NTc3NDc1fQ.Y5ePPr6mv_NVYt62CDABqA03RxNwpU-v3kJcJV9QwV8`










