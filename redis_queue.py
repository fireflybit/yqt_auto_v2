import json
import redis

class RedisQueue(object):
    def __init__(self, name):
        self.__db = redis.Redis(host="106.52.91.86", port=56379, db=0, password="nc_wuyuan")
        self.key = name

    def qsize(self):
        return self.__db.llen(self.key)

    def put(self, item):
        self.__db.rpush(self.key, item)

    def get_wait(self, timeout=None):
        item = self.__db.blpop(self.key, timeout=None)
        return item

    def get_nowait(self):
        item = self.__db.lpop(self.key)

    def serialize(self, item):
        return json.dumps(item, ensure_ascii=False)

    def deserialize(self, item):
        return json.loads(item)