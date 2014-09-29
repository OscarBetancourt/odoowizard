# -*- encoding: utf-8 -*-

from report import report_sxw

class report_nota(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(report_nota,self).__init__(cr,uid,name,context)

report_sxw.report_sxw('report.notas.report_nota','prueba.wiz','addons/notas/report/nota.rml',parser=report_nota,header=True)
