# -*- coding: utf-8 -*-
{
    'name': "Custom PO on Expense v1",

    'summary': """
        Add a relation between PO and expense""",

    'description': """
        Add a relation between PO and expense
    """,

    'author': "Sharp IT",
    'website': "http://www.sharpit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',
    'price': '0.0',
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing', 'purchase', 'hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'images': [
        'static/description/banner.png',
        'static/description/cover.png',
    ]
}
