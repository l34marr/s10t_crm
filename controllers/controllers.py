# -*- coding: utf-8 -*-
# from odoo import http


# class S10tCrm(http.Controller):
#     @http.route('/s10t_crm/s10t_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s10t_crm/s10t_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s10t_crm.listing', {
#             'root': '/s10t_crm/s10t_crm',
#             'objects': http.request.env['s10t_crm.s10t_crm'].search([]),
#         })

#     @http.route('/s10t_crm/s10t_crm/objects/<model("s10t_crm.s10t_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s10t_crm.object', {
#             'object': obj
#         })
