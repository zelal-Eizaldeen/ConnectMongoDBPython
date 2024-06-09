#MongoDB driver
import pymongo
#Making connection to MongoDB
conn=pymongo.MongoClient()
print("Connected to MongoDB")
db=conn.fridaynight


#Query Beers table
Q1=db.Beers.find({"brewer": "AB InBev"},{"name":1})
#Query Sells table
Q2=db.Sells.find({"price": {"$lt":5}}, {"beer":1})
print("** Results of Q1:")

for d1 in Q1:
    name=d1["name"]
    print(name)
print("** Results of Q2:")
for d2 in Q2:
    beer=d2["beer"]
    print(beer)

######Intersection#######
results=[]
print("** Intersection:")
for d1 in Q1.rewind():
    for d2 in Q2.rewind():
        if (d1["name"]== d2["beer"] and d1["name"] not in results):
            results.insert(0, d1["name"])
            print(d1["name"])

######Union#######
results=[]
print("** Union:")
for d1 in Q1.rewind():
    if (d1["name"] not in results):
        results.insert(0, d1["name"])
        print(d1["name"])
for d2 in Q2.rewind():
    if (d2["beer"] not in results):
        results.insert(0, d2["beer"])
        print(d2["beer"])
