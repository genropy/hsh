# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('oggetto_tag', pkey='id', name_long='Tag oggetti', 
                        caption_field='nome', lookup=True)
        self.sysFields(tbl)
        
        tbl.column('nome', name_long='Nome')