# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'public:Public,th/th:TableHandler'

    def main(self,root,fromPage=None,**kwargs):
        bc = root.rootBorderContainer(datapath='main',
                        title='Gestione domestica')
