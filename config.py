import os

DATABASE_URL = 'localhost'
DATABASE_PORT = '3306'
TARGET_TABLE = 'app_api_professor'

JSON_FILE = '/home/jeremytrieu/Desktop/rate-teacher-app/professor_data.JSON'

AUTH_FROM_FILE = True
CNF_FILE = os.path.abspath(os.path.join('/etc/mysql', 'my.cnf'))
API_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'api'))

def get_gmap_api_key():
    if AUTH_FROM_FILE:
        with open(API_FILE, 'r') as f:
            API_KEY = f.read()

    return API_KEY

def get_database_connection():
    if AUTH_FROM_FILE:
        with open(CNF_FILE, 'r') as configfile:
            file_list = configfile.read().split('\n')
            for i, line in reversed(list(enumerate(file_list))):
                if 'password' in line:
                    password = file_list[i].replace('password = ','')
                    username = file_list[i-1].replace('user = ','')
                    DATABASE_SCHEMA = file_list[i-2].replace('database = ','')
                    break
    else:
        print("\n\nEntering database: " + DATABASE_URL +
              ". Authentication required.")
        username = input("Username > ").strip()
        password = input("Password > ").strip()

    DATABASE_STRING = f"mysql+mysqlconnector://{username}:{password}@{DATABASE_URL}:{str(DATABASE_PORT)}/{DATABASE_SCHEMA}"

    return DATABASE_SCHEMA, DATABASE_STRING