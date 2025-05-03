# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Hospital(models.Model):
    _name = 'hospital'  
    
    _description = 'Hospital' 
    
    ref = fields.Char(default='New', readonly=1)  #عملية(رقم التصنيع)
    patient_name = fields.Char(string='Patient Name',default='Name', required=True)  #اسم المريض
    age = fields.Integer(string='The Age')  #العمر
    doctors_note = fields.Text(string='Doctors_Notes ')  #ملاحظات الطبيب
    signature = fields.Char(string='The Signature')  # التوقيع

    disease_ids = fields.Many2many('disease')
    cure_ids = fields.Many2many('cure')
    
    
    @api.model
    def create(self, vals_list): #عملية(رقم التصنيع)
        res = super(Hospital, self).create(vals_list)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('hospital_seq')
        return res
    
    
    
    
class Cure(models.Model):
        
    _name = 'cure'  
    
    _description = 'cure' 
    
  
    name_cure = fields.Char(default='The Cure',required=1)  #العلاج
    company_name = fields.Char(string='Company Name')  #اسم الشركة المصنعة للدواء
    medication_time = fields.Date(string='Medication Time', required=1)  #وقت تناول الدواء
    
    