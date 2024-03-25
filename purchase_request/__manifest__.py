{
    'name': "Purchase Request",
    'summary': """ Quản lý yêu cầu mua hàng """,
    'description': """ Quản lý yêu cầu mua hàng""",
    'author': "NganNH",
    'website': "https://www.ngannh.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','purchase', 'hr', 'product'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'data/purchase_sequence.xml',
        'views/purchase_request_views.xml',
        'views/purchase_request_line_views.xml',
        # 'views/templates.xml',

    ],

}
