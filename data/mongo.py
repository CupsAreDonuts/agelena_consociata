import pymongo

def get_client():
    return pymongo.MongoClient('mongodb://localhost:27017/')

def get_social_database():
    client = get_client()
    return client['social_database']

def get_people():
    social_database = get_social_database()
    return social_database['people']
