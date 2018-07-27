from mongoengine import *
import mlab  
class Posts(Document):
    title=StringField()
    author=StringField()
    content=StringField()
mlab.connect()

post=Posts(title="Test 2",author="Anon",content="Roses are red. I want a tent. Thanos snaps. Suicide rate is now 50%")
post.save()


