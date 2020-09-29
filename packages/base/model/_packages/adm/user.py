# encoding: utf-8
from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('user', pkey='id')
        self.sysFields(tbl)

        #Aggiungo la colonna "prima casa", che verrà inserita durante la registrazione
        tbl.column('prima_casa', plugToForm=True, lbl='Prima casa')
    
    def trigger_onInserting(self, record):    
        #Durante la creazione dello user imposto il gruppo a "Casalingo"
        record['group_code'] = 'HK'

    def trigger_onInserted(self, record):
        #Alla creazione dello user inserisco automaticamente anche la nuova casa...
        casa_tbl = self.db.table('base.casa')
        casa_id = casa_tbl.newPkeyValue()
        nuova_casa = dict(id=casa_id, nome=record['prima_casa'])
        self.db.table('base.casa').insert(nuova_casa)
        
        #...e la nuova utenza
        utenza_tbl = self.db.table('base.utenza')
        utenza_id = utenza_tbl.newPkeyValue()
        nuova_utenza = dict(id=utenza_id, user_id=record['id'], casa_id=nuova_casa['id'])
        self.db.table('base.utenza').insert(nuova_utenza)

        self.db.commit()

        