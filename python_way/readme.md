# Client object
You will receive `client` type class as the return of connecting into mongoDB cluster.
```
client = pymongo.MongoClient("mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/{database_name}?retryWrites=true&w=majority")
```

<br/>

# Database object
To access database you can write
```
db = client.database_name
```
or
```
db = client["database_name"]
```
<br/>

# Collection object
Once you choose your database, then choose the collections name as well.
```
posts = db.posts
```
or
```
posts = db["posts"]
```

<br/>

# CRUD operations
The rest syntax is similar with the one in mongodb cmd, it is intuitive enough.
If in doubt, use `dir()` function to inspect the class attr and method.
```
dir(posts)
```