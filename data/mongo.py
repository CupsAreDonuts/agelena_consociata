import pymongo
import pandas as pd

def get_client():
    return pymongo.MongoClient('mongodb://localhost:27017/')

def get_social_database():
    client = get_client()
    return client['social_database']

def get_people():
    social_database = get_social_database()
    return social_database['people']

def add_person_in_people(person: dict):
    get_people().insert_one(person)

def main():
    people = get_people()
    people_as_table = pd.DataFrame(list(people.find()))
    print(people_as_table)

if __name__ == '__main__':
    main()
