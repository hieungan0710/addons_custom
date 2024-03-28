from odoo import models, fields, api, _
class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Yêu cầu mua hàng'

    name = fields.Char(string='STT',Tracking=True , required=True, copy=False, readonly=True,index=True, default=lambda self: _('PR'))
    department_id = fields.Many2one('hr.department', string='Bộ phận')
    request_id = fields.Many2one('res.users', string='Người tạo yêu cầu')
    approver_id = fields.Many2one('res.users', string='Người phê duyệt')
    date = fields.Date(string='Ngày tạo', default=fields.Date.today )
    date_approve = fields.Date(string='Ngày phê duyệt' )
    request_line_ids = fields.One2many('purchase.request.line', 'request_id')
    description = fields.Text(string='Mô tả')
    state = fields.Selection([('draft', 'Draft'), ('wait', 'Wait'), ('approved', 'Approved'), ('cancel', 'Cancel')],
                             string='Trạng thái', default='draft')
    total_qty = fields.Float(string='Tổng số lượng', compute='_compute_total_qty', store=True)
    total_amount = fields.Float(string='Tổng giá trị', compute='_compute_total_amount', store=True)
    have_write_right = fields.Boolean(string='Have write right', compute="_compute_have_write_right")
    go = fields.Boolean(string="create", default=False)

    @api.onchange('name')
    def _compute_have_write_right(self):
        if self.env.user.has_group('purchase_request.group_user'):
            self.have_write_right = False
        if self.env.user.has_group('purchase_request.group_admin'):
            self.have_write_right = True

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request')
        if self.go == False:
            vals['go'] = True
        return super(PurchaseRequest, self).create(vals)

    @api.depends('request_line_ids.qty')
    def _compute_total_qty(self):
        for request in self:
            request.total_qty = sum(request.request_line_ids.mapped('qty'))

    @api.depends('request_line_ids.total')
    def _compute_total_amount(self):
        for request in self:
            request.total_amount = sum(request.request_line_ids.mapped('total'))

    @api.depends()
    def action_delete_purchase_request(self):
        for record in self:
            record.unlink()