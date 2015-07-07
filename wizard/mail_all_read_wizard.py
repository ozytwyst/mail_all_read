# -*- coding: utf-8 -*-
##############################################################################
#
#   mail_all_read module for OpenERP, Mark all mails as 'Read'
#   Copyright (C) 2015 ozytwyst Julien Thomazeau <ozydev@julienthomazeau.fr>
#
#   This file is a part of mail_all_read
#
#   mail_all_read is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   mail_all_read is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
from openerp.osv import orm
from openerp.osv import osv
from openerp.osv import fields
_logger = logging.getLogger(__name__)

class mail_all_read_wizard(orm.TransientModel):
    _name = 'mail_all_read.wizard'

    def mark_all_as_read(self, cr, uid, ids, context=None):
        user_pid = self.pool['res.users'].read(cr, uid, uid, ['partner_id'], context=context)['partner_id'][0]
        _logger.info(user_pid)

        mail_notification_obj = self.pool['mail.notification']
        mail_notification_ids = mail_notification_obj.search(cr,uid,[('partner_id','=',user_pid)])
        if mail_notification_ids:
            mail_notification_obj.write(cr,uid,mail_notification_ids,{'read':True})
        res = { 'type': 'ir.actions.client', 'tag': 'reload' }
        return res
