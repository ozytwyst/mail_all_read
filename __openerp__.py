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
{
    'name' : 'Mail All Read',
    'version' : '1.0.0',
    'author' : 'Ozydev',
    'category' : 'Social Network',
    'depends' : ['mail'],
    'data' : [
        'wizard/mail_all_read_wizard_view.xml',
    ],
    'css' : [
        'static/src/css/mail_all_read.css'
    ],
    'js' : [
        'static/src/js/mail_all_read.js'
    ],
    'qweb' : [
        'static/src/xml/mail_all_read_main.xml',
    ],
    'installable' : True
}
