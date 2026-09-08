from django.test import TestCase, Client
from django.urls import reverse
from products.models import ProductCategory, Product, ProductImage


class ProductsAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = ProductCategory.objects.create(
            name="Passenger Elevator",
            slug="passenger-elevator",
            short_description="High-speed passenger transit",
            description="Complete engineering description for passenger lifts.",
            icon="bi-person-walking",
            active=True,
            display_order=1
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Gearless Passenger Lift",
            slug="gearless-passenger-lift",
            short_description="Smart PMSM gearless elevator",
            description="In-depth details for gearless passenger lift.",
            capacity="8 Persons (544 kg)",
            speed="1.5 m/s",
            machine_type="PMSM Gearless",
            drive_type="Closed-Loop V3F",
            features="Multi-beam infrared curtain\nAutomatic rescue device (ARD)\nOverload indicator",
            technical_specifications="Drive: V3F Microprocessor\nBraking: Dual Disc Calipers",
            finishes="Hairline SS 304\nTitanium Gold",
            featured=True,
            active=True,
            display_order=1
        )

    def test_category_and_product_str(self):
        self.assertEqual(str(self.category), "Passenger Elevator")
        self.assertIn("Gearless Passenger Lift", str(self.product))
        self.assertEqual(self.category.product_count, 1)

    def test_product_helper_methods(self):
        features = self.product.get_features_list()
        self.assertEqual(len(features), 3)
        self.assertIn("Automatic rescue device (ARD)", features)

        finishes = self.product.get_finishes_list()
        self.assertEqual(len(finishes), 2)
        self.assertIn("Hairline SS 304", finishes)

        specs = self.product.get_specs_list()
        self.assertEqual(len(specs), 2)
        self.assertEqual(specs[0], ("Drive", "V3F Microprocessor"))

    def test_product_list_view(self):
        res = self.client.get(reverse('products:list'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'products/product_list.html')
        self.assertContains(res, "Passenger Elevator")
        self.assertContains(res, "Gearless Passenger Lift")

    def test_product_list_search_and_filter(self):
        # Filter by category
        res = self.client.get(reverse('products:list') + '?category=passenger-elevator')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Gearless Passenger Lift")

        # Search query matching
        res_search = self.client.get(reverse('products:list') + '?q=gearless')
        self.assertEqual(res_search.status_code, 200)
        self.assertContains(res_search, "Gearless Passenger Lift")

        # Search query non-matching
        res_empty = self.client.get(reverse('products:list') + '?q=nonexistentlift')
        self.assertEqual(res_empty.status_code, 200)
        self.assertContains(res_empty, "No Elevator Models Match Your Selection")

    def test_category_detail_view(self):
        url = reverse('products:category_detail', kwargs={'slug': 'passenger-elevator'})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'products/category_detail.html')
        self.assertContains(res, "Passenger Elevator")
        self.assertContains(res, "Gearless Passenger Lift")

    def test_product_detail_view(self):
        url = reverse('products:detail', kwargs={'category_slug': 'passenger-elevator', 'slug': 'gearless-passenger-lift'})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'products/product_detail.html')
        self.assertContains(res, "Gearless Passenger Lift")
        self.assertContains(res, "544 kg")
        self.assertContains(res, "PMSM Gearless")
        self.assertContains(res, "Automatic rescue device (ARD)")

    def test_product_direct_slug_routing(self):
        # When accessing category slug directly under /products/
        res_cat = self.client.get('/products/passenger-elevator/')
        self.assertEqual(res_cat.status_code, 200)
        self.assertTemplateUsed(res_cat, 'products/category_detail.html')

        # When accessing product slug directly under /products/
        res_prod = self.client.get('/products/gearless-passenger-lift/')
        self.assertEqual(res_prod.status_code, 302)
        self.assertEqual(res_prod.url, '/products/passenger-elevator/gearless-passenger-lift/')
