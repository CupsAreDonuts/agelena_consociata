import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['social_database']
mycol = mydb['people']
