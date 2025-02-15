# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('posto',pkey='id',name_long='Posto',
                        name_plural='Posti',caption_field='hierarchical_descrizione',
                        partition_casa_id='casa_id')
        self.sysFields(tbl, hierarchical='descrizione', counter=True)
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('casa_id',size='22',name_long='Casa'
                    ).relation('casa.id',relation_name='posti', onDelete='cascade')
        tbl.column('posto_tipo_id',size='22', group='_', name_long='Tipo posto'
                    ).relation('posto_tipo.id', relation_name='posti', mode='foreignkey', onDelete='raise')

    def trigger_onInserting(self, record):
        record['casa_id'] = record['casa_id'] or self.db.currentEnv['casa_id']

    def aggiungiPosto(self,descrizione=None,**kwargs):
        record = self.newrecord(descrizione=descrizione)
        self.insert(record)
        return record

    def trigger_onInserting(self,record):
        record['casa_id'] = record['casa_id'] or self.db.currentEnv.get('casa_id')
