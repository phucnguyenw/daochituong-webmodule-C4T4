from matplotlib import pyplot
from mongoengine import *
import mlab
class Customers(Document):
    name=StringField()
    age=IntField()
    address=StringField()
    ref=StringField()
 

mlab.connect()
ads_count=len(Customers.objects(ref__icontains="ads"))
event_count=len(Customers.objects(ref__icontains="event"))
wom_count=len(Customers.objects(ref__icontains="wom"))

percentage=[ads_count,event_count,wom_count]
#print(percentage)

refs=["Advertisements","Events","Words of mouths"]

pyplot.pie(percentage,labels = refs, autopct = "%.1f%%", shadow=True, explode=[0,0.1,0.15])
pyplot.axis("equal")

pyplot.show()