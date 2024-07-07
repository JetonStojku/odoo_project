from odoo import api, fields, models


class ProductCategory(models.Model):
    _name = 'tech_gear.product_category'
    _description = 'Description'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
