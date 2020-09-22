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
        r.fieldcell('default_posto_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top', datapath='.record', padding='5px')
        fb = top.formbuilder(cols=3, border_spacing='4px')
        fb.field('nome' )
        fb.field('descrizione' )
        fb.field('default_posto_id' )
        center = bc.contentPane(region='center')
        th = center.dialogTableHandler(relation='@oggetti', addrow=True, delrow=True)
        form.htree.relatedTableHandler(th,inherited=True) #questa aggiunta mi permette di attivare drag&drop 
                                                            #anche tra oggetti e albero gerarchico delle categorie

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', hierarchical=True, duplicate=True)
