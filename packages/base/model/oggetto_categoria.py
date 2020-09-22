# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('oggetto_categoria',pkey='id',
                            name_long='Categoria oggetti',name_plural='Categorie oggetti',
                            caption_field='nome', partition_casa_id='casa_id')
        self.sysFields(tbl,hierarchical='nome',counter=True)
        tbl.column('nome',name_long='Nome')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',
                    relation_name='categorie_casa', mode='foreignkey', onDelete='raise')
        tbl.column('default_posto_id',size='22', group='_', name_long='Posto Default').relation('posto.id', 
                    relation_name='categorie_posti_def', mode='foreignkey', onDelete='raise')
    
    def aggiungiCategoria(self,nome=None,**kwargs):
        record = self.newrecord(nome=nome)
        self.insert(record)
        return record
    
    def trigger_onInserting(self,record):
        record['casa_id'] = record['casa_id'] or self.db.currentEnv.get('casa_id')

