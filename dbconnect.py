# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:01:14 2019

@author: 손희영
"""

import pymysql

def predicted_pop(gu, date):

    conn = pymysql.connect(host='172.16.98.77', port=3306, user = 'bonvoyage', password='9897', db = 'predict_population', charset = 'utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs1 = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT `%s` FROM predict_population.predictedpopulation_3 WHERE date = '%s';"%(gu,date)
    sql1 = "SELECT `%s` FROM predict_population.predictedpopulation_3 WHERE date = 'average';"%(gu)
    
    curs.execute(sql)
    rows = curs.fetchall()
    pop = int(rows[0][gu])
    
    curs1.execute(sql1)
    rows1 = curs1.fetchall()
    avg = int(rows1[0][gu])
      
    if pop>(avg*1.01):
        return "many"
    elif pop<(avg*0.99):
        return "less"
    else:
        return "similar"


