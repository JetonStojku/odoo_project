import base64

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase
from odoo.tools.misc import file_open


class TestProductImport(TransactionCase):

    def setUp(self):
        super(TestProductImport, self).setUp()
        self.category_model = self.env['tech_gear.product_category']
        self.product_model = self.env['product.template']
        self.warehouse_model = self.env['stock.warehouse']

        self.test_excel_file = base64.b64encode(file_open('tech_gear_inventory/data/products_data.xlsx', 'rb').read())

    def test_import_products(self):
        # Create wizard with test Excel file
        wizard = self.env['import_products_wizard'].create({
            'file': self.test_excel_file,
            'file_name': 'products_data.xlsx'
        })

        # Run import and check for expected outcomes
        try:
            wizard.import_products()
        except UserError as e:
            self.fail(f'Import raised an unexpected UserError: {e}')

        # Check if product and category were created
        category = self.category_model.search([('name', '=', 'Mobiles')], limit=1)
        self.assertTrue(category.exists(), 'Category was not created.')

        product = self.product_model.search([('name', '=', 'Samsung SM-A057 Galaxy')], limit=1)
        self.assertTrue(product.exists(), 'Product was not created.')
        self.assertEqual(product.categ_id.id, category.id, 'Product category mismatch.')
        self.assertEqual(product.list_price, 165, 'Product price mismatch.')

        # Check stock quant
        warehouse = self.warehouse_model.search([('company_id', '=', self.env.company.id)], limit=1)
        stock_quant = self.env['stock.quant'].search([('product_id', '=', product.id), ('location_id', '=', warehouse.lot_stock_id.id)], limit=1)
        self.assertTrue(stock_quant.exists(), 'Stock quant was not created.')
        self.assertEqual(stock_quant.quantity, 15, 'Product quantity mismatch.')
