# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class src/user/data_addition/(models.Model):
#     _name = 'src/user/data_addition/.src/user/data_addition/'
#     _description = 'src/user/data_addition/.src/user/data_addition/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
