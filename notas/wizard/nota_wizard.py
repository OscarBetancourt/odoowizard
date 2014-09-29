# -*- encoding: utf-8 -*-

from osv import osv,fields
from openerp.tools.translate import _

class prueba_wiz(osv.osv_memory):
    _name='prueba.wiz'
     
    _columns={
              'nota':fields.many2one('control_notas.alumnos','reporte',requiered=True),
              'telefono':fields.selection([('movistar','movistar'),('tigo','tigo'),('claro','claro')],"telefono"),
              'periodo':fields.datetime('periodo'),
    }

    def print_report(self,cr,uid,ids,data,context=None):
        #data['form'].update(self.read(cr, uid, ids, ['nota','telefono'], context=context)[0]) 
       # data = self.pre_print_report(cr, uid, ids, data, context=context)
        return {
              'type':'ir.actions.report.xml',
              'report_name':'notas.report_nota', 
              'datas': data}

prueba_wiz()    

