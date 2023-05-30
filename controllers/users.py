from pymongo import MongoClient


# Create a MongoClient object
client = MongoClient('localhost', 27017)

# Access a specific database
db = client['feat']

user_collection = db['users']

def add_user(username, password):
    user_id = 18000
    user_dict ={
        "user_id": user_id+1,
        "username": username,
        "password": password
    } 
    user_collection.insert_one(user_dict)

    return True
add_user("kelly","test")

user_documents = user_collection.find()
for usr_document in user_documents:
    print(f"Users: {usr_document}")


# result = user_collection.delete_one(document2)
# # Check if the deletion was successful
# if result.deleted_count == 1:
#     print("Document deleted successfully.")
# else:
#     print("No document matched the deletion condition.")