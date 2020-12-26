# setup_test_data.py
import random
import names
from django.contrib.auth import get_user_model
from tweets.models import Tweet
from accounts.models import UserProfile
from factories import UserFactory, TweetFactory

NUM_USERS = 500
NUM_TWEETS = 10000

User = get_user_model()
def handle():
    models = [User, Tweet]
    # Create all the users
    people = []
    for _ in range(NUM_USERS):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        random_number = str(random.randint(0, 100))
        person = UserFactory(username=first_name+last_name+random_number)
        people.append(person)

    # Create all the threads
    for _ in range(NUM_TWEETS):
        creator = random.choice(people)
        tweet = TweetFactory(user=creator)


handle()
