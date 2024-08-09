# -*- coding: utf-'8' "-*-"

from openerp import api, models, fields, SUPERUSER_ID

import logging
_logger = logging.getLogger(__name__)


class RokiMailMassMailingContact(models.Model):
    _inherit = 'mail.mass_mailing.contact'

    newsletter_web_ui = fields.Boolean(string='Newsletter Web nur Oberfläche')
