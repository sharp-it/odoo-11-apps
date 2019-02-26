# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    cr_amount = fields.Monetary(digits=0, currency_field='journal_currency_id')
    db_amount = fields.Monetary(digits=0, currency_field='journal_currency_id')
    amount = fields.Monetary(digits=0, currency_field='journal_currency_id', compute='_calc_amount', store=True)

    @api.depends('cr_amount', 'db_amount')
    def _calc_amount(self):
        for rec in self:
            if rec.cr_amount > 0:
                rec.db_amount = 0
                rec.amount = -1 * rec.cr_amount
            if rec.db_amount > 0:
                rec.cr_amount = 0
                rec.amount = rec.db_amount
