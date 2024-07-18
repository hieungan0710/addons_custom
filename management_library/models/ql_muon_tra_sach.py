from odoo import fields, models, api, _

class QLMuonTraSach(models.Model):
    _name = 'ql.muon.tra.sach'
    _description = 'Quản Lý Hoạt Động Mượn Trả Sách'
    _rec_name = 'ma_sach_id'

    ma_sach_id = fields.Many2one('ql.sach', string='Mã Sách', required=True)
    doc_gia_id = fields.Many2one('ql.doc.gia', string='Mã Độc Giả', required=True)
    trang_thai = fields.Selection([
        ('dang_muon', 'Đang Mượn'),
        ('da_tra', 'Đã Trả'),
        ('tre_han', 'Trễ Hạn')
    ], string='Trạng Thái', default='dang_muon', required=True)
    ngay_nhap = fields.Date(string='Ngày Nhập', default=fields.Date.today)
