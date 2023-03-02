import unittest
from datetime import date

from models import Customer


class CustomerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer(
            first_name='John',
            last_name='Doe',
            nationality='American',
            birth_date=date(1980, 1, 1),
            passport_number=123456,
            passport_valid_date=date(2030, 1, 1),
            email='john.doe@example.com',
            phone_number=1234567890,
            is_archived=False,
            ordered=False,
            plan='basic'
        )
    
    def test_customer_creation(self):
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.first_name, 'John')
        self.assertEqual(self.customer.last_name, 'Doe')
        self.assertEqual(self.customer.nationality, 'American')
        self.assertEqual(self.customer.birth_date, date(1980, 1, 1))
        self.assertEqual(self.customer.passport_number, 123456)
        self.assertEqual(self.customer.passport_valid_date, date(2030, 1, 1))
        self.assertEqual(self.customer.email, 'john.doe@example.com')
        self.assertEqual(self.customer.phone_number, 1234567890)
        self.assertFalse(self.customer.is_archived)
        self.assertFalse(self.customer.ordered)
        self.assertEqual(self.customer.plan, 'basic')

if __name__ == '__main__':
    unittest.main()