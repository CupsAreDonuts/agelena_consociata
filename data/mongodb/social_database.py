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


def get_meetings():
    social_database = get_social_database()
    return social_database['meetings']


def add_meeting_in_meetings(meeting: dict):
    meetings = get_meetings()
    meetings.insert_one(meeting)


def edit_meeting_in_meetings(previous_meeting: dict, edited_meeting: dict):
    meetings = get_meetings()
    meetings.update_one({'date': previous_meeting['date'],
                         'time': previous_meeting['time'],
                         'participants': previous_meeting['participants']},
                        {"$set": edited_meeting})


def delete_meeting_in_meetings(meeting: dict):
    meetings = get_meetings()
    meetings.delete_one(meeting)


def find_meeting_in_meetings(query: dict):
    meetings = get_meetings()
    return meetings.find_one(query)
