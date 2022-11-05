import  json
import pymongo

'''insert jason file of data into mongodb data base'''

with open("C:/Users/Star World/Downloads/student.json") as file:
  data = file.read()
  y=json.loads(data)
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = client["mydatabase1"]
  mycol = mydb["customers4"]
  x=mycol.insert_many(y)
  for x in mycol.find():
    print(x)

  """1)      Find the student name who scored maximum scores in all (exam, quiz and homework)?
"""
  print("max mark in all subject")
  myquery={'scores.0.score':{"$gt":90},'scores.1.score':{"$gt":90},'scores.2.score':{"$gt":90}}
  for i in mycol.find(myquery):
   print(i)

  '''2)      Find students who scored below average in the exam and pass mark is 40%?'''
  myquery1 = {'scores.0.score': {"$lte": 50}}
  for b in mycol.find(myquery1):
   print(b)

  '''3)      Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories.'''

  #fail mark
  myquery2 = {'scores.score': {"$lt": 40}}
  myquery3 = {"$set": {"grade": "fail"}}
  c1 = mycol.update_many(myquery2, myquery3)
  for c1 in mycol.find():
    print(c1)

  #pass mark

  myquery2 = {'scores.0.score': {"$gt": 40}, 'scores.1.score': {"$gt": 40}, 'scores.2.score': {"$gt": 40}}
  myquery3 = {"$set": {"grade": "pass"}}
  c = mycol.update_many(myquery2, myquery3)
  for c in mycol.find():
    print(c)

  '''4)       Find the total and average of the exam, quiz and homework and store them in a separate collection.'''
  for m in mycol.aggregate([{"$project": {"_id": 1, 'name': '$name', 'totalmark': {"$sum": "$scores.score"},
                                          "average": {"$avg": "$scores.score"}}}]):
    print(m)

  '''5)      Create a new collection which consists of students who scored below average and above 40% in all the categories.'''

  myquery2 = {'scores.0.score': {"$gte": 40, "$lte": 50}, 'scores.1.score': {"$gte": 40, "$lte": 50},
              'scores.2.score': {"$gte": 40, "$lte": 50}}
  for e in mycol.find(myquery2):
    print(e)
    client1 = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb1 = client1["mydatabase1"]
    mycol1 = mydb["customers5"]
    y = mycol1.insert_many([e])
    for f in mycol1.find():
     print(f)

  '''6) Create a new collection which consists of students who scored below the fail mark in all the categories.'''

  myquery = {'scores.0.score': {"$lt": 40}, 'scores.1.score': {"$lt": 40}, 'scores.2.score': {"$lt": 40}}
  for l in mycol.find(myquery):
    print(l)
    client1 = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb1 = client1["mydatabase1"]
    mycol1 = mydb["customers6"]
    z = mycol1.insert_many([l])
    for z in mycol1.find():
      print(z)

  '''7) Create a new collection which consists of students who scored above pass mark in all the categories.'''

  myquery = {'scores.0.score': {"$gte": 40}, 'scores.1.score': {"$gte": 40}, 'scores.2.score': {"$gte": 40}}
  for k in mycol.find(myquery):
    print(k)
    client1 = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb1 = client1["mydatabase1"]
    mycol1 = mydb["customers7"]
    u = mycol1.insert_many([k])
    for y in mycol1.find():
      print(u)
