from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

from tweets.models import Tweet
from accounts.models import UserProfile

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    # print(first_name)
    # random_number = random.randint(0, 2020)
    username = factory.Faker("first_name")


class TweetFactory(DjangoModelFactory):
    class Meta:
        model = Tweet

    user = factory.SubFactory(UserFactory)
    content = factory.Faker(
        "sentence",
        nb_words=10,
        variable_nb_words=True
    )