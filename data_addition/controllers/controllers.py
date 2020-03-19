# -*- coding: utf-8 -*-
# from odoo import http


# class Src/user/dataAddition/(http.Controller):
#     @http.route('/src/user/data_addition//src/user/data_addition//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src/user/data_addition//src/user/data_addition//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('src/user/data_addition/.listing', {
#             'root': '/src/user/data_addition//src/user/data_addition/',
#             'objects': http.request.env['src/user/data_addition/.src/user/data_addition/'].search([]),
#         })

#     @http.route('/src/user/data_addition//src/user/data_addition//objects/<model("src/user/data_addition/.src/user/data_addition/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src/user/data_addition/.object', {
#             'object': obj
#         })
