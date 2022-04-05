import pymongo

def connect_local():
    client = pymongo.MongoClient("localhost:27017")
    return client


if __name__ == "__main__":
    client = connect_local()