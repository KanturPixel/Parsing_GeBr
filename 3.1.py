from pprint import pprint
from pymongo import MongoClient
from get_vacancy import get_vacancy_info

MONGO_URL = "127.0.0.1:27017"
MONGO_DB = "vacancies"

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db["vacancies"]

def find_by_min_salary(collection, salary_min):
    result = collection.find({'salary_min': {"$gt": salary_min}},
                             {'_id': 0, 'input_website': 0})
    for item in result:
        pprint(item)

def find_by_salary(collection, salary_min, salary_max):
    result = collection.find({"$or": [
        {"$and": [{'salary_min': {"$gt": salary_min}}, {'salary_max': {"$gt": salary_max}}]},
        {"$and": [{'salary_min': {"$gt": salary_min}}, {'salary_max': {"$eq": None}}]},
        ]},
        {'_id': 0, 'input_website': 0})
    for item in result:
        pprint(item)

def insert_vacancies_to_db(collection, vacancy):
    print('Vacancies are loading...')
    vacancy_info = get_vacancy_info(vacancy)
    for item in vacancy_info:
        collection.update_many({'hyperlink': item['hyperlink']}),
        {'$set': item}, upsert=True)

    print('Vacancies loaded in database!')





