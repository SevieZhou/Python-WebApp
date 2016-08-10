import orm
import asyncio
import sys
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='azsxdc123', db='awesome')
    u = User(name='test7788',email='test77@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)