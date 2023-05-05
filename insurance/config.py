import pymongo
import pandas as pd
import numpy as np
import json
import os, sys
from dataclasses import dataclass



@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("mangodb_url")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "Response"
print(env_var.mongo_db_url)