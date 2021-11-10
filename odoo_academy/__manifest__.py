# _*_ coding: utf-8 -*-

{

   'name': 'Odoo Academy',

   'summary': 'Aplicar descuentos en la interfaz del POS',

   'version': '12.0.1.0.0',  

   'description': """ Academy app.a
        Academy modeule:
        - Courses
        - Sessions
        - Attendees
    """, 

    
    'author': 'Yenbust',

  
    'category': 'Traning',
    
    'version': '0.1',
    
    'depends': ['sale'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/session_views_inherit.xml',
        'views/product_views_inherit.xml',
    ],
    
    # 'demo': ['demo/academy_demo.xml'],    
   


}