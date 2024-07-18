from odoo import fields, models, api, _

class QLTheThuVien(models.Model):
    _name = 'ql.the.thu.vien'
    _description = 'Quản Lý Thẻ Thư Viện'
    _rec_name = 'doc_gia_id'

    doc_gia_id = fields.Many2one('ql.doc.gia', string='Mã Độc Giả', required=True)
    ten_doc_gia = fields.Char(related='doc_gia_id.ten_doc_gia', string='Họ Tên Độc Giả', readonly=True)
    ngay_sinh = fields.Date(related='doc_gia_id.ngay_sinh', string='Ngày Sinh', readonly=True)
    don_vi = fields.Char(string='Lớp')
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ')
    ], string='Giới Tính', default='nam')
