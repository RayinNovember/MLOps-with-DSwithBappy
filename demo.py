# import os
# mongo_db_url = os.getenv('mongodb_url')
# print(mongo_db_url)
# from us_visa.configuration.mongo_db_connection import MongoDBClient
# test = MongoDBClient()

# from us_visa.constants import *
# import os
# import pymongo
# import certifi
# ca = certifi.where()


# print(os.getenv("mongodb_url"))
# print("mongodb+srv://wangchangrui1815:Raywang8442!@cluster0.y4ggqf2.mongodb.net/?appName=Cluster0")

# mongo_db_url = os.getenv("mongodb_url").strip().strip('"').strip("'")
# client = pymongo.MongoClient(mongo_db_url)
#client = pymongo.MongoClient("mongodb+srv://wangchangrui1815:Raywang8442!@cluster0.y4ggqf2.mongodb.net/?appName=Cluster0")

from us_visa.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()