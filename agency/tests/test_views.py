from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, NewsPaper

REDACTORS_URL = reverse("agency:redactor-list")
NEWSPAPERS_URL = reverse("agency:newspaper-list")
TOPICS_URL = reverse("agency:topic-list")
REDACTORS_DETAIL_URL = reverse("agency:newspaper-detail",
                               kwargs={"pk": 1})
NEWSPAPERS_DETAIL_URL = reverse("agency:newspaper-detail",
                                kwargs={"pk": 1})


class PublicViewTests(TestCase):
    def test_list_login_required_list(self):
        tests = [REDACTORS_URL, NEWSPAPERS_URL, TOPICS_URL]
        for test in tests:
            res = self.client.get(test)
            self.assertNotEqual(res.status_code, 200)

    def test_detail_login_required_list(self):
        tests = [
            REDACTORS_DETAIL_URL,
            NEWSPAPERS_DETAIL_URL
        ]
        for test in tests:
            res = self.client.get(test)
            self.assertNotEqual(res.status_code, 200)


class PrivateViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password"
        )
        self.client.force_login(self.user)

    def test_logged_in_page_view(self):
        topic = Topic.objects.create(
            name="Crime"
        )
        NewsPaper.objects.create(
            title="Assassination",
            topic=topic
        )
        tests = [
            self.client.get(TOPICS_URL),
            self.client.get(NEWSPAPERS_URL)
        ]

        for test in tests:
            self.assertEqual(test.status_code, 200)

    def test_topic_create(self):
        self.assertEqual(Topic.objects.count(), 0)

        topic_data = {
            "name": "Sports",
        }
        create_url = reverse("agency:topic-create")
        response = self.client.post(create_url, topic_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(Topic.objects.first().name, "Sports")

    def test_newspaper_delete(self):
        topic = Topic.objects.create(name="Politics")
        newspaper = NewsPaper.objects.create(title="Headline", topic=topic)

        self.assertEqual(NewsPaper.objects.count(), 1)

        delete_url = reverse("agency:topic-delete", kwargs={"pk": topic.pk})
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(NewsPaper.objects.count(), 0)
