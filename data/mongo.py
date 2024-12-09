import pymongo


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


def edit_person_in_people(person: dict):
    get_people().update_one({'_id': person['_id']}, update={"$set": person}, upsert=False)


def get_all_entries_of_person(first_name: str, last_name: str) -> list:
    query = {'first_name': first_name, 'last_name': last_name}
    found_people = get_people().find(query)
    return list(found_people)
