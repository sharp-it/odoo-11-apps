# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    move_type = fields.Selection([('I', 'In'), ('O', 'Out')])
    move_amount = fields.Monetary(digits=0, currency_field='journal_currency_id')
    amount = fields.Monetary(digits=0, currency_field='journal_currency_id', compute='_calc_amount', store=True)

    @api.depends('move_type', 'move_amount')
    def _calc_amount(self):
        for rec in self:
            if rec.move_type == 'O':
                rec.amount = -1 * rec.move_amount
            else:
                rec.move_type = 'I'
                rec.amount = rec.move_amount
