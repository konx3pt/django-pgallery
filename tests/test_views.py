from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser

from djet.testcases import ViewTestCase

from pgallery.views import GalleryListView, TaggedPhotoListView
from .factories import GalleryFactory, UserFactory


class GalleryListViewTestCase(ViewTestCase):
    view_class = GalleryListView

    def test_draft_invisible(self):
        gallery = GalleryFactory(status='draft', title="Draft gallery")
        request = self.factory.get(user=AnonymousUser())
        response = self.view(request)
        self.assertNotContains(response, gallery.title)

    def test_draft_visible_for_staff(self):
        gallery = GalleryFactory(status='draft', title="Draft gallery")
        user = UserFactory(is_staff=True)
        request = self.factory.get(user=user)
        response = self.view(request)
        self.assertContains(response, gallery.title)


class TaggedPhotoListViewTestCase(ViewTestCase):
    view_class = TaggedPhotoListView

    def test_tag_in_response(self):
        request = self.factory.get()
        response = self.view(request, tag='example_tag')
        self.assertContains(response, 'example_tag')
