# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    po_id = fields.Many2one('purchase.order', string='PO No.')
