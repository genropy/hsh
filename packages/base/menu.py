#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    base = root.branch('Base')
    base.thpage('Utenze',table='base.utenza')
    base.thpage('Oggetti',table='base.oggetto')
    base.thpage('Posti',table='base.posto')
    base.lookups('Categorie-Tipi', lookup_manager="base")
    base.thpage('Case',table='base.casa')
