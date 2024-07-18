from odoo import fields, models, api, _

class QLDocGia(models.Model):
    _name = 'ql.doc.gia'
    _description = 'Quản Lý Độc Giả'
    _rec_name = 'doc_gia_id'

    doc_gia_id = fields.Char(string='Mã Độc Giả', required=True)
    ten_doc_gia = fields.Char(string='Tên Độc Giả', required=True)
    ngay_sinh = fields.Date(string='Ngày Sinh')  # Đảm bảo trường này tồn tại
    dia_chi = fields.Char(string='Địa Chỉ')
    sdt = fields.Char(string='Số Điện Thoại')
    email = fields.Char(string='Email')
