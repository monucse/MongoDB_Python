import pymongo

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


client = pymongo.MongoClient("mongodb+srv://KUSHI045:KuShi025@shivam.ueoblcw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["inventory"]
collection = database["table"]
# collection.insert_many(data)

# extract = collection.find()
# extract1 = collection.find({"status" : "A"})
# for i in extract1:
#     print(i)

# extract2 = collection.find({"status" : {"$in": ["A" , "P"] }})
# for i in extract2:
#     print(i)

# extract3 = collection.find({"status" : {"$gt" : "C"}})
# for i in extract3:
#     print(i)

# extract4 = collection.find({"qty" : {"$gte" : 75}})
# for i in extract4:
#     print(i)

# extract5 = collection.find({"qty" : {"$lte" : 95}})
# for i in extract5:
#     print(i)

# extract6 = collection.find({"item": "sketch pad","qty" : {"$lte" : 95}})
# for i in extract6:
#     print(i)

# collection.update_one({"item" : "canvas"}, {"$set" : {"item" : "Shivam Kumar"}})
# update_result = collection.find()
# for i in update_result:
#     print(i)

collection.delete_one({"item" : "Shivam Kumar"})
del_result = collection.find()
for i in del_result:
    print(i)