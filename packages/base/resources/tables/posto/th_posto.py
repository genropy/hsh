#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_descrizione')

    def th_order(self):
        return 'hierarchical_descrizione'

    def th_query(self):
        return dict(column='hierarchical_descrizione', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top', datapath='.record', padding='5px')
        fb = top.formbuilder(cols=3, border_spacing='4px')
        fb.field('descrizione' )
        fb.field('posto_tipo_id' )
        center = bc.contentPane(region='center')
        th = center.dialogTableHandler(relation='@oggetti',addrow=False,delrow=False, margin='8px')
        form.htree.relatedTableHandler(th,inherited=True) #questa aggiunta mi permette di attivare drag&drop 
                                                            #anche tra oggetti e albero gerarchico dei posti


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', 
                    hierarchical=True, tree_picker='posto_tipo_id', duplicate=True)
