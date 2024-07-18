# -*- coding: utf-8 -*-
{
    'name': "management_library",
    'summary': """Quản lý thư viện mượn trả sách""",
    'description': """
        Long description of module's purpose
    """,
    'author': "NganNH",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/ql_sach_view.xml',
        'views/ql_muon_tra_sach_view.xml',
        'views/ql_the_thu_vien_view.xml',
        'views/bao_cao_thong_ke_view.xml',
        'views/ql_doc_gia_view.xml',
        'views/library_menus.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
