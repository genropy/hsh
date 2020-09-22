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
        r.fieldcell('categoria_id')
        r.fieldcell('posto_id')
        r.fieldcell('casa_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

    def th_options(self):
        return dict(uploadTags='user')

class ViewFromCategoria(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('quantita')
        r.fieldcell('anno_acquisto')
        r.fieldcell('posto_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')

class ViewFromPosto(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('quantita')
        r.fieldcell('anno_acquisto')
        r.fieldcell('categoria_id')


    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        bc = pane.borderContainer(margin='2px',text_align='center', datapath='#FORM.record')

        cp_left = bc.contentPane(region='left', width='50%', margin='10px')
        fb = cp_left.formbuilder(cols=1, border_spacing='4px')
        fb.field('nome' )
        fb.field('anno_acquisto' )
        fb.field('quantita' )
        fb.field('categoria_id',tag='hdbselect',folderSelectable=True)
        fb.field('posto_id', tag='hdbselect',folderSelectable=True)
        fb.checkboxtext(value='^.tag_id', table='base.oggetto_tag', 
                            columns='$nome', lbl='Tag: ', cols=2)
        
        cp_right = bc.contentPane(region='center', margin='10px')
        cp_right.img(src='^.foto', 
                    crop_height='150px', max_width='150px',
                    crop_width='150px', max_height='150px',
                    crop_border='2px dotted silver',
                    crop_rounded=6, edit=True,
                    placeholder=True,
                    upload_filename='=#FORM.record.id',
                    upload_folder='site:oggetti/foto')

    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        if newrecord:
            record['casa_id'] = self.rootenv['casa_id']
            categoria_record = record['@categoria_id']
            record['posto_id'] = categoria_record['default_posto_id']

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', duplicate=True)
