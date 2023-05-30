from pymongo import MongoClient


# Create a MongoClient object
client = MongoClient('localhost', 27017)

# Access a specific database
db = client['feat']

engaged_by_collection = db['engaged_by']

def engaged_by(req_id, engaged_by, status, web_link):
    user_dict ={
        "reqid": req_id,
        "engaged_by": engaged_by,
        "status": status,
        "web_link":web_link
    } 
    engaged_by_collection.insert_one(user_dict)

    return True
engaged_by(28001,18001,'started','https://github.com/tactlabs/prettymetrics')

engaged_by_documents = engaged_by_collection.find()
for engaged_by_document in engaged_by_documents:
    print(f"engaged by: {engaged_by_document}")


# result = user_collection.delete_one(document2)
# # Check if the deletion was successful
# if result.deleted_count == 1:
#     print("Document deleted successfully.")
# else:
#     print("No document matched the deletion condition.")