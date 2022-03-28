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
        casa_tbl.insert(nuova_casa)
        
        #...e la nuova utenza
        utenza_tbl = self.db.table('base.utenza')
        nuova_utenza = utenza_tbl.newrecord(user_id=record['id'], casa_id=nuova_casa['id'])
        utenza_tbl.insert(nuova_utenza)
        #per la nuova utenza usiamo l'equivalente newrecord invece del dict esclusivamente a scopo didattico

        self.db.commit()

        