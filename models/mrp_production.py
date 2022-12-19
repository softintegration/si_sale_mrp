# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_id = fields.Many2one('sale.order', 'Sales order', index=True, readonly=True, check_company=True,
                              states={'draft': [('readonly', False)]})
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True,
                                 states={'draft': [('readonly', False)]}, store=True, index=True)
    client_order_ref = fields.Char(string='Customer Reference', related='sale_id.client_order_ref', readonly=True)
