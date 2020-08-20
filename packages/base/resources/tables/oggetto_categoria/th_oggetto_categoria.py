#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('hierarchical_nome')
        r.fieldcell('df_fbcolumns')
        r.fieldcell('df_colswidth')
        r.fieldcell('descrizione')
        r.fieldcell('casa_id')
        r.fieldcell('posto_id_def')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('nome' )
        fb.field('hierarchical_nome' )
        fb.field('df_fbcolumns' )
        fb.field('df_colswidth' )
        fb.field('descrizione' )
        fb.field('casa_id' )
        fb.field('posto_id_def' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', hierarchical=True)
