# -*- coding: utf-8 -*-
# from odoo import http


# class DataAdditions(http.Controller):
#     @http.route('/data_additions/data_additions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_additions/data_additions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_additions.listing', {
#             'root': '/data_additions/data_additions',
#             'objects': http.request.env['data_additions.data_additions'].search([]),
#         })

#     @http.route('/data_additions/data_additions/objects/<model("data_additions.data_additions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_additions.object', {
#             'object': obj
#         })
