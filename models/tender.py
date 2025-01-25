from odoo import models, fields, api, _

class Tender(models.Model):
    _name = 'tender.system'
    _description = 'Tender System'
    _rec_name = 'srm_enquiry_number'

    srm_enquiry_number = fields.Char(string='SRM Enquiry Number', copy=False, readonly=True, index=True)
    customer_name = fields.Char(string='Customer Name', required=True)
    customer_location = fields.Char(string='Customer Location')
    tender_no = fields.Integer(string='Tender Number', required=True)
    tender_date = fields.Date(string='Tender Date', required=True)
    tender_due_datetime = fields.Datetime(string='Tender Due DateTime', required=True)

    @api.model
    def create(self, vals):
        for val in vals:
            val['srm_enquiry_number'] = self.env['ir.sequence'].next_by_code('srm.enquiry') or _("New")
        return super(Tender, self).create(vals)