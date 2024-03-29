from odoo import models, fields, api

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Chi tiết yêu cầu mua hàng'

    request_id = fields.Many2one('purchase.request', string='STT')
    product_id = fields.Many2one('product.template', string='Sản phẩm')
    description = fields.Text(string='Mô tả')
    company_id = fields.Many2one('res.company', string='Công Ty')
    uom_id = fields.Many2one('uom.uom', string='Đơn vị tính')
    qty = fields.Float(string='Số lượng')
    qty_approve = fields.Float(string='Số lượng đã phê duyệt',invisible=True)
    total = fields.Float(string='Tổng', compute='_compute_total', store=True)

    @api.depends('qty', 'product_id.list_price')
    def _compute_total(self):
        for line in self:
            line.total = line.qty * line.product_id.list_price
