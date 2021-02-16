# -*- coding: utf-8 -*-

{
    'name': 'roki_config',
    'summary': '''FS-Online roki instance configuration''',
    'description': '''
FS-Online Instance Configuration
================================

Customer configuration for the instance roki

- Default settings
- View modifications
- CSS
- Translations
    ''',
    'author': 'Joachim Grubelnik (joachim.grubelnik@datadialog.net), DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'sale',
        'portal_sale',
        'website',
        'website_sale_donate',
    ],
    'data': [
        'views/templates.xml',
        'views/snippet_options.xml',
    ],
}