# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('oggetto_categoria',pkey='id',
                            name_long='Categoria oggetti',name_plural='Categorie oggetti',
                            caption_field='nome', partition_casa_id='casa_id')
        self.sysFields(tbl,hierarchical='nome',df=True,counter=True)
        tbl.column('nome',name_long='Nome')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',
                    relation_name='categorie_casa', mode='foreignkey', onDelete='raise')
        tbl.column('posto_id_def',size='22', group='_', name_long='Posto Default').relation('posto.id', 
                    relation_name='categorie_posti_def', mode='foreignkey', onDelete='raise')