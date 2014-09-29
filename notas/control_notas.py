# -*- encoding: utf-8 -*-
from osv import osv,fields


class control_notas_alumnos(osv.osv):
    _name='control_notas.alumnos'
    _description='alumnos'
    _columns={  
            'nombre':fields.char('nombre',size=40,requiered=True),
            'apellido':fields.char('apellido',size=100,requiered=True),
            'telefono':fields.char('telefono',size=15,requiered=True),
            'nota':fields.char('nota',size=100,requiered=True),

    }
control_notas_alumnos()

class control_notas_profesores(osv.osv):
    _name='control_notas.profesores'
    _description='profesores'
    _columns={
            'alumnos_id':fields.many2many('control_notas.alumnos','alumnos',requiered=True),
             'email':fields.char('email',size=100,requiered=True),
    }
control_notas_profesores()

# _name es el nombre oficial de la clase
#_description Es una etiqueta para la tabla
# _columns son las columnas de la tabla  
