
from gnr.web.gnrwebpage import BaseComponent
import datetime

class LoginComponent(BaseComponent):
    def onUserSelected_base(self,avatar,data):
        utenze = self.db.table('base.utenza'
                ).query(where='$user_id=:user_id', 
                user_id=avatar.user_id).fetch()
        #utenze domestiche collegate
        if not utenze:
            #sono il configuratore
            data['configuratore'] = True
            return
        elif len(utenze)==1:
            #se ho una casa sola
            utenza = utenze[0]
            data['casa_id'] = utenza['casa_id']
            data['casa_singola'] = True

    def rootenvForm_base(self,fb):
        fb.dbSelect(value='^.casa_id',dbtable='base.casa',
                        condition='@utenze.user_id=:user_id', #relation_name
                        condition_user_id='=gnr.avatar.user_id',
                        selected_nome='.nome_casa',
                        disabled='^.casa_singola',hasDownArrow=True,
                        lbl='Casa')
        

    def onAuthenticating_base(self, avatar, rootenv=None):
        rootenv['current_casa_id'] = rootenv['casa_id']
