# -*- coding: utf-8 -*-
{
    'name': 'The Hospital',
    'version': '18.0.0.1',
    'author': 'ibrahem Bamoman',
    'website': '',
    'category': '',
    'depends': ['base','website', 'portal'],
    'data': [
        
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/sequence_data.xml',
        
        # Views
        'views/hospital_menu.xml',
        'views/the_hospital.xml',
        'views/disease.xml',
        # 'views/cure.xml',
        
        
        # Report
        'report/the_hospital_report.xml',
    
        ],
    'demo': [],
    'application': True,
}
