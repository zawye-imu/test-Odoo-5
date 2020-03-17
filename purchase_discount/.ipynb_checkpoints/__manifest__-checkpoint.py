{
    'name': 'Purchase Discount Addition',
    'description': 'Apply discount on purchase invoice total own me',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'me',
    'website': '',
    'depends': [
        'purchase',
        'account',
    ],
    'data': [
    'views/purchase_order_view.xml',
    ],
    'application': True,
    'installable': True,
}