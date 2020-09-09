#!/usr/bin/env python3
""" update topics module
"""


def update_topics(mongo_collection, name, topics):
    """ Python function that changes all topics of a
        school document based on the name
    """
    return mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
