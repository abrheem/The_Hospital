# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class disease(models.Model):
    _name = 'disease'  
    
    
    disease_name = fields.Char(string='The Disease')  # تشخيص
    
    
    