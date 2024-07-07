# -*- coding: utf-8 -*-
import base64

import xlrd

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ImportProductsWizard(models.TransientModel):
    _name = 'import_products_wizard'
    _description = _('Import_products_wizard')

    file = fields.Binary(string=_('Add excel file with products data to import'))
    file_name = fields.Char('File Name')

    def import_products(self):
        if not self.file:
            raise UserError('Please upload a file.')

        data = xlrd.open_workbook(file_contents=base64.b64decode(self.file))
        sheet = data.sheet_by_index(0)

        REQUIRED_HEADERS = {'Product Name': 0, 'Category': 1, 'Price': 2, 'Quantity': 3}
        existing_headers = sheet.row_values(0)

        if len(existing_headers) < len(REQUIRED_HEADERS):
            raise UserError(f'Missing headers: {", ".join(REQUIRED_HEADERS)}')
        missing_headers = []
        for header in REQUIRED_HEADERS:
            if header not in existing_headers:
                missing_headers.append(header)

        if missing_headers:
            raise UserError(f'Missing headers: {", ".join(missing_headers)}')

        for row_idx in range(1, sheet.nrows):
            row = sheet.row(row_idx)
            category_name = row[REQUIRED_HEADERS['Category']].value
            category = self.env['tech_gear.product_category'].search([('name', '=', category_name)], limit=1)
            if not category:
                category = self.env['tech_gear.product_category'].create({'name': category_name})
            
            product_vals = {
                'name': row[REQUIRED_HEADERS['Product Name']].value,
                'tech_category_id': category.id,
                'list_price': row[REQUIRED_HEADERS['Price']].value,
            }
            product = self.env['product.template'].search([('name', '=', product_vals['name'])], limit=1)
            if product.exists():
                product.write(product_vals)
            else:
                product_vals['detailed_type'] = 'product'
                product = self.env['product.template'].create(product_vals)
            
            warehouse = self.env['stock.warehouse'].search(
            [('company_id', '=', self.env.company.id)], limit=1
            )
            self.env['stock.quant'].with_context(inventory_mode=True).create({
                'product_id': product.id,
                'location_id': warehouse.lot_stock_id.id,
                'inventory_quantity': row[REQUIRED_HEADERS['Quantity']].value,
            })._apply_inventory()
        return {'type': 'ir.actions.act_window_close'}
