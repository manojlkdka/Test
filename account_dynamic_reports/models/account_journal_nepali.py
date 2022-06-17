from odoo import api, fields, models, _


class AccountJournalNepaliDate(models.Model):
    _inherit = 'account.journal'

    nepali_date_to_jl = fields.Char('Date (B.S.)', compute="_get_nepalidate_to_jl", store=True)
    nepali_date_from_jl = fields.Char('Date (B.S.)', compute="_get_nepalidate_from_jl", store=True)

    @api.depends('date_to')
    def _get_nepalidate_to_jl(self):
        dt_format = '%Y-%m-%d'
        for jrnl in self:
            if jrnl.date_to:
                np_dt_abs = self.env['np.date']
                dt = np_dt_abs.get_nepalidate(str(jrnl.date_to), dt_format)
                jrnl.update({'nepali_date_to_gl': dt})
    
    @api.depends('date_from')
    def _get_nepalidate_from_jl(self):
        dt_format = '%Y-%m-%d'
        for jrnl in self:
            if jrnl.date_from:
                np_dt_abs = self.env['np.date']
                dt = np_dt_abs.get_nepalidate(str(jrnl.date_from), dt_format)
                jrnl.update({'nepali_date_from_gl': dt})
