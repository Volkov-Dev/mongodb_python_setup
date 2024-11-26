from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]  # Create or use an existing database
collection = db["my_collection"]  # Create or use an existing collection

# Insert data into MongoDB
data = {"name": "Chris", "age": 35, "profession": "Student"}
collection.insert_one(data)
print("Data successfully inserted!")

# Retrieve data from MongoDB
retrieved_data = collection.find_one({"name": "Chris"})
print("Retrieved Data:", retrieved_data)
