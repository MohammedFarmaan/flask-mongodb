from pymongo import MongoClient


# Create a MongoClient object
client = MongoClient('localhost', 27017)

# Access a specific database
db = client['feat']

employer_req_collection = db['employer_req']

def add_user(title, content):
    req_id = 28000
    user_dict ={
        "reqid": req_id+1,
        "title": title,
        "content": content
    } 
    employer_req_collection.insert_one(user_dict)

    return True
add_user("Ml app","flask,python")

employer_req_documents = employer_req_collection.find()
for employer_req_document in employer_req_documents:
    print(f"employer req: {employer_req_document}")


# result = user_collection.delete_one(document2)
# # Check if the deletion was successful
# if result.deleted_count == 1:
#     print("Document deleted successfully.")
# else:
#     print("No document matched the deletion condition.")