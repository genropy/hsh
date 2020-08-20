#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('quantita')
        r.fieldcell('anno_acquisto')
        r.fieldcell('foto')
        r.fieldcell('posto_id')
        r.fieldcell('categoria_id')
        r.fieldcell('casa_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('nome' )
        fb.field('quantita' )
        fb.field('anno_acquisto' )
        fb.field('foto' )
        fb.field('posto_id' )
        fb.field('categoria_id' )
        fb.field('casa_id' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
