import json
import pymongo

#file path to open and insert data in the collectionhttps://github.com/sarathkumar1304/students-db
with open("/Users/ELCOT/Downloads/students (1).json", 'r') as f:
    data = json.load(f)

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["studentsdatabase1"]
mycol = mydb["students_info1"]
# mycol.insert_many(data)

# 1find the student name who scored maximum scores in all exam quiz and homework
print("--* 1.student scored maximum score in all categories like exam,quiz and homework *--")
lst_marks=[]
for i in mycol.find():
    total=0
    for j in range(len(i['scores'])):
        total=total+i['scores'][j]['score']
    lst_marks.append(total)
    #print(i['_id'],total)
    mycol.update_one({"_id":i['_id']},{"$set":{"total":total}})

for i in mycol.find():
   if(i['total']==max(lst_marks)):
        print(i)
        break

# 2 find students who scored below average in the "exam" and pass mark is 40%
print("--* 2.student scored below average in the exam and pass mark is 40% *--")

for i in mycol.find():
    if (i['scores'][0]['score']<40):
        print(i)

#3.Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories.
for i in mycol.find():
    if (i['scores'][0]['score']>=40 and i['scores'][1]['score']>=40 and i['scores'][2]['score']>=40):
        mycol.update_one({"_id":i["_id"]},{"$set":{"Result":"pass"}})
    else:
        mycol.update_one({"_id":i['_id']},{"$set":{"Result":"Fail"}})
    print(i)

#Find the total and average of the exam, quiz and homework and store them in a separate collection.
mycol4=mydb["Ques-4"]
lst_exam_marks=[]
lst_quiz_marks=[]
lst_hw_marks=[]

for i in mycol.find():
    lst_exam_marks.append(i['scores'][0]['score'])
    lst_quiz_marks.append(i['scores'][1]['score'])
    lst_hw_marks.append(i['scores'][2]['score'])

avg_exam=sum(lst_exam_marks)/len(lst_exam_marks)
avg_quiz=sum(lst_quiz_marks)/len(lst_quiz_marks)
avg_hw=sum(lst_hw_marks)/len(lst_hw_marks)
data={
    'all_marks' :[{'sum_exam_mk': sum(lst_exam_marks)},{'sum_quiz_mk' :sum(lst_quiz_marks)},{'sum_hw_mk' :sum(lst_hw_marks)}],
    'all_marks_avg' :[{'avg_exam' :avg_exam},{'avg_quiz' :avg_quiz},{'avg_hw' :avg_hw}]
       }
#print(data)

#mycol4.insert_one(data)
for i in mycol4.find():
    print(i)

#5)Create a new collection which consists of students who scored below average and above 40% in all the categories.
print("5 answer")
mycol5=mydb["Ques-5"]
avg_of_total=sum(lst_marks)/len(lst_marks)
avg_of_total

for i in mycol.find():

    if (i['scores'][0]['score']>=40 and i['scores'][1]['score']>=40 and i['scores'][2]['score']>=40 and i['total']< avg_of_total):
        print(i)
        #mycol5.insert_one(i)
for m in mycol5.find():
    print(m)

#6)Create a new collection which consists of students who scored below the fail mark in all the categories
mycol6=mydb["Ques-6"]
for i in mycol.find():
    if(i['scores'][0]['score']<40 and i['scores'][1]['score']<40 and i['scores'][2]['score']<40):
        #print(i)
        #mycol6.insert_one(i)
        print(i)
for k in mycol6.find():
    print(k)

#7Create a new collection which consists of students who scored above pass mark in all the categories.
mycol7=mydb["Ques-7"] #create a collection
for i in mycol.find():
    if(i['scores'][0]['score']>40 and i['scores'][1]['score']>40 and i['scores'][2]['score']>40 ):
        print(i)
        #mycol7.insert_one(i)
for j in mycol7.find():
    print(j)