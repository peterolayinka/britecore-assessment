from django.test import TestCase

from management.models import RiskType, RiskField, RiskFieldType, Risk, RiskFieldTypeEnum
# Create your tests here.

class RiskTypeTest(TestCase):
    @classmethod
    def setUpTestData(cls, name="Automobiles"):
        return RiskType.objects.create(name=name)

    def test_risk_name_label(self):
        risk_type = RiskType.objects.get(id=1)
        field_label = risk_type._meta.get_field('name').verbose_name
        self.assertTrue(field_label, 'name')

class RiskFieldTypeTest(TestCase):
    @classmethod
    def setUpTestData(cls, name="Age", field=RiskFieldTypeEnum.NUMBER):
        return RiskFieldType.objects.create(name=name, field=field)

    def test_risk_field_type_name_label(self):
        risk_field_type = RiskFieldType.objects.get(id=1)
        field_label = risk_field_type._meta.get_field('name').verbose_name
        self.assertTrue(field_label, 'name')

    def test_risk_field_type_field_label(self):
        risk_field_type = RiskFieldType.objects.get(id=1)
        field_label = risk_field_type._meta.get_field('field').verbose_name
        self.assertTrue(field_label, 'field')

class RiskTest(TestCase):
    @classmethod
    def setUpTestData(cls, client_name="Peter Olayinka"):
        risk_type = RiskTypeTest.setUpTestData()
        return Risk.objects.create(client_name=client_name, risk_type=risk_type)

    def test_risk_label(self):
        risk = Risk.objects.get(id=1)
        risk_type = RiskType.objects.get(id=1)
        field_label = risk._meta.get_field('client_name').verbose_name
        self.assertTrue(field_label, 'client name')

class RiskFieldTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        risk = RiskTest.setUpTestData()
        risk_field_type = RiskFieldTypeTest.setUpTestData()
        return RiskField.objects.create(field_type=risk_field_type, risk=risk, value="23")

    def test_risk_label(self):
        risk_field = RiskField.objects.get(id=1)
        risk_type = RiskType.objects.get(id=1)
        field_label = risk_field._meta.get_field('value').verbose_name
        self.assertTrue(field_label, 'value')
