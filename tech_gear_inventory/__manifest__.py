{
    'name': 'Tech gear inventory',
    'version': '1.0',
    'summary': 'Tech gear inventory summary',
    'description': 'Tech gear inventory description',
    'category': 'Category',
    'author': 'Jeton Stojku',
    'website': 'https://github.com/JetonStojku/odoo_project',
    'license': 'LGPL-3',
    'depends': ['base', 'stock', 'base_import'],
    "data": [
        "security/ir.model.access.csv",
        "views/product_category_views.xml",
        "views/product_template_views.xml",
        "wizard/import_products_wizard.xml"
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
