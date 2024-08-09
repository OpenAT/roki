# -*- coding: utf-'8' "-*-"
from openerp import api, models, fields, SUPERUSER_ID

import logging
_logger = logging.getLogger(__name__)


class RokiResPartner(models.Model):
    _inherit = 'res.partner'

    newsletter_web_ui = fields.Boolean(string='Newsletter Web nur Oberfläche')
