# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('casa',pkey='id',name_long='Casa',name_plural='Case',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome')
        tbl.column('descrizione',name_long='Descrizione')