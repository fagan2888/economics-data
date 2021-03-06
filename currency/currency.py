#coding:utf-8

"""
数据来源, 东方财富 http://data.eastmoney.com/cjsj/moneysupply.aspx?p=1
API : http://data.eastmoney.com/DataCenter_V3/Chart/cjsj/China.ashx?isxml=false&type=GJZB&style=ZGZB&mkt=11&r=0.2980607212649313
"""

import pandas as pd
import matplotlib.pyplot as plt


def p2f(x):
    return float(x.strip('%'))


df = pd.read_csv('data.csv', sep='\t', converters={'M2同比' : p2f, 'M1同比' : p2f, 'M0同比': p2f})

df = df.sort_values(by='月份')
df = df.set_index('月份')

df[['M2数量（亿元）', 'M1数量（亿元）', 'M0数量（亿元）']].plot(grid='on', figsize = (12,6))
f = plt.gcf()
f.savefig('data.svg')


df[['M2同比', 'M1同比', 'M0同比']].plot(grid='on', figsize = (12,6))
f = plt.gcf()
f.savefig('data_r.svg')

def md_table(df):
    return df.to_html(index=False).encode('utf-8', 'ignore')

fp = open('data.html', 'w')
fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
         'type="text/css">' \
         'table {border-collapse: collapse;}' \
         'th, td {border: 1px solid;}' \
         '</style>')


fp.write(open('data.svg').read())
fp.write(open('data_r.svg').read())
fp.write( md_table(df.reset_index().sort_values(by='月份', ascending=False)) )
fp.close()
