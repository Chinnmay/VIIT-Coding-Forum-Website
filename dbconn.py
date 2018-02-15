import os
import pprint

from pymongo import MongoClient


def get_summaries_by_domain(domain=None):
	final_json = dict()
	try:
		client = MongoClient(os.environ['VIIT_CODING_FORUM_MONGO_URL'])
		db = client.heroku_ntl5gcw6
		collection = db.discussions
		if domain is None:
			cur = collection.find({}, {"_id": 0, "description": 0, "forum": 0})
		else:
			cur = collection.find({"domains":domain}, {"_id":0, "description":0, "forum":0})
		count = 1
		for doc in cur:
			final_json["result_"+str(count)] = doc
			count = count+1
		# pprint.pprint(final_json)
		client.close()
	except:
		final_json['status'] = False
	return final_json


def get_full_details(ID):
	final_json = dict()
	try:
		client = MongoClient(os.environ['VIIT_CODING_FORUM_MONGO_URL'])
		db = client.heroku_ntl5gcw6
		collection = db.discussions
		cur = collection.find({"ID": ID}, {"_id": 0})
		# pprint.pprint(cur)
		for doc in cur:
			final_json = doc
		# pprint.pprint(final_json)
		client.close()
	except:
		final_json['status'] = False
		print("Failed")
	return final_json

def add_question(ID, question):
	try:
		client = MongoClient(os.environ['VIIT_CODING_FORUM_MONGO_URL'])
		db = client.heroku_ntl5gcw6
		collection = db.discussions
		doc = get_full_details(ID)
		question_list = doc['forum']
		max = 0
		for ques in question_list:
			if max < ques['question_id']:
				max = ques['question_id']
		max = max+1
		cur = collection.update({"ID": ID}, {"$push":{"forum":{"question_id":max, "question":question, "comments":[]}}})
		client.close()
		return True
	except:
		return False


# print(add_question(111,"Question from Python"))
# get_full_details(111)
