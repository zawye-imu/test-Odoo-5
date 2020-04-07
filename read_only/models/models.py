# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class read_only(models.Model):
#     _name = 'read_only.read_only'
#     _description = 'read_only.read_only'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




class sale_orderline_inherit1(models.Model):
    _inherit = "sale.order.line"
    price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0,readonly=True)