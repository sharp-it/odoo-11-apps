# -*- coding: utf-8 -*-
from odoo import http

# class CustomPoOnCashV1(http.Controller):
#     @http.route('/custom_po_on_cash_v1/custom_po_on_cash_v1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_po_on_cash_v1/custom_po_on_cash_v1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_po_on_cash_v1.listing', {
#             'root': '/custom_po_on_cash_v1/custom_po_on_cash_v1',
#             'objects': http.request.env['custom_po_on_cash_v1.custom_po_on_cash_v1'].search([]),
#         })

#     @http.route('/custom_po_on_cash_v1/custom_po_on_cash_v1/objects/<model("custom_po_on_cash_v1.custom_po_on_cash_v1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_po_on_cash_v1.object', {
#             'object': obj
#         })