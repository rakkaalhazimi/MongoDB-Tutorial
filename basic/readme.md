# Create MongoDB Account


<br/>

# Connect into MongoDB Cluster
```
mongosh "mongodb+srv://cluster0.0mxgk.mongodb.net/myFirstDatabase" --apiVersion 1 --usertitle [usertitle]
```

<br/>

# Create and Use Database
```
use [database title]
```

<br/>

# Create collections
The database isn't actually created until we insert a data into it.
Collections are like tables in a SQL.
```
db.createCollection("my document")
```

<br/>

# Create collections on the fly
Instead of initialize collection creation first, we can create collections on the fly, by inserting the data inside predefined database.
```
db.posts.insertOne(object)
```
ex: db.posts.insertOne({
    "title": "post 1",
    "id": 1,
    "tag": "sport",
    "likes": 3,
    "body": "content"
})

<br/>

# Insert many object
Previously, we only insert single object. Now, we can also insert multiple objects, by using:
```
db.posts.insertMany(array[object])
```
ex: db.posts.insertMany([
{
    "title": "post 1",
    "id": 1,
    "tag": "sport",
    "likes": 3,
    "body": "content"
},
{
    "title": "post 2",
    "id": 2,
    "tag": "education",
    "likes": 1,
    "body": "content"
},
{
    "title": "post 3",
    "id": 3,
    "tag": "economics",
    "likes": 3,
    "body": "content"
},
{
    "title": "post 4",
    "id": 4,
    "tag": "sport",
    "likes": 1,
    "body": "content"
},
{
    "title": "post 5",
    "id": 5,
    "tag": "politics",
    "likes": 4,
    "body": "content"
}])

<br/>

# See All the Documents
```
db.posts.find()
```

<br/>

# Filter the documents by key, value
```
db.posts.find(object)
```
ex: db.posts.find({title: "post 1"})

<br/>

# Count the documents
```
db.posts.find(object).count()
```
ex: db.posts.find({title: "post 1"}).count()

<br/>

# Sort the documents by key
```
db.posts.find(object).sort({key: -1})  # 1 for ascending, -1 for descending
```
ex: db.posts.find({title: "post 1"}).sort({likes: -1})

<br/>

# Limit the find result
```
db.posts.find(object).limit(int)
```
ex: db.posts.find({title: "post 1"}).limit(2)

<br/>

# Find only one document
```
db.post.findOne(object)
```
ex: db.posts.findOne({title: "post 1"})

<br/>

# Find document by comparison (larger than, lower than, etc.)
```
db.posts.findOne({key: {$cond: int}})
```
ex: db.posts.findOne({likes: {$gt: 3}}) 
gt: greather than, lt: lower than

<br/>

# Update documents
This will change the entire document
```
db.posts.updateOne(object, new_object)
```
ex: db.posts.updateOne({title: "post 1"}, {title: "post first"})

<br/>

# Update only single category
We can instead change only single category and keep the rest
```
db.posts.updateOne(object, {$set: new_object})
``` 
ex: ex: db.posts.updateOne({title: "post 1"}, {$set: {title: "post first"}})

<br/>

# Update if it found and create if it not found
```
db.posts.updateOne(object, {$set: new_object}, {upsert: true})
```
ex: db.posts.updateOne(object, {$set: {title: "post 2", likes: 20}}, {upsert: true})

<br/>

# Increment document
```
db.posts.updateOne(object, {$inc: fields: int})
```
ex: db.posts.updateOne({title: "post 1"}, {$inc: likes: 2})

<br/>

# Increment all document
```
db.posts.updateMany({}, {$inc: fields: int})
```
ex: db.posts.updateMany({}, {$inc: likes: 2})

<br/>

# Delete single document
```
db.posts.deleteOne(object)
```
ex: db.posts.deleteOne({title: "post 1"})

<br/>

# Delete many document
```
db.posts.deleteMany(object)
```
ex: db.posts.deleteMany({tag: "sport"})


<br/>