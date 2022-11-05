import pymongo

'''defitition used to inser data from mongo db'''
def insert():
    name = input("enter your name")
    place = input("enter your place")
    gender = input("enter your gender")
    phone_number = input("enter your phone_number")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["telephone"]
    mycol = mydb["directory"]
    mydict = {"name": f'{name}',
            "place": f'{place}',
            "gender": f'{gender}',
            "phone_number": f'{phone_number}'
               }
    x = mycol.insert_one( mydict)
 
'''definition used to read or retrive data from database'''
def retrive():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["telephone"]
    mycol = mydb["directory"]
    for x in mycol.find():
        print(x)
        
'''definition used to update already entered data and new feild to add to data'''       
def update():
    old_index = input("enter your  old_index like name ,gender,place,mobile_number")
    old_data=input("enter old data ")
    update_index = input("enter your  index like name ,gender,place,mobile_number")
    update_data=input("enter your data to update")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["telephone"]
    mycol = mydb["directory"]
    old_querey={(f'{old_index}'):f'{old_data}'}
    myquerey={"$set":{(f'{update_index}'):f'{update_data}'}}
    mycol.update_one(old_querey,myquerey)
    print(f"{update_data}has been updated successfully")
    
'''definition used to delete the data from database'''    
def delete():
    delete_index = input("enter your delete index like name ,gender,place")
    delete_data = input("enter your data to delete")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["telephone"]
    mycol = mydb["directory"]
    x=mycol.delete_one({f'{delete_index}':f'{delete_data}'})
    for x in mycol.find():
        print(x)
    print(f"has been deleted successfully")
    
'''get value to call the definition'''    
print("WELCOME TO TELEPHONE DIRECTORY")
print("enter 1 to insert data")
print("enter 2 to retrive data")
print("enter 3 to update data")
print("enter 4 to delete data")
option=int(input("enter here..."))
if option==1:
       insert()
if option==2:
    retrive()
if option == 3:
    update()
if option == 4:
    delete()

