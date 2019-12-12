# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:01:14 2019

@author: 손희영
"""

import pymysql

def predicted_pop(gu, date):

    conn = pymysql.connect(host='us-cdbr-iron-east-05.cleardb.net', port=3306, user = 'b987ca09f52fe8', password='0e33ea25', db = 'heroku_f3edcccc308c4b9', charset = 'utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs1 = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT `%s` FROM predict_population.predictedpopulation WHERE date = '%s';"%(gu,date)
    sql1 = "SELECT `%s` FROM predict_population.predictedpopulation WHERE date = 'average';"%(gu)
    
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

