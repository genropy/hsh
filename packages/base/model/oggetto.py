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
                        relation_name='oggetti', mode='foreignkey',onDelete='raise')
        tbl.column('posto_id',size='22',name_long='Posto').relation('posto.id',
                    relation_name='oggetti', mode='foreignkey', onDelete='raise')
        tbl.column('casa_id',size='22',name_long='Casa').relation('casa.id',
                    relation_name='oggetti', mode='foreignkey', onDelete='raise')
        tbl.column('tag_id',size='22',name_long='Tag').relation('oggetto_tag.id',
                        relation_name='oggetti', mode='foreignkey')

    def defaultValues(self):
        return dict(quantita='1', casa_id=self.db.currentEnv['casa_id'])

    #def importerStructure(self):
    #    return dict(fields= dict(nome='descrizione',
    #                            categoria='tipo',
    #                            posto='luogo'),
    #                         mandatories='nome',
    #                         default_anno=2020)
#
    #def importerInsertRow(self,row,**kwargs):
    #    print(x)

    def importer_alfa(self,reader):
        tblcategoria = self.db.table('base.oggetto_categoria')
        tblposto = self.db.table('base.posto')
        for r in reader():
            if not r['descrizione']:
                continue
            record_oggetto = self.newrecord()
            record_oggetto['nome'] = r['descrizione']
            if r['data']:
                record_oggetto['anno_acquisto'] = r['data'].year
    
            if r['tipo']:
                categoria = tblcategoria.query(where='$nome=:t',t=r['tipo'],limit=1).fetch()
                if not categoria:
                    categoria = tblcategoria.aggiungiCategoria(nome=r['tipo'])
                else:
                    categoria = categoria[0]
                record_oggetto['categoria_id'] = categoria['id']
            
                
            if r['luogo']:
                posto = tblposto.query(where='$descrizione=:p',p=r['luogo'],limit=1).fetch()
                if not posto:
                    posto = tblposto.aggiungiPosto(descrizione=r['luogo'])
                else:
                    posto = posto[0]
                record_oggetto['posto_id'] = posto['id']
            self.insert(record_oggetto)
        self.db.commit()
        


    def importer_beta(self,reader):
        print('beta')


    #def trigger_onInserting(self, record):
    #   record['casa_id'] = record['casa_id'] or self.db.currentEnv['casa_id']