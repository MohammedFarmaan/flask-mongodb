from pymongo import MongoClient


# Create a MongoClient object
client = MongoClient('localhost', 27017)

# Access a specific database
db = client['feat']

employer_collection = db['employers']

def add_user(username, password):
    user_id = 18000
    user_dict ={
        "userid": user_id+1,
        "username": username,
        "password": password
    } 
    employer_collection.insert_one(user_dict)

    return True
add_user("kelly","test")

emp_documents = employer_collection.find()
for usr_document in emp_documents:
    print(f"Users: {usr_document}")

# result = employer_collection.delete_one(document2)
# # Check if the deletion was successful
# if result.deleted_count == 1:
#     print("Document deleted successfully.")
# else:
#     print("No document matched the deletion condition.")