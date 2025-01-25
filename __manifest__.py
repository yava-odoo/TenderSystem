{
    'name': 'Tender System',
    'version': '1.0',
    'summary': 'Module to manage tenders',
    'description': 'This module helps in managing tenders including views and models.',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/tender_views.xml',
        'security/tender_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}