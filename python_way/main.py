import argparse
import pymongo


def connect_cluster(username, password):
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.0mxgk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # db = client.test
    return client


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect into MongoDB Cluster.")
    parser.add_argument('--user', required=True, help='user name for mongodb')
    parser.add_argument('--password', required=True, help='password for mongodb')

    args = parser.parse_args()

    client = connect_cluster(args.user, args.password)