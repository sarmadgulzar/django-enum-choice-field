from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


class Color2RGBAPIViewTest(TestCase):
    def test_color_2_rgb(self):
        url = reverse("color2rgb")
        payload = {"color": "BLUE"}
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertDictEqual(response.json(), {"rgb": [0, 0, 255]})
