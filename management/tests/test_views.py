from django.test import TestCase
from django.urls import reverse

from .test_models import (RiskFieldTest, RiskFieldTypeTest, 
                        RiskTypeTest, RiskTest, RiskFieldTypeEnum,
                        Risk, RiskField, RiskFieldType, RiskType)

# Create your tests here.

def set_up_risk_test_data():
    RiskTest.setUpTestData()
    RiskTest.setUpTestData(client_name="PyDanny")

class MainViewTestCase(TestCase):
    def setUp(self):
        set_up_risk_test_data()
        # Setup run before every test method.

    def test_risk_list_is_displayed_on_main_view_template(self):
        response = self.client.get(reverse('index'))
        risk = response.context[0]['risks'].object_list
        self.assertTrue(len(risk), 2)
        self.assertTrue(risk[0].client_name, 'Peter Olayinka')
        self.assertTrue(risk[1].client_name, 'PyDanny')
        self.assertTrue(response.status_code, 200)

class RiskViewSet(TestCase):
    def setUp(self):
        set_up_risk_test_data()
        RiskFieldTest.setUpTestData()

    def enpoint_returns_a_list_of_all_risk(self):
        response = self.client.get(reverse('risk-list'))
        self.assertTrue(len(response.json()), 3)
        self.assertTrue(response.json(), [
            {'id': 1, 'risk_type': 
                {'name': 'Automobiles', 'id': 1}, 'client_name': 'Peter Olayinka', 
                'field': []},
            {'id': 2, 'risk_type': 
                {'name': 'Automobiles', 'id': 2}, 'client_name': 'PyDanny', 
                'field': []}, 
            {'id': 3, 'risk_type': 
                {'name': 'Automobiles', 'id': 3}, 'client_name': 'Peter Olayinka', 
                'field': [{'field_type': {'id': 1, 'name': 'Age', 'field': 'RiskFieldTypeEnum.NUMBER'},
                'risk': 3}]}])

    def test_endpoint_can_returns_a_single_risk(self):
        response = self.client.get(reverse('risk-detail', args=[3]))
        self.assertTrue(len(response.json()), 1)
        self.assertTrue(response.json(), [
            {'id': 3, 'risk_type': {'name': 'Automobiles', 'id': 3}, 'client_name': 'Peter Olayinka', 
            'field': [{'field_type': {'id': 1, 'name': 'Age', 'field': 'RiskFieldTypeEnum.NUMBER'}, 
            'risk': 3}]}])

    def test_endpoint_can_create_risk_from_valid_data(self):
        RiskFieldTypeTest.setUpTestData(name="Website", field=RiskFieldTypeEnum.URL)
        RiskFieldTypeTest.setUpTestData(name="Address", field=RiskFieldTypeEnum.TEXT)
        RiskTypeTest.setUpTestData()
        data = {
            "clientName": "Daniel Roy Greenfield",
            "fields": [
                {"field": 1, "value": "https://roygreenfield.com"}, 
                {"field": 2, "value": "I don't know, ask him!"}
            ],
            "riskType": 1
        }
        response = self.client.post(reverse('risk-list'), data,
                                content_type="application/json")
        self.assertTrue(response.json(), {"status", True})
        self.assertTrue(Risk.objects.count(), 1)
        self.assertTrue(RiskField.objects.count(), 2)
        self.assertTrue(RiskFieldType.objects.count(), 2)
        self.assertTrue(RiskType.objects.count(), 1)

