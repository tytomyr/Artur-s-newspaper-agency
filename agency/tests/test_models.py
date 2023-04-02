from django.contrib.auth import get_user_model
from django.test import TestCase
from agency.models import (Topic,
                           NewsPaper)


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_name"
        )
        self.assertEqual(
            str(topic),
            f"{topic.name}"
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            years_of_experience=1,
            username="test_username",
            password="test_password",
            first_name="Test",
            last_name="TestL"
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.first_name} {redactor.last_name}"
        )

    def test_article_str(self):
        topic = Topic.objects.create(
            name="test_name"
        )
        newspaper = NewsPaper.objects.create(
            title="test",
            topic=topic
        )

        self.assertEqual(str(newspaper), newspaper.title)
