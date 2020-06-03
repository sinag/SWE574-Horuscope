# exec(open('clean_database.py').read())
from activitystream.models import ActivityStream
from comment.models import Comment
from community.models import Community
from datatype.models import DataType
from datetimefield.models import DateTimeField
from flag.models import Flag
from instance.models import Instance
from integerfield.models import IntegerField
from property.models import Property
from subscription.models import Subscription
from textfield.models import TextField

textfields = TextField.objects.all()
integerfields = IntegerField.objects.all()
datetimefields = DateTimeField.objects.all()
properties = Property.objects.all()
subcriptions = Subscription.objects.all()
comments = Comment.objects.all()
instances = Instance.objects.all()
datatypes = DataType.objects.all()
flags = Flag.objects.all()
communities = Community.objects.all()
activitystreams = ActivityStream.objects.all()

for subcription in subcriptions:
    subcription.delete()
for flag in flags:
    flag.delete()
for comment in comments:
    comment.delete()
for textfield in textfields:
    textfield.delete()
for integerfield in integerfields:
    integerfield.delete()
for datetimefield in datetimefields:
    datetimefield.delete()
for property in properties:
    property.delete()
for instance in instances:
    instance.delete()
for datatype in datatypes:
    datatype.delete()
for community in communities:
    community.delete()
for activitystream in activitystreams:
    activitystream.delete()


