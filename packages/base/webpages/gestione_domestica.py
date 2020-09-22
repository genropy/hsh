# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'public:Public,th/th:TableHandler'

    def main(self,root,fromPage=None,**kwargs):
        casa_record = self.db.table('base.casa').record(pkey=self.rootenv['casa_id']).output('record')
        frame = root.rootBorderContainer(datapath='main',
                        title=f'Gestione {casa_record["nome"]}')
        frame.data('.casa_record',casa_record)
        self.gestioneDomesticaTabs(frame.tabContainer(region='center',margin='2px'))
        footer = frame.bottom.slotToolbar('*,logoutbtn,5') #logout già predefinito ma così lo personalizziamo

        footer.logoutbtn.button(label='Esci',action="genro.logout()",
                        iconClass='iconbox switch_off',
                        tip='!!Logout')
    
    def gestioneDomesticaTabs(self,tc):
        tc.contentPane(title='Gestione posti'
                            ).thFormHandler(table='base.posto', datapath='.posti',
                                            default_casa_id=self.rootenv['casa_id'],
                                            viewResource='ViewFromPosto')
        tc.contentPane(title='Gestione oggetti').thFormHandler(table='base.oggetto_categoria',
                                            datapath='.oggetti', 
                                            default_casa_id=self.rootenv['casa_id'],
                                            viewResource='ViewFromCategoria')
        th = tc.contentPane(title='Tutti gli oggetti').dialogTableHandler(
            table='base.oggetto',view_store_onStart=True,
            default_casa_id=self.rootenv['casa_id']
        )
        th.view.top.bar.replaceSlots('delrow','export,importer,5,delrow')