# -*- coding: utf-8 -*-
# from odoo import http


# class ReadOnly(http.Controller):
#     @http.route('/read_only/read_only/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/read_only/read_only/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('read_only.listing', {
#             'root': '/read_only/read_only',
#             'objects': http.request.env['read_only.read_only'].search([]),
#         })

#     @http.route('/read_only/read_only/objects/<model("read_only.read_only"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('read_only.object', {
#             'object': obj
#         })
