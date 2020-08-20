# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('posto_tipo', pkey='id', name_long='Tipo posto', name_plural='Tipi posto',
                        caption_field='nome', lookup=True)
        self.sysFields(tbl)
        
        tbl.column('nome', name_long='Nome')