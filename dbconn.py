import os
import pprint
import logging
import pymongo
from pymongo import MongoClient
from datetime import datetime

def get_summaries_by_domain(domain=None):
	final_json = dict()
	try:
		client = MongoClient(os.environ['VIIT_CODING_FORUM_MONGO_URL'])
		db = client.heroku_ntl5gcw6
		collection = db.discussions

		if domain is None:
			cur = collection.find({"date":{"$gte":datetime.utcnow()}}, {"_id": 0, "description": 0, "forum": 0}).sort([("date", pymongo.ASCENDING)])
		else:
			cur = collection.find({"domains":domain, "date":{"$gte":datetime.utcnow()}}, {"_id":0, "description":0, "forum":0}).sort([("date", pymongo.ASCENDING)])
		l1 = list()
		for doc in cur:
			l1.append(doc)
		client.close()
	except:
		logging.exception("message")
		return False
	if len(l1)==0:
		return "No results"
	else:
		return l1


def get_full_details(ID):
	final_json = dict()
	try:
		client = MongoClient(os.environ['VIIT_CODING_FORUM_MONGO_URL'])
		db = client.heroku_ntl5gcw6
		collection = db.discussions
		cur = collection.find({"ID": ID}, {"_id": 0})
		for doc in cur:
			final_json = doc
		client.close()
	except:
		final_json['status'] = False
		print("Failed")
	return final_json
