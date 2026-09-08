from django.test import TestCase, Client
from django.urls import reverse
from gallery.models import GalleryCategory, GalleryImage


class GalleryTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.cat1 = GalleryCategory.objects.create(
            name="Cabin Interiors",
            slug="cabin-interiors",
            display_order=1
        )
        self.cat2 = GalleryCategory.objects.create(
            name="Installation Sites",
            slug="installation-sites",
            display_order=2
        )

        self.img1 = GalleryImage.objects.create(
            title="Gold Titanium Etched Cabin",
            category=self.cat1,
            description="Luxury stainless steel finishes",
            display_order=1,
            active=True
        )
        self.img2 = GalleryImage.objects.create(
            title="Shaft Hoistway Alignment",
            category=self.cat2,
            description="High precision laser shaft alignment",
            display_order=2,
            active=True
        )
        self.inactive_img = GalleryImage.objects.create(
            title="Draft Construction Image",
            category=self.cat2,
            active=False
        )

    def test_gallery_models(self):
        self.assertEqual(str(self.cat1), "Cabin Interiors")
        self.assertEqual(str(self.img1), "Gold Titanium Etched Cabin (Cabin Interiors)")

    def test_gallery_list_all(self):
        response = self.client.get(reverse('gallery:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery_list.html')
        self.assertEqual(len(response.context['images']), 2)
        self.assertContains(response, "Gold Titanium Etched Cabin")
        self.assertContains(response, "Shaft Hoistway Alignment")
        self.assertNotContains(response, "Draft Construction Image")

    def test_gallery_filter_by_category(self):
        response = self.client.get(reverse('gallery:list'), {'category': 'cabin-interiors'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['images']), 1)
        self.assertEqual(response.context['images'][0], self.img1)
        self.assertContains(response, "Gold Titanium Etched Cabin")
        self.assertNotContains(response, "Shaft Hoistway Alignment")

    def test_gallery_filter_invalid_category(self):
        response = self.client.get(reverse('gallery:list'), {'category': 'invalid-slug'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['images']), 2)
