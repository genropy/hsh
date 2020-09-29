
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
    
    # Personalizzo la form di login per aggiungere anche una casa durante la registrazione
    def login_newUser_form(self,form):
        fb = form.record.div(margin='10px',margin_right='20px',padding='10px').formbuilder(
                        cols=1, border_spacing='6px',onEnter='SET creating_new_user = true;',
                        width='100%',tdl_width='6em',fld_width='100%',row_height='3ex')
        fb.textbox(value='^.firstname',lbl='!!First name',validate_notnull=True,
                                                    validate_case='c',validate_len='2:')
        fb.textbox(value='^.lastname',lbl='!!Last name',validate_notnull=True,
                                                    validate_case='c',validate_len='2:')
        fb.textbox(value='^.email',lbl='!!Email',validate_notnull=True)
        fb.textbox(value='^.username',lbl='!!Username',validate_notnull=True,
                                    validate_nodup='adm.user.username',validate_len='4:')
        fb.textbox(value='^.prima_casa',lbl='!!Casa',validate_notnull=True)
        fb.div(width='100%',position='relative',row_hidden=False).button('!!Send',
            action='SET creating_new_user = true;',position='absolute',right='-5px',top='8px')
