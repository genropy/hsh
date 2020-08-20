# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('oggetto',pkey='id',name_long='Oggetto',
                            name_plural='Oggetti',caption_field='nome',
                            partition_casa_id='casa_id')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome')
        tbl.column('quantita', size=':2', dtype='L', name_long='Quantità')
        tbl.column('anno_acquisto',dtype='I',name_long='Anno acquisto')
        tbl.column('foto',name_long='Foto')
        tbl.column('posto_id',size='22',name_long='posto').relation('posto.id',relation_name='oggetti', mode='foreignkey', onDelete='raise')
        tbl.column('categoria_id',size='22',name_long='Categoria').relation('oggetto_categoria.id',relation_name='oggetti', mode='foreignkey')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',relation_name='oggetti', mode='foreignkey', onDelete='raise')
