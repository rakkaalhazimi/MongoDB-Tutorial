import argparse
import pymongo


def connect_cluster(username, password):
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.0mxgk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return client
    

def count_element_type(collection, field, type_):
    return collection.count_documents({field: type_})


def get_unique_item(collection, field):
    return collection.distinct(field)


def get_aggregate_result(collection, pipelines):
    return collection.aggregate(pipelines)


if __name__ == "__main__":
    # Args
    parser = argparse.ArgumentParser(description="Connect into MongoDB Cluster.")
    parser.add_argument('--user', required=True, help='user name for mongodb')
    parser.add_argument('--password', required=True, help='password for mongodb')
    args = parser.parse_args()

    # DB and collection name
    database_name = "sample_airbnb"
    collection_name = "listingsAndReviews"

    client = connect_cluster(args.user, args.password)
    db = client[database_name]
    collection = db[collection_name]

    # Query
    ## Count and retrieve unique item
    print(count_element_type(collection, "bed_type", "Real Bed"))
    print(get_unique_item(collection, "bed_type"))

    # Aggregate
    ## Get all host's offering price and sort by the number of bedrooms
    pipelines = [
        {"$match": {}},
        {"$group": {"_id": "$host.host_name", "prices": {"$sum": "$price"}, "bedrooms": {"$max": "$bedrooms"}} },
        {"$sort": {"bedrooms": -1}}
    ]
    
    agg_results = get_aggregate_result(collection, pipelines)
    for item in agg_results:
        print(item)
