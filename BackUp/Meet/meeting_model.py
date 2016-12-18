# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions


class MeetingTask(models.Model):
    _name = 'meeting.task'
    _description = 'Meeting task'
    _inherit = ['mail.thread']
    Theme = fields.Char('theme',help="add a theme")
    Lecturer = fields.Char('tutor')
    Docs=fields.Html('brief')
    Time=fields.Datetime('time')
    Place=fields.Char('place')
    user_id=fields.Many2one('res.users','coordinator')
    date_deadline=fields.Datetime('deadline')
    
    user_ids=fields.Many2many('res.users',string='participants')
    user_count=fields.Integer('number of persons',compute='_get_count')
     
    @api.one
    def register(self):
        user_id=(4,[[self.env.user.id]])
        self.write({'user_ids':[user_id]})
        return True 
      
    @api.one
    def _get_count(self):
        self.user_count=len(self.user_ids)
        return True





