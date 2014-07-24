
import json
import redis

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT)


class NanoblogPost():
    REDIS_LIST_KEY = 'nanoblog-posts'

    def __init__(self, title, body):
        self.title = title
        self.body = body

    @staticmethod
    def iter_all():
        posts = client.lrange(
            NanoblogPost.REDIS_LIST_KEY,
            0, -1)
        for post in posts:
            yield NanoblogPost(**json.loads(post))

    def addtodb(self):
        value = json.dumps(
            {'title': self.title,
             'body': self.body}
        )
        client.lpush(self.REDIS_LIST_KEY, value)
