# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shipping_partner(models.Model):
    _name = 'shipping.partner'
    _description = 'A Shipping Partner Model'

    name = fields.Char()
    priority = fields.Integer()
    serviceable_zip_codes = fields.One2many(string='Zip codes for shipping partners', comodel_name='shipping.partner.zip.code', inverse_name='partner_id')
    tracking_ids = fields.One2many(string='Tracking ID of shipping partner', comodel_name='shipping.partner.tracking.id', inverse_name='partner_id')


class shipping_partner_zip_code(models.Model):
    _name = 'shipping.partner.zip.code'
    _description = 'zip codes for shipping partners'

    zip_code = fields.Char()
    partner_id = fields.Many2one(string='partner ID', comodel_name='shipping.partner')


class shipping_partner_tracking_id(models.Model):
    _name = 'shipping.partner.tracking.id'
    _description = 'Tracking ID for shipping partners'

    tracking_id = fields.Integer()
    partner_id = fields.Many2one(string='partner ID', comodel_name='shipping.partner')


# @api.multi
# def confirm_request(self):
#     self.state = 'confirm'

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
