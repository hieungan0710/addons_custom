from odoo import models, fields, api, _

class QLSach(models.Model):
    _name = 'ql.sach'
    _description = 'Quản lý sách'
    _rec_name = 'sach_id'

    sach_id = fields.Char(string='Mã Đầu Sách', required=True)
    ten_sach = fields.Char(string='Tên Đầu Sách', required=True)
    nha_xb = fields.Char(string='Nhà Xuất Bản', required=True)
    so_trang = fields.Integer(string='Số Trang', required=True)
    tac_gia = fields.Char(string='Tác Giả', required=True)
    so_luong = fields.Integer(string='Số Lượng Sách', required=True)
