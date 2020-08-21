#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')

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
        fb.field('posto_tipo_id' )
        center = bc.contentPane(region='center')
        th = center.dialogTableHandler(relation='@oggetti',addrow=False,delrow=False)
        form.htree.relatedTableHandler(th,inherited=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', 
                    hierarchical=True, tree_picker='posto_tipo_id', duplicate=True)
