# -*- coding: utf-8 -*-
{
    'name': "Sharp Cash In Out V1",

    'summary': """
        Change the way to use cash box with select in and out.""",

    'description': """
        Change the way to use cash box with select in and out.
    """,

    'author': "Sharp IT",
    'website': "http://www.sharp4it.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',
    'price': '10.0',
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing'],

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
}
