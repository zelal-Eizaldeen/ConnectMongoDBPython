#MongoDB driver
import pymongo
#Making connection to MongoDB
conn=pymongo.MongoClient()
print("Connected to MongoDB")

db=conn.fridaynight
#Query Beers table
print("** Beers:")
for x in db.Beers.find():
  print(x)