{
    'name': 'Meeting Application',
    'description': 'Publish a meeting',
    'author': 'Cao Fa',
    'depends': ['mail'],
    'application': True,
    'data': [
        'meeting_view.xml',
        'security/ir.model.access.csv',
        'security/meeting_access_rules.xml',
    ]
}
