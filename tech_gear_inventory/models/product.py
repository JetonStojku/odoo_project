from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tech_category_id = fields.Many2one('tech_gear.product_category', string='Category')
