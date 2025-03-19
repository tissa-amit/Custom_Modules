from odoo import models, fields


class PerformanceReview(models.Model):
    _name = 'performance.review'
    _description = 'Employee Performance Review'

    # Basic Fields
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    review_date = fields.Date(string='Review Date', default=fields.Date.today())
    score = fields.Float(string='Score', help='Performance score out of 10')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    comments = fields.Text(string='Comments')

    # Image Field
    profileimage = fields.Binary(string='Profile Image', attachment=True)

    # Monetary Field
    salary = fields.Monetary(string='Salary', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    # Binary Field
    attachment = fields.Binary(string='Attachment')

    # Selection Field
    rating = fields.Selection([
        ('1', 'Poor'),
        ('2', 'Average'),
        ('3', 'Good'),
        ('4', 'Very Good'),
        ('5', 'Excellent'),
    ], string='Rating')

    # Boolean Field
    is_approved = fields.Boolean(string='Approved', default=False)

    from odoo.exceptions import UserError

    def action_mass_approve(self):
        """ Mass approve performance reviews (Only for CEO) """
        if not self.env.user.has_group('employee_performance.group_ceo'):
            raise UserError("Only the CEO can approve reviews.")

        self.write({'is_approved': True})

    def action_cancel_redirect(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:1881/odoo/action-476',
            'target': 'self',
        }
