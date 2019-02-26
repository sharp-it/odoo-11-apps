# -*- coding: utf-8 -*-
from odoo import http

# class SharpCashInOutV2(http.Controller):
#     @http.route('/sharp_cash_in_out_v2/sharp_cash_in_out_v2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sharp_cash_in_out_v2/sharp_cash_in_out_v2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sharp_cash_in_out_v2.listing', {
#             'root': '/sharp_cash_in_out_v2/sharp_cash_in_out_v2',
#             'objects': http.request.env['sharp_cash_in_out_v2.sharp_cash_in_out_v2'].search([]),
#         })

#     @http.route('/sharp_cash_in_out_v2/sharp_cash_in_out_v2/objects/<model("sharp_cash_in_out_v2.sharp_cash_in_out_v2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sharp_cash_in_out_v2.object', {
#             'object': obj
#         })