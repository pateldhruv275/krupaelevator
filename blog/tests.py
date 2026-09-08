from django.test import TestCase, Client
from django.urls import reverse
from blog.models import BlogCategory, BlogPost


class BlogAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cat1 = BlogCategory.objects.create(
            name="Safety & Compliance",
            slug="safety-compliance",
            description="Elevator safety standards and IS codes"
        )
        self.cat2 = BlogCategory.objects.create(
            name="Technology & Innovation",
            slug="technology-innovation",
            description="PMSM and IoT smart lift tech"
        )

        self.post1 = BlogPost.objects.create(
            category=self.cat1,
            title="Understanding IS 14665 Standards",
            slug="understanding-is-14665-standards",
            author="Er. Sharma",
            summary="Key points of Indian Standard IS 14665 for elevator safety.",
            content="Detailed breakdown of elevator safety requirements and certifications...",
            reading_time=5,
            active=True
        )

        self.post2 = BlogPost.objects.create(
            category=self.cat2,
            title="Gearless PMSM Efficiency Benefits",
            slug="gearless-pmsm-efficiency-benefits",
            author="Krupa Engineering",
            summary="Why gearless PMSM elevators save up to 40% electricity.",
            content="Detailed analysis of permanent magnet synchronous motors...",
            reading_time=6,
            active=True
        )

        self.inactive_post = BlogPost.objects.create(
            category=self.cat1,
            title="Draft Safety Protocols",
            slug="draft-safety-protocols",
            summary="Work in progress draft.",
            content="Confidential internal notes...",
            active=False
        )

    def test_models_representation(self):
        self.assertEqual(str(self.cat1), "Safety & Compliance")
        self.assertEqual(str(self.post1), "Understanding IS 14665 Standards")
        self.assertEqual(self.cat1.post_count, 1)  # Only active posts counted
        self.assertEqual(self.cat1.get_absolute_url(), reverse('blog:category', kwargs={'slug': 'safety-compliance'}))
        self.assertEqual(self.post1.get_absolute_url(), reverse('blog:detail', kwargs={'slug': 'understanding-is-14665-standards'}))

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertContains(response, "Understanding IS 14665 Standards")
        self.assertContains(response, "Gearless PMSM Efficiency Benefits")
        self.assertNotContains(response, "Draft Safety Protocols")
        self.assertIn('posts', response.context)
        self.assertIn('categories', response.context)

    def test_blog_list_search(self):
        # Search for "PMSM"
        response = self.client.get(reverse('blog:list') + '?q=PMSM')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gearless PMSM Efficiency Benefits")
        self.assertNotContains(response, "Understanding IS 14665 Standards")

        # Search for non-matching query
        response_empty = self.client.get(reverse('blog:list') + '?q=NonExistentKeywordXYZ')
        self.assertEqual(response_empty.status_code, 200)
        self.assertContains(response_empty, "No blog posts matched your search query")

    def test_blog_list_pagination(self):
        # Create additional posts so total active > 6 (default page size is 6)
        for i in range(7):
            BlogPost.objects.create(
                category=self.cat1,
                title=f"Extra Safety Guide {i}",
                slug=f"extra-safety-guide-{i}",
                summary="Guide summary.",
                content="Guide content...",
                active=True
            )
        # Page 1
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_obj'].has_other_pages())
        self.assertEqual(len(response.context['posts']), 6)

        # Page 2
        response_p2 = self.client.get(reverse('blog:list') + '?page=2')
        self.assertEqual(response_p2.status_code, 200)
        self.assertEqual(len(response_p2.context['posts']), 3)  # 2 original + 7 new = 9 total; 9 - 6 = 3

    def test_blog_category_archive(self):
        response = self.client.get(reverse('blog:category', kwargs={'slug': 'safety-compliance'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertContains(response, "Understanding IS 14665 Standards")
        self.assertNotContains(response, "Gearless PMSM Efficiency Benefits")
        self.assertEqual(response.context['selected_category'], self.cat1)

    def test_blog_category_404(self):
        response = self.client.get(reverse('blog:category', kwargs={'slug': 'invalid-slug-category'}))
        self.assertEqual(response.status_code, 404)

    def test_blog_detail_view(self):
        initial_views = self.post1.views_count
        response = self.client.get(reverse('blog:detail', kwargs={'slug': self.post1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        self.assertContains(response, "Understanding IS 14665 Standards")
        self.assertContains(response, "Detailed breakdown of elevator safety")

        # Refresh from database and verify atomic view count increment
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.views_count, initial_views + 1)

    def test_blog_detail_404_on_invalid_or_inactive(self):
        # Non-existent slug
        response = self.client.get(reverse('blog:detail', kwargs={'slug': 'not-a-real-post'}))
        self.assertEqual(response.status_code, 404)

        # Inactive post should return 404 to public
        response_inactive = self.client.get(reverse('blog:detail', kwargs={'slug': self.inactive_post.slug}))
        self.assertEqual(response_inactive.status_code, 404)
