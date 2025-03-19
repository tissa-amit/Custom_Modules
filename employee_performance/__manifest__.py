{
    'name': 'Employee Performance By Amit',
    'version': '1.0',
    'author': 'Mr. Amit',
    'summary': 'Manage employee performance reviews and goals.',
    'description': """
        This module allows managers to conduct performance reviews,
        set and track goals, and generate performance reports for employees.
    """,
    'website': 'https://hamara-hr.com',
    'category': 'Human Resources',
    'depends': ['base', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        # 'data/ir_cron_data.xml',
        'security/security.xml',
        'views/performance_review_views.xml',

    ],
    'images': ['static/description/icon.png'],
    'web_icon': 'static/description/icon.png',

    'installable': True,
    'application': True,
}
