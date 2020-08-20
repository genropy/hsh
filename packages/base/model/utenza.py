# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('utenza',pkey='id',
                            name_long='Utenza',name_plural='Utenze',caption_field='id')
        self.sysFields(tbl)
        tbl.column('user_id',size='22',name_long='User').relation('adm.user.id',relation_name='case_collegate', mode='foreignkey', onDelete='raise')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',relation_name='utenze', onDelete='cascade', meta_thmode='plain')