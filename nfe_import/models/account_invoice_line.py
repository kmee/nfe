# -*- coding: utf-8 -*-
# Copyright (C) 2019 - KMEE INFORMATICA LTDA
#     Daniel Sadamo <daniel.sadamo@kmee.com.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api, _, tools
from openerp.addons import decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    cfop_fornecedor = fields.Char(
        string='CFOP do fornecedor',
        default='',
    )
    icms_efetivo_value = fields.Float(
        string='Valor ICMS Efetivo',
        default=0.0,
    )
    icms_efetivo_bc = fields.Float(
        string='Valor BC ICMS Efetivo',
        default=0.0,
    )
    icms_efetivo_perc_reduction = fields.Float(
        string='Perc Reducao BC ICMS Efetivo',
        default=0.0,
    )
    icms_efetivo_percent = fields.Float(
        string='Perc ICMS Efetivo',
        default=0.0,
    )
