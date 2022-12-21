# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_sale_mrp_production_request = fields.Boolean("Automatic link between source Sale orders and created Production orders",
                                        help="Create direct link between the origin Sale orders and the created Production orders by the Production order requests")


