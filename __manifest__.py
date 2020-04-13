{
    'name': "Shipping Partners",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       A module that makes it easy to track shipping for the sales in a company
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
