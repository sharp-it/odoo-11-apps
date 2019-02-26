# -*- coding: utf-8 -*-
from odoo import http

# class SharpCashInOutV1(http.Controller):
#     @http.route('/sharp_cash_in_out_v1/sharp_cash_in_out_v1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sharp_cash_in_out_v1/sharp_cash_in_out_v1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sharp_cash_in_out_v1.listing', {
#             'root': '/sharp_cash_in_out_v1/sharp_cash_in_out_v1',
#             'objects': http.request.env['sharp_cash_in_out_v1.sharp_cash_in_out_v1'].search([]),
#         })

#     @http.route('/sharp_cash_in_out_v1/sharp_cash_in_out_v1/objects/<model("sharp_cash_in_out_v1.sharp_cash_in_out_v1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sharp_cash_in_out_v1.object', {
#             'object': obj
#         })