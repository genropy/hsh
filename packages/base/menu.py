#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    base = root.branch('Base')
    base.thpage('Utenze',table='base.utenza')
    base.thpage('Oggetti',table='base.oggetto')
    base.thpage('Oggetti categorie',table='base.oggetto_categoria')
    base.thpage('Posti',table='base.posto')
    base.lookups('Tipi', lookup_manager="base")
    base.thpage('Case',table='base.casa')
