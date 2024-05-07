# -*- coding: utf-8 -*- 


{
    'name': 'Link Sale and MRP',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.4',
    'category': 'Sale/Manufacturing',
    'demo': [],
    'depends': ['sale','mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production_views.xml',
        'views/res_config_settings_views.xml'
    ],
    'license': 'LGPL-3',
}
