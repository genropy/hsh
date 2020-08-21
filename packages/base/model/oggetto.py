# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('oggetto',pkey='id',name_long='Oggetto',
                            name_plural='Oggetti',caption_field='nome',
                            partition_casa_id='casa_id')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome')
        tbl.column('quantita', size=':2', dtype='L', name_long='Quantità')
        tbl.column('anno_acquisto',dtype='I', format='####', name_long='Anno acquisto')
        tbl.column('foto', dtype='P', name_long='Foto')
        tbl.column('categoria_id',size='22',name_long='Categoria', categoria='.categoria').relation('oggetto_categoria.id',
                        relation_name='oggetti', mode='foreignkey')
        tbl.column('posto_id',size='22',name_long='Posto').relation('posto.id',
                    relation_name='oggetti', mode='foreignkey', onDelete='raise')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',
                    relation_name='oggetti', mode='foreignkey', onDelete='raise')
        tbl.column('tag_id',size='22',name_long='Tag').relation('oggetto_tag.id',
                        relation_name='oggetti', mode='foreignkey')

    def defaultValues(self):
        return dict(quantita='1', casa_id=self.db.currentEnv['casa_id'])
    
    #def trigger_onInserting(self, record):
    #   record['casa_id'] = record['casa_id'] or self.db.currentEnv['casa_id']