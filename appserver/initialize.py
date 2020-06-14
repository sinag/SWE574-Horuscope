import django
from django.conf import settings

from root.settings import DATABASES, INSTALLED_APPS, SERVER_ADDRESS, MIDDLEWARE, AUTH_USER_MODEL
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS, SERVER_ADDRESS=SERVER_ADDRESS, MIDDLEWARE=MIDDLEWARE, AUTH_USER_MODEL=AUTH_USER_MODEL)
django.setup()


from django.contrib.auth import get_user_model
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
from users.models import CustomUser
from follow.models import Follow


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
follows = Follow.objects.all()
users = CustomUser.objects.all()

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
for follow in follows:
    follow.delete()
for user in users:
    user.delete()


User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    # Community(name="Test Community Name", description="Test Community Description").save()

nyc_bikers_owner = CustomUser.objects.create_user(
    'scoofy',
    'scoofy@email.com',
    'scoofy',
    first_name="Mia",
    last_name="Sanderson",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_20_7E53C1.png"
)
nyc_bikers_post_1_author = CustomUser.objects.create_user(
    'welcometogoodburger7',
    'welcometogoodburger7@email.com',
    'welcometogoodburger7',
    first_name="Shirley",
    last_name="Underwood",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_08_7E53C1.png"
)
nyc_bikers_post_1_commenter = CustomUser.objects.create_user(
    'rbromblin',
    'rbromblin@email.com',
    'rbromblin',
    first_name="Amin",
    last_name="Wooten",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_08_A5A4A4.png"
)
nyc_bikers_post_2_author = CustomUser.objects.create_user(
    'myFach',
    'myFach@email.com',
    'myFach',
    first_name="Mariam",
    last_name="Whitmore",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_01_545452.png"
)
nyc_bikers_post_2_commenter_1 = CustomUser.objects.create_user(
    'SnarkyBehindTheStick',
    'SnarkyBehindTheStick@email.com',
    'SnarkyBehindTheStick',
    first_name="Nasir",
    last_name="Fuentes",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_18_7E53C1.png"
)
nyc_bikers_post_2_commenter_2 = CustomUser.objects.create_user(
    'stpeter666',
    'stpeter666@email.com',
    'stpeter666',
    first_name="Nasir",
    last_name="Fuentes",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_09_FF4500.png"
)
nyc_bikers_post_3_author = CustomUser.objects.create_user(
    'SometimesInBrooklyn',
    'SometimesInBrooklyn@email.com',
    'SometimesInBrooklyn',
    first_name="Shakil",
    last_name="Hampton",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_18_FF8717.png"
)

nyc_bikers_post_3_commenter_1 = CustomUser.objects.create_user(
    'bikeHikeNYC',
    'bikeHikeNYC@email.com',
    'bikeHikeNYC',
    first_name="Kristy",
    last_name="Osborne",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_06_46A508.png"
)
nyc_bikers_post_3_commenter_2 = CustomUser.objects.create_user(
    'Wellington27',
    'Wellington27@email.com',
    'Wellington27',
    first_name="Myles",
    last_name="Velez",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_20_A5A4A4.png"
)

nyc_bikers_post_4_author = CustomUser.objects.create_user(
    'giddythekidd',
    'giddythekidd@email.com',
    'giddythekidd',
    first_name="Angela",
    last_name="Donovan",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_01_0DD3BB.png"
)

nyc_bikers_post_4_commenter_1 = CustomUser.objects.create_user(
    'hashtagPLUR',
    'hashtagPLUR@email.com',
    'hashtagPLUR',
    first_name="Samson",
    last_name="Barrow",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_17_A5A4A4.png"
)

nyc_bikers_post_4_commenter_2 = CustomUser.objects.create_user(
    'Madgoat999',
    'Madgoat999@email.com',
    'Madgoat999',
    first_name="Joss",
    last_name="Fisher",
    bio="",
    profile_pic="https://www.redditstatic.com/avatars/avatar_default_03_545452.png"
)

animal_shelters_community = Community(
    name="Animal Shelters in İstanbul",
    description="An animal shelter info sharing platform for İstanbul. You can share information about the animal shelters nearby",
    author_id=nyc_bikers_post_1_author.id,
    city="İstanbul, Turkey"
)
animal_shelters_community.save()

animal_shelters_post_type = DataType(
    community_id=animal_shelters_community.id,
    author_id=nyc_bikers_post_1_author.id,
    name="Animal Shelters in İstanbul",
    description="Animal shelter locations and other information about them",
    generic=0
)
animal_shelters_post_type.save()

animal_shelters_post_type_title = Property(
    datatype_id=animal_shelters_post_type.id,
    author_id=nyc_bikers_post_1_author.id,
    name="Title",
    type=0,
    generic=1,
    required=True
)
animal_shelters_post_type_title.save()

animal_shelters_post_type_semantic_tags = Property(
    datatype_id=animal_shelters_post_type.id,
    author_id=nyc_bikers_post_1_author.id,
    name="Semantic Tags",
    type=0,
    generic=1,
    required=True
)
animal_shelters_post_type_semantic_tags.save()

animal_shelters_post_type_location = Property(
    datatype_id=animal_shelters_post_type.id,
    author_id=nyc_bikers_post_1_author.id,
    name="Location",
    type=9,
    generic=0,
    required=True
)
animal_shelters_post_type_location.save()

animal_shelters_post_type_content = Property(
    datatype_id=animal_shelters_post_type.id,
    author_id=nyc_bikers_post_1_author.id,
    name="Content",
    type=10,
    generic=0,
    required=False
)
animal_shelters_post_type_content.save()




animal_shelters_post_1 = Instance(datatype_id=animal_shelters_post_type.id, author_id=nyc_bikers_post_1_author.id)
animal_shelters_post_1.save()

TextField(
    value="İstanbul Şile Animal Shelter",
    instance_id=animal_shelters_post_1.id,
    property_id=animal_shelters_post_type_title.id
).save()

TextField(
    value="Q1411287-animal shelter,Q241631-Şile",
    instance_id=animal_shelters_post_1.id,
    property_id=animal_shelters_post_type_semantic_tags.id
).save()

TextField(
    value='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6007.897197667609!2d29.632068262946273!3d41.15747293000237!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x409e321185d42727%3A0xa21ef43eec59f31a!2zxLBzdGFuYnVsIMWeaWxlIFlvbHUgJiBBxJ92YSBDZC4sIEJhbGliZXksIDM0OTgwIMWeaWxlL8Swc3RhbmJ1bA!5e0!3m2!1str!2str!4v1592147073365!5m2!1str!2str" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    instance_id=animal_shelters_post_1.id,
    property_id=animal_shelters_post_type_location.id
).save()

TextField(
    value="They accept food, sunshade, cottage, water-food containers, antibiotics, vitamins and vaccines. They also need volunteers",
    instance_id=animal_shelters_post_1.id,
    property_id=animal_shelters_post_type_content.id
).save()

animal_shelters_post_2 = Instance(datatype_id=animal_shelters_post_type.id, author_id=nyc_bikers_post_2_author.id)
animal_shelters_post_2.save()

TextField(
    value="Güngören Municipality Animal Shelter",
    instance_id=animal_shelters_post_2.id,
    property_id=animal_shelters_post_type_title.id
).save()

TextField(
    value="Q1411287-animal shelter,Q932166-Güngören",
    instance_id=animal_shelters_post_2.id,
    property_id=animal_shelters_post_type_semantic_tags.id
).save()

TextField(
    value='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3009.8664788665274!2d28.870869115719277!3d41.02817702614844!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14cabada23e7d4f9%3A0x8aaf66e546ab3369!2zR2Vuw6dvc21hbiwgTXVzdGFmYSBZYcWfYXIgQ2QuLCAzNDE2NSBHw7xuZ8O2cmVuL8Swc3RhbmJ1bA!5e0!3m2!1str!2str!4v1592148224401!5m2!1str!2str" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    instance_id=animal_shelters_post_2.id,
    property_id=animal_shelters_post_type_location.id
).save()

TextField(
    value="They accept food, old newspapers, cardboards, blankets, parasitic drugs and vaccines.",
    instance_id=animal_shelters_post_2.id,
    property_id=animal_shelters_post_type_content.id
).save()








public_transport_community = Community(
    name="Public Transport in İstanbul",
    description="This is a community consisting of online reviews of forms of public transport. You can share your reviews about busses, train stations, airports, ferries, etc.",
    author_id=nyc_bikers_post_2_author.id,
    city="İstanbul, Turkey"
)
public_transport_community.save()

public_transport_post_type = DataType(
    community_id=public_transport_community.id,
    author_id=nyc_bikers_post_2_author.id,
    name="Public Transport Review",
    description="You can share your reviews about busses, train stations, airports, ferries, etc.",
    generic=0
)
public_transport_post_type.save()

public_transport_post_type_title = Property(
    datatype_id=public_transport_post_type.id,
    author_id=nyc_bikers_post_2_author.id,
    name="Title",
    type=0,
    generic=1,
    required=True
)
public_transport_post_type_title.save()

public_transport_post_type_semantic_tags = Property(
    datatype_id=public_transport_post_type.id,
    author_id=nyc_bikers_post_2_author.id,
    name="Semantic Tags",
    type=0,
    generic=1,
    required=True
)
public_transport_post_type_semantic_tags.save()

public_transport_post_type_image = Property(
    datatype_id=public_transport_post_type.id,
    author_id=nyc_bikers_post_2_author.id,
    name="Image",
    type=6,
    generic=0,
    required=False
)
public_transport_post_type_image.save()

public_transport_post_type_content = Property(
    datatype_id=public_transport_post_type.id,
    author_id=nyc_bikers_post_2_author.id,
    name="Content",
    type=10,
    generic=0,
    required=True
)
public_transport_post_type_content.save()

public_transport_post_2 = Instance(datatype_id=public_transport_post_type.id, author_id=nyc_bikers_post_4_author.id)
public_transport_post_2.save()

TextField(
    value="İETT bus driver was on the phone during the whole journey",
    instance_id=public_transport_post_2.id,
    property_id=public_transport_post_type_title.id
).save()

TextField(
    value="Q178512-public transport,Q1572846-Traffic",
    instance_id=public_transport_post_2.id,
    property_id=public_transport_post_type_semantic_tags.id
).save()

TextField(
    value="https://files.sikayetvar.com/complaint/1164/11645822/16d-numarali-otobus-soforu-yolculukta-telefonla-konusuyor-1.jpg",
    instance_id=public_transport_post_2.id,
    property_id=public_transport_post_type_image.id
).save()

TextField(
    value="İETT bus driver was on the phone during the whole journey. It is very strange to talk on the phone in a bus carrying so many passengers, even when talking is prohibited in cars.",
    instance_id=public_transport_post_2.id,
    property_id=public_transport_post_type_content.id
).save()

Comment(
    instance_id=public_transport_post_2.id,
    created_by_id=nyc_bikers_post_1_commenter.id,
    body="I think you should report him. Do you remember the licence plate?"
).save()

public_transport_post_1 = Instance(datatype_id=public_transport_post_type.id, author_id=nyc_bikers_post_3_author.id)
public_transport_post_1.save()

TextField(
    value="Social distancing(!) in public transport",
    instance_id=public_transport_post_1.id,
    property_id=public_transport_post_type_title.id
).save()

TextField(
    value="Q178512-public transport,Q81068910-COVID-19 pandemic",
    instance_id=public_transport_post_1.id,
    property_id=public_transport_post_type_semantic_tags.id
).save()

TextField(
    value="https://www.trthaber.com/resimler/1298000/1298589.jpg",
    instance_id=public_transport_post_1.id,
    property_id=public_transport_post_type_image.id
).save()

TextField(
    value="With the circular published yesterday by the Ministry of the Interior, it was announced that the number of passengers can be carried in public transportation vehicles is limited with the number of seats. According to the report of DHA, the driver of a van was fined, which has 10 passengers standing in the inspections in Kartal.",
    instance_id=public_transport_post_1.id,
    property_id=public_transport_post_type_content.id
).save()

Comment(
    instance_id=public_transport_post_1.id,
    created_by_id=nyc_bikers_post_1_commenter.id,
    body="This is sad.. People did have a really hard time putting up with the quarantine period, and now it seems all precautions are gone"
).save()




nyc_bikers_community = Community(
    name="NYCbike",
    description="A resource for NYC-specific cycling events and information. This is a great place to post and find group rides, questions about NYC cycling and bike shops, infrastructure changes, and cycling-related news. New to riding in the city? We'd love to help you get started!",
    author_id=nyc_bikers_owner.id,
    city="New York, NY, USA"
)
nyc_bikers_community.save()

nyc_bikers_post_type = DataType(
    community_id=nyc_bikers_community.id,
    author_id=nyc_bikers_owner.id,
    name="Cycling news and info for NYC",
    description="Cycling news and info for NYC",
    generic=0
)
nyc_bikers_post_type.save()

nyc_bikers_post_type_title = Property(
    datatype_id=nyc_bikers_post_type.id,
    author_id=nyc_bikers_owner.id,
    name="Title",
    type=0,
    generic=1,
    required=True
)
nyc_bikers_post_type_title.save()

nyc_bikers_post_type_semantic_tags = Property(
    datatype_id=nyc_bikers_post_type.id,
    author_id=nyc_bikers_owner.id,
    name="Semantic Tags",
    type=0,
    generic=1,
    required=True
)
nyc_bikers_post_type_semantic_tags.save()

nyc_bikers_post_type_image = Property(
    datatype_id=nyc_bikers_post_type.id,
    author_id=nyc_bikers_owner.id,
    name="Image",
    type=6,
    generic=0,
    required=False
)
nyc_bikers_post_type_image.save()

nyc_bikers_post_type_content = Property(
    datatype_id=nyc_bikers_post_type.id,
    author_id=nyc_bikers_owner.id,
    name="Content",
    type=10,
    generic=0,
    required=True
)
nyc_bikers_post_type_content.save()

nyc_bikers_post_1 = Instance(datatype_id=nyc_bikers_post_type.id, author_id=nyc_bikers_post_1_author.id)
nyc_bikers_post_1.save()

TextField(
    value="Midnight Rider",
    instance_id=nyc_bikers_post_1.id,
    property_id=nyc_bikers_post_type_title.id
).save()

TextField(
    value="Q11442-bicycle,Q36402-midnight",
    instance_id=nyc_bikers_post_1.id,
    property_id=nyc_bikers_post_type_semantic_tags.id
).save()

TextField(
    value="https://preview.redd.it/x2uny8hbai451.jpg?width=960&crop=smart&auto=webp&s=786e573d99bbd5d4f0cb2abc0a070bd4d788b88a",
    instance_id=nyc_bikers_post_1.id,
    property_id=nyc_bikers_post_type_image.id
).save()

TextField(
    value="Midnight rider is here!",
    instance_id=nyc_bikers_post_1.id,
    property_id=nyc_bikers_post_type_content.id
).save()

Comment(
    instance_id=nyc_bikers_post_1.id,
    created_by_id=nyc_bikers_post_1_commenter.id,
    body="This bridge is a close runner up to the Queensborough in the Most Blighted by Idiot New Cyclist category"
).save()


nyc_bikers_post_2 = Instance(datatype_id=nyc_bikers_post_type.id, author_id=nyc_bikers_post_2_author.id)
nyc_bikers_post_2.save()

TextField(
    value="From yesterday’s protest ride",
    instance_id=nyc_bikers_post_2.id,
    property_id=nyc_bikers_post_type_title.id
).save()

TextField(
    value="Q11442-bicycle,Q273120-protest,Q19600530-Black Lives Matter",
    instance_id=nyc_bikers_post_2.id,
    property_id=nyc_bikers_post_type_semantic_tags.id
).save()

TextField(
    value="https://preview.redd.it/tgg994yg8o451.jpg?width=640&crop=smart&auto=webp&s=c071509a3012bf45fb2830b8291e02a65ac2c715",
    instance_id=nyc_bikers_post_2.id,
    property_id=nyc_bikers_post_type_image.id
).save()

TextField(
    value="The rides have been super peaceful. There’s been almost no police interference. There were definitely some cases of them trying to bottleneck riders, but for the most part they’ve been helping block traffic here and there. I haven’t ever felt unsafe at any point the last 3 rides.",
    instance_id=nyc_bikers_post_2.id,
    property_id=nyc_bikers_post_type_content.id
).save()

Comment(
    instance_id=nyc_bikers_post_2.id,
    created_by_id=nyc_bikers_post_2_commenter_1.id,
    body="Did anyone from the @streetridersnyc ride capture Strava data of the ride? I’d love to see the route and distance we did!"
).save()

Comment(
    instance_id=nyc_bikers_post_2.id,
    created_by_id=nyc_bikers_post_2_commenter_2.id,
    body="i rode my nicer lockerupper and brought my usual things - phone, camera, etc - but kept them in a fannypack instead of handlebar dump pouch. avoid being right up front or right at the back. the cops didn't hassle anyone on the rides i've been on afaik."
).save()

nyc_bikers_post_3 = Instance(datatype_id=nyc_bikers_post_type.id, author_id=nyc_bikers_post_3_author.id)
nyc_bikers_post_3.save()

TextField(
    value="Two Bicyclists Killed In Separate Incidents In The Bronx",
    instance_id=nyc_bikers_post_3.id,
    property_id=nyc_bikers_post_type_title.id
).save()

TextField(
    value="Q11442-bicycle,Q9687-traffic collision",
    instance_id=nyc_bikers_post_3.id,
    property_id=nyc_bikers_post_type_semantic_tags.id
).save()

TextField(
    value="https://cms.prod.nypr.digital/images/306868/fill-661x496/",
    instance_id=nyc_bikers_post_3.id,
    property_id=nyc_bikers_post_type_image.id
).save()

TextField(
    value="Two bicyclists were killed by drivers in the span of a week in separate collisions that happened in the Mott Haven section of the Bronx.Around 7:45 p.m. June 5th, Ivan Morales, 23, was heading southbound on a bike lane on Willis Avenue when police said he slammed into a 2013 Lexus sedan driven by a 62-year-old man driving east on East 138th Street.",
    instance_id=nyc_bikers_post_3.id,
    property_id=nyc_bikers_post_type_content.id
).save()

Comment(
    instance_id=nyc_bikers_post_3.id,
    created_by_id=nyc_bikers_post_3_commenter_1.id,
    body="This is so sad and such an unnecessary loss of life. Double parked cars in the Bronx are a nightmare for cyclists, in and out of bike lanes. I have never seen a protected bike lane, although they probably exist in some areas."
).save()

Comment(
    instance_id=nyc_bikers_post_3.id,
    created_by_id=nyc_bikers_post_3_commenter_2.id,
    body="The Bronx is so tough for biking. It’s incredible how we lack just so much infrastructure. I bike as often as I can but it is very difficult to stay safe. This is awful."
).save()

nyc_bikers_post_4 = Instance(datatype_id=nyc_bikers_post_type.id, author_id=nyc_bikers_post_4_author.id)
nyc_bikers_post_4.save()

TextField(
    value="From the start of the blm bike protest in Brooklyn earlier today",
    instance_id=nyc_bikers_post_4.id,
    property_id=nyc_bikers_post_type_title.id
).save()

TextField(
    value="Q11442-bicycle,Q273120-protest,Q19600530-Black Lives Matter",
    instance_id=nyc_bikers_post_4.id,
    property_id=nyc_bikers_post_type_semantic_tags.id
).save()

TextField(
    value="https://preview.redd.it/fj94u6xeam451.jpg?width=960&crop=smart&auto=webp&s=6caec8f382cee2e21a7c24860eb1586d7f56c448",
    instance_id=nyc_bikers_post_4.id,
    property_id=nyc_bikers_post_type_image.id
).save()

TextField(
    value="I loved the guy on Fresh Pond filming his rap video in the middle of the street while everyone rode by.",
    instance_id=nyc_bikers_post_4.id,
    property_id=nyc_bikers_post_type_content.id
).save()

Comment(
    instance_id=nyc_bikers_post_4.id,
    created_by_id=nyc_bikers_post_4_commenter_1.id,
    body="Biking through the Hasidic neighborhood and some wartime bombing siren going off was quite the interesting scene. Amazing ride altogether, hope there will be another one"
).save()

Comment(
    instance_id=nyc_bikers_post_4.id,
    created_by_id=nyc_bikers_post_4_commenter_2.id,
    body="Is that what that was? I couldn't figure out what that constant siren was"
).save()


