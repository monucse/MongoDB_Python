import pymongo

client = pymongo.MongoClient("mongodb+srv://KUSHI045:KuShi025@shivam.ueoblcw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db1 = client["My_info"]
coll = db1["Shivam"] 
coll1 = db1["Data_packet"] 
# record =  coll.find()
# for i in record:
#     print(i)

# coll.find({"companyName"})

# data =  coll.find({"companyName" : "iNeuron"})
# for i in data:
#     print(i)

data1 = coll.find({"courseOffered" : {"$gt": "E"}})
for i in data1:
    print(i)