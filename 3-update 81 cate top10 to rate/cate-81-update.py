import pymysql
import pymysql.cursors
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


mydb = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='action'
    )

#Registration year distribution of each product
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
cursor_1=mydb.cursor()
for product_id in product_top10:
    for year_list in year_dist:
        consumer_reg_tm='SELECT ROUND(T0.num1/T1.num2*100,3)\
                         FROM (SELECT count(*) AS num1\
                               FROM user\
                               WHERE user_id IN (SELECT user_id\
                               FROM action\
                               WHERE action.sku_id ={x}\
                               AND action.type = 2)\
                               AND YEAR(user_reg_tm)={y})T0,\
                              (SELECT count(*) as num2\
                               FROM user\
                               WHERE user_id IN(SELECT user_id\
                               FROM action\
                               WHERE action.type=2)\
                               AND YEAR(user_reg_tm)={y})T1;'.format(x=product_id,y=year_list)
        cursor_1.execute(consumer_reg_tm)
        consumer_reg_tm_sql=cursor_1.fetchall()
        for consumer_reg_tm_result in consumer_reg_tm_sql:
            print(product_id,year_list,consumer_reg_tm_result)
cursor_1.close() 

'''
81731 2008 (Decimal('0.326'),)
81731 2009 (Decimal('0.258'),)
81731 2010 (Decimal('0.285'),)
81731 2011 (Decimal('0.304'),)
81731 2012 (Decimal('0.274'),)
81731 2013 (Decimal('0.278'),)
81731 2014 (Decimal('0.260'),)
81731 2015 (Decimal('0.209'),)
81731 2016 (Decimal('0.176'),)
81731 2017 (Decimal('0.130'),)
81731 2018 (Decimal('0.074'),)
281779 2008 (Decimal('0.221'),)
281779 2009 (Decimal('0.167'),)
281779 2010 (Decimal('0.180'),)
281779 2011 (Decimal('0.186'),)
281779 2012 (Decimal('0.136'),)
281779 2013 (Decimal('0.169'),)
281779 2014 (Decimal('0.155'),)
281779 2015 (Decimal('0.124'),)
281779 2016 (Decimal('0.114'),)
281779 2017 (Decimal('0.115'),)
281779 2018 (Decimal('0.066'),)
167081 2008 (Decimal('0.221'),)
167081 2009 (Decimal('0.161'),)
167081 2010 (Decimal('0.146'),)
167081 2011 (Decimal('0.170'),)
167081 2012 (Decimal('0.174'),)
167081 2013 (Decimal('0.180'),)
167081 2014 (Decimal('0.248'),)
167081 2015 (Decimal('0.257'),)
167081 2016 (Decimal('0.252'),)
167081 2017 (Decimal('0.243'),)
167081 2018 (Decimal('0.276'),)
177991 2008 (Decimal('0.130'),)
177991 2009 (Decimal('0.140'),)
177991 2010 (Decimal('0.098'),)
177991 2011 (Decimal('0.141'),)
177991 2012 (Decimal('0.135'),)
177991 2013 (Decimal('0.174'),)
177991 2014 (Decimal('0.168'),)
177991 2015 (Decimal('0.169'),)
177991 2016 (Decimal('0.146'),)
177991 2017 (Decimal('0.139'),)
177991 2018 (Decimal('0.099'),)
47830 2008 (Decimal('0.169'),)
47830 2009 (Decimal('0.091'),)
47830 2010 (Decimal('0.118'),)
47830 2011 (Decimal('0.057'),)
47830 2012 (Decimal('0.070'),)
47830 2013 (Decimal('0.067'),)
47830 2014 (Decimal('0.065'),)
47830 2015 (Decimal('0.056'),)
47830 2016 (Decimal('0.051'),)
47830 2017 (Decimal('0.052'),)
47830 2018 (Decimal('0.034'),)
150215 2008 (Decimal('0.143'),)
150215 2009 (Decimal('0.140'),)
150215 2010 (Decimal('0.166'),)
150215 2011 (Decimal('0.114'),)
150215 2012 (Decimal('0.116'),)
150215 2013 (Decimal('0.104'),)
150215 2014 (Decimal('0.090'),)
150215 2015 (Decimal('0.072'),)
150215 2016 (Decimal('0.049'),)
150215 2017 (Decimal('0.041'),)
150215 2018 (Decimal('0.015'),)
319860 2008 (Decimal('0.143'),)
319860 2009 (Decimal('0.081'),)
319860 2010 (Decimal('0.105'),)
319860 2011 (Decimal('0.100'),)
319860 2012 (Decimal('0.078'),)
319860 2013 (Decimal('0.082'),)
319860 2014 (Decimal('0.072'),)
319860 2015 (Decimal('0.060'),)
319860 2016 (Decimal('0.056'),)
319860 2017 (Decimal('0.041'),)
319860 2018 (Decimal('0.013'),)
281165 2008 (Decimal('0.234'),)
281165 2009 (Decimal('0.129'),)
281165 2010 (Decimal('0.153'),)
281165 2011 (Decimal('0.129'),)
281165 2012 (Decimal('0.109'),)
281165 2013 (Decimal('0.112'),)
281165 2014 (Decimal('0.090'),)
281165 2015 (Decimal('0.081'),)
281165 2016 (Decimal('0.073'),)
281165 2017 (Decimal('0.063'),)
281165 2018 (Decimal('0.040'),)
320225 2008 (Decimal('0.065'),)
320225 2009 (Decimal('0.075'),)
320225 2010 (Decimal('0.046'),)
320225 2011 (Decimal('0.084'),)
320225 2012 (Decimal('0.072'),)
320225 2013 (Decimal('0.080'),)
320225 2014 (Decimal('0.075'),)
320225 2015 (Decimal('0.102'),)
320225 2016 (Decimal('0.098'),)
320225 2017 (Decimal('0.087'),)
320225 2018 (Decimal('0.057'),)
'''

plt.subplot(2,3,1)
reg_level_year=[0.326,0.258,0.285,0.304,0.274,0.278,0.260,0.209,0.176,0.130,0.074]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('registration year distribution:81731')

plt.subplot(2,3,2)
reg_level_year=[0.221,0.167,0.180,0.186,0.136,0.169,0.155,0.124,0.114,0.115,0.066]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281779')

plt.subplot(2,3,3)
reg_level_year=[0.221,0.161,0.146,0.170,0.174,0.180,0.248,0.257,0.252,0.243,0.276]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('167081')

plt.subplot(2,3,4)
reg_level_year=[0.130,0.140,0.098,0.141,0.135,0.174,0.168,0.169,0.146,0.139,0.099]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('177991')

plt.subplot(2,3,5)
reg_level_year=[0.169,0.091,0.118,0.057,0.070,0.067,0.065,0.056,0.051,0.052,0.034]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('47830')

plt.subplot(2,3,6)
reg_level_year=[0.143,0.140,0.166,0.114,0.116,0.104,0.090,0.072,0.049,0.041,0.015]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('150215')
plt.show()  

plt.subplot(2,2,1)
reg_level_year=[0.143,0.081,0.105,0.100,0.078,0.082,0.072,0.060,0.056,0.041,0.013]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('319860')

plt.subplot(2,2,2)
reg_level_year=[0.234,0.129,0.153,0.129,0.109,0.112,0.090,0.081,0.073,0.063,0.040]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281165')

plt.subplot(2,2,3)
reg_level_year=[0.065,0.075,0.046,0.084,0.072,0.080,0.075,0.102,0.098,0.087,0.057]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('320225')
plt.show() 





#Consumer level distribution (grouped by products)
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
consumer_level_list=[1,3,4,5,6,7]
cursor_2=mydb.cursor()
for product_id in product_top10:
    for level_list in consumer_level_list:
        consumer_city_level='SELECT ROUND(T0.num1/T1.num2*100,3)\
                            FROM(SELECT count(*) AS num1\
                                FROM user\
                                WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.sku_id={x} AND action.type=2)\
                                AND user.user_lv_cd={y})T0,\
                                (SELECT count(*) AS num2\
                                 FROM user\
                                 WHERE user_id IN(SELECT user_id\
                                 FROM action\
                                 WHERE action.type=2)\
                                 AND user.user_lv_cd={y})T1;'.format(x=product_id,y=level_list)
        cursor_2.execute(consumer_city_level)
        consumer_city_level_sql=cursor_2.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(product_id,level_list,city_level_result)
cursor_2.close()
'''
81731 1 (Decimal('0.178'),)
81731 3 (Decimal('0.104'),)
81731 4 (Decimal('0.000'),)
81731 5 (Decimal('0.271'),)
81731 6 (Decimal('0.088'),)
81731 7 (Decimal('0.339'),)
281779 1 (Decimal('0.117'),)
281779 3 (Decimal('0.062'),)
281779 4 (Decimal('0.000'),)
281779 5 (Decimal('0.161'),)
281779 6 (Decimal('0.058'),)
281779 7 (Decimal('0.222'),)
167081 1 (Decimal('0.221'),)
167081 3 (Decimal('0.125'),)
167081 4 (Decimal('0.607'),)
167081 5 (Decimal('0.186'),)
167081 6 (Decimal('0.311'),)
167081 7 (Decimal('0.183'),)
177991 1 (Decimal('0.155'),)
177991 3 (Decimal('0.146'),)
177991 4 (Decimal('0.000'),)
177991 5 (Decimal('0.161'),)
177991 6 (Decimal('0.120'),)
177991 7 (Decimal('0.158'),)
47830 1 (Decimal('0.050'),)
47830 3 (Decimal('0.031'),)
47830 4 (Decimal('0.000'),)
47830 5 (Decimal('0.070'),)
47830 6 (Decimal('0.022'),)
47830 7 (Decimal('0.112'),)
150215 1 (Decimal('0.055'),)
150215 3 (Decimal('0.021'),)
150215 4 (Decimal('0.000'),)
150215 5 (Decimal('0.091'),)
150215 6 (Decimal('0.022'),)
150215 7 (Decimal('0.153'),)
319860 1 (Decimal('0.046'),)
319860 3 (Decimal('0.000'),)
319860 4 (Decimal('0.000'),)
319860 5 (Decimal('0.080'),)
319860 6 (Decimal('0.015'),)
319860 7 (Decimal('0.130'),)
281165 1 (Decimal('0.066'),)
281165 3 (Decimal('0.031'),)
281165 4 (Decimal('0.015'),)
281165 5 (Decimal('0.106'),)
281165 6 (Decimal('0.040'),)
281165 7 (Decimal('0.155'),)
320225 1 (Decimal('0.096'),)
320225 3 (Decimal('0.083'),)
320225 4 (Decimal('0.015'),)
320225 5 (Decimal('0.080'),)
320225 6 (Decimal('0.084'),)
320225 7 (Decimal('0.073'),)
'''

plt.subplot(2,5,1)
product_action_top1=[0.178,0.104,0.000,0.271,0.088,0.339]
type_number1=[1,3,4,5,6,7]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.117,0.062,0.000,0.161,0.058,0.222]
type_number2=[1,3,4,5,6,7]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.221,0.125,0.607,0.186,0.311,0.183]
type_number3=[1,3,4,5,6,7]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.155,0.146,0.000,0.161,0.120,0.158]
type_number4=[1,3,4,5,6,7]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.050,0.031,0.000,0.070,0.022,0.112]
type_number5=[1,3,4,5,6,7]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.055,0.021,0.000,0.091,0.022,0.153]
type_number6=[1,3,4,5,6,7]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.046,0.000,0.000,0.080,0.015,0.130]
type_number7=[1,3,4,5,6,7]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.066,0.031,0.015,0.106,0.040,0.155]
type_number9=[1,3,4,5,6,7]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.096,0.083,0.015,0.080,0.084,0.073]
type_number10=[1,3,4,5,6,7]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()










#City level distribution (grouped by product)
city_level_num=[1,2,3,4,5,6]
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_3=mydb.cursor()
for product_id in product_top10:
    for city_num_level in city_level_num:
        consumer_city_level='SELECT ROUND(T0.num1/T1.num2*100,3)\
                             FROM (SELECT count(*) AS num1\
                                   FROM user\
                                   WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                                   FROM action\
                                   WHERE action.sku_id={y} AND action.type=2))T0,\
                                   (SELECT count(*) AS num2\
                                    FROM user\
                                    where user.city_level={x}\
                                    AND user.user_id IN (SELECT user_id\
                                    FROM action\
                                    WHERE action.type=2))T1;'.format(x=city_num_level,y=product_id)
        cursor_3.execute(consumer_city_level)
        consumer_city_level_sql=cursor_3.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(product_id,city_num_level,city_level_result)
cursor_3.close()
'''
81731 1 (Decimal('0.196'),)
81731 2 (Decimal('0.137'),)
81731 3 (Decimal('0.237'),)
81731 4 (Decimal('0.219'),)
81731 5 (Decimal('0.158'),)
81731 6 (Decimal('0.094'),)
281779 1 (Decimal('0.133'),)
281779 2 (Decimal('0.070'),)
281779 3 (Decimal('0.136'),)
281779 4 (Decimal('0.129'),)
281779 5 (Decimal('0.124'),)
281779 6 (Decimal('0.169'),)
167081 1 (Decimal('0.269'),)
167081 2 (Decimal('0.232'),)
167081 3 (Decimal('0.197'),)
167081 4 (Decimal('0.215'),)
167081 5 (Decimal('0.257'),)
167081 6 (Decimal('0.207'),)
177991 1 (Decimal('0.152'),)
177991 2 (Decimal('0.166'),)
177991 3 (Decimal('0.162'),)
177991 4 (Decimal('0.137'),)
177991 5 (Decimal('0.138'),)
177991 6 (Decimal('0.113'),)
47830 1 (Decimal('0.064'),)
47830 2 (Decimal('0.046'),)
47830 3 (Decimal('0.062'),)
47830 4 (Decimal('0.058'),)
47830 5 (Decimal('0.050'),)
47830 6 (Decimal('0.056'),)
150215 1 (Decimal('0.073'),)
150215 2 (Decimal('0.033'),)
150215 3 (Decimal('0.094'),)
150215 4 (Decimal('0.070'),)
150215 5 (Decimal('0.053'),)
150215 6 (Decimal('0.019'),)
319860 1 (Decimal('0.063'),)
319860 2 (Decimal('0.046'),)
319860 3 (Decimal('0.067'),)
319860 4 (Decimal('0.062'),)
319860 5 (Decimal('0.050'),)
319860 6 (Decimal('0.075'),)
281165 1 (Decimal('0.085'),)
281165 2 (Decimal('0.083'),)
281165 3 (Decimal('0.094'),)
281165 4 (Decimal('0.083'),)
281165 5 (Decimal('0.076'),)
281165 6 (Decimal('0.056'),)
320225 1 (Decimal('0.095'),)
320225 2 (Decimal('0.075'),)
320225 3 (Decimal('0.080'),)
320225 4 (Decimal('0.075'),)
320225 5 (Decimal('0.091'),)
320225 6 (Decimal('0.150'),)
'''

plt.subplot(2,5,1)
product_action_top1=[0.196,0.137,0.237,0.219,0.158,0.094]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.133,0.070,0.136,0.129,0.124,0.169]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.369,0.232,0.197,0.215,0.257,0.207]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.152,0.166,0.162,0.137,0.138,0.113]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.064,0.046,0.062,0.058,0.050,0.056]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.073,0.033,0.094,0.070,0.053,0.019]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.063,0.046,0.067,0.062,0.050,0.075]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.085,0.083,0.094,0.083,0.076,0.056]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.095,0.075,0.080,0.075,0.091,0.150]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()







#The age distribution of top 10 products
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
age_list=[1,2,3,4,5,6]
cursor_4=mydb.cursor()
for product_id in product_top10:
    for age_num in age_list:
        consumer_order_age='SELECT ROUND(T0.num1/T1.num2*100,3)\
                            FROM (SELECT count(*) AS num1\
                                FROM user\
                                WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.sku_id={x} AND action.type=2)\
                                AND user.age={y})T0,\
                                (SELECT count(*) AS num2\
                                 FROM user\
                                 WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.type=2)\
                                AND user.age={y})T1;'.format(x=product_id,y=age_num)
        cursor_4.execute(consumer_order_age)
        consumer_order_age_sql=cursor_4.fetchall()
        for order_age_result in consumer_order_age_sql:
            print(product_id,age_num,order_age_result)
cursor_4.close()
'''
81731 1 (Decimal('0.085'),)
81731 2 (Decimal('0.103'),)
81731 3 (Decimal('0.000'),)
81731 4 (Decimal('0.166'),)
81731 5 (Decimal('0.260'),)
81731 6 (Decimal('0.187'),)
281779 1 (Decimal('0.090'),)
281779 2 (Decimal('0.119'),)
281779 3 (Decimal('0.000'),)
281779 4 (Decimal('0.074'),)
281779 5 (Decimal('0.136'),)
281779 6 (Decimal('0.159'),)
167081 1 (Decimal('0.268'),)
167081 2 (Decimal('0.364'),)
167081 3 (Decimal('0.000'),)
167081 4 (Decimal('0.132'),)
167081 5 (Decimal('0.158'),)
167081 6 (Decimal('0.358'),)
177991 1 (Decimal('0.138'),)
177991 2 (Decimal('0.102'),)
177991 3 (Decimal('0.000'),)
177991 4 (Decimal('0.133'),)
177991 5 (Decimal('0.156'),)
177991 6 (Decimal('0.153'),)
47830 1 (Decimal('0.041'),)
47830 2 (Decimal('0.074'),)
47830 3 (Decimal('0.000'),)
47830 4 (Decimal('0.024'),)
47830 5 (Decimal('0.058'),)
47830 6 (Decimal('0.075'),)
150215 1 (Decimal('0.041'),)
150215 2 (Decimal('0.048'),)
150215 3 (Decimal('0.000'),)
150215 4 (Decimal('0.037'),)
150215 5 (Decimal('0.082'),)
150215 6 (Decimal('0.087'),)
319860 1 (Decimal('0.038'),)
319860 2 (Decimal('0.067'),)
319860 3 (Decimal('0.000'),)
319860 4 (Decimal('0.021'),)
319860 5 (Decimal('0.057'),)
319860 6 (Decimal('0.090'),)
281165 1 (Decimal('0.044'),)
281165 2 (Decimal('0.074'),)
281165 3 (Decimal('0.000'),)
281165 4 (Decimal('0.044'),)
281165 5 (Decimal('0.085'),)
281165 6 (Decimal('0.117'),)
320225 1 (Decimal('0.053'),)
320225 2 (Decimal('0.097'),)
320225 3 (Decimal('0.000'),)
320225 4 (Decimal('0.065'),)
320225 5 (Decimal('0.079'),)
320225 6 (Decimal('0.107'),)
'''

#draw the plot to show which age prefer to buy the product
plt.subplot(2,5,1)
product_action_top1=[0.085,0.103,0.000,0.166,0.260,0.187]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.090,0.119,0.000,0.074,0.136,0.159]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.268,0.364,0.000,0.132,0.158,0.358]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.138,0.102,0.000,0.133,0.156,0.153]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.041,0.074,0.000,0.024,0.058,0.075]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.041,0.048,0.000,0.037,0.082,0.087]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.038,0.067,0.000,0.021,0.057,0.090]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.044,0.074,0.000,0.044,0.085,0.117]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.053,0.097,0.000,0.065,0.079,0.107]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()






#The consumer makes orders for one same product more than once
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
cursor_5=mydb.cursor()
for product_id in product_top10:
    for year_list in year_dist:
        consumer_reg_tm='SELECT ROUND(T0.num1/T1.num2*100,3)\
                        FROM(SELECT count(*) AS num1\
                            FROM user\
                            WHERE user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id ={x}\
                            AND action.type = 2\
                            GROUP BY action.user_id\
                            HAVING count(*)>1)\
                            AND YEAR(user_reg_tm)={y})T0,\
                            (SELECT count(*) AS num2\
                            FROM user\
                            WHERE user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id ={x}\
                            AND action.type = 2\
                            GROUP BY action.user_id\
                            HAVING count(*)>1))T1'.format(x=product_id,y=year_list)
        cursor_5.execute(consumer_reg_tm)
        consumer_reg_tm_sql=cursor_5.fetchall()
        for consumer_reg_tm_result in consumer_reg_tm_sql:
            print(product_id,year_list,consumer_reg_tm_result)
cursor_5.close()
'''
81731 2008 (Decimal('2.190'),)
81731 2009 (Decimal('1.460'),)
81731 2010 (Decimal('1.460'),)
81731 2011 (Decimal('6.569'),)
81731 2012 (Decimal('11.679'),)
81731 2013 (Decimal('8.029'),)
81731 2014 (Decimal('13.139'),)
81731 2015 (Decimal('20.438'),)
81731 2016 (Decimal('21.898'),)
81731 2017 (Decimal('8.759'),)
81731 2018 (Decimal('4.380'),)
281779 2008 (Decimal('0.000'),)
281779 2009 (Decimal('1.613'),)
281779 2010 (Decimal('4.839'),)
281779 2011 (Decimal('6.452'),)
281779 2012 (Decimal('6.452'),)
281779 2013 (Decimal('16.129'),)
281779 2014 (Decimal('20.968'),)
281779 2015 (Decimal('14.516'),)
281779 2016 (Decimal('11.290'),)
281779 2017 (Decimal('14.516'),)
281779 2018 (Decimal('3.226'),)
167081 2008 (Decimal('0.000'),)
167081 2009 (Decimal('0.730'),)
167081 2010 (Decimal('1.460'),)
167081 2011 (Decimal('1.460'),)
167081 2012 (Decimal('9.489'),)
167081 2013 (Decimal('7.299'),)
167081 2014 (Decimal('12.409'),)
167081 2015 (Decimal('16.058'),)
167081 2016 (Decimal('26.277'),)
167081 2017 (Decimal('16.788'),)
167081 2018 (Decimal('8.029'),)
177991 2008 (Decimal('0.000'),)
177991 2009 (Decimal('0.000'),)
177991 2010 (Decimal('0.000'),)
177991 2011 (Decimal('5.952'),)
177991 2012 (Decimal('5.952'),)
177991 2013 (Decimal('5.952'),)
177991 2014 (Decimal('15.476'),)
177991 2015 (Decimal('20.238'),)
177991 2016 (Decimal('20.238'),)
177991 2017 (Decimal('20.238'),)
177991 2018 (Decimal('5.952'),)
47830 2008 (Decimal('4.545'),)
47830 2009 (Decimal('9.091'),)
47830 2010 (Decimal('4.545'),)
47830 2011 (Decimal('9.091'),)
47830 2012 (Decimal('9.091'),)
47830 2013 (Decimal('4.545'),)
47830 2014 (Decimal('13.636'),)
47830 2015 (Decimal('31.818'),)
47830 2016 (Decimal('4.545'),)
47830 2017 (Decimal('4.545'),)
47830 2018 (Decimal('4.545'),)
150215 2008 (Decimal('0.000'),)
150215 2009 (Decimal('4.762'),)
150215 2010 (Decimal('11.905'),)
150215 2011 (Decimal('9.524'),)
150215 2012 (Decimal('11.905'),)
150215 2013 (Decimal('19.048'),)
150215 2014 (Decimal('7.143'),)
150215 2015 (Decimal('28.571'),)
150215 2016 (Decimal('7.143'),)
150215 2017 (Decimal('0.000'),)
150215 2018 (Decimal('0.000'),)
319860 2008 (Decimal('0.000'),)
319860 2009 (Decimal('0.000'),)
319860 2010 (Decimal('0.000'),)
319860 2011 (Decimal('7.692'),)
319860 2012 (Decimal('23.077'),)
319860 2013 (Decimal('7.692'),)
319860 2014 (Decimal('7.692'),)
319860 2015 (Decimal('30.769'),)
319860 2016 (Decimal('0.000'),)
319860 2017 (Decimal('15.385'),)
319860 2018 (Decimal('7.692'),)
281165 2008 (Decimal('0.000'),)
281165 2009 (Decimal('2.941'),)
281165 2010 (Decimal('2.941'),)
281165 2011 (Decimal('8.824'),)
281165 2012 (Decimal('14.706'),)
281165 2013 (Decimal('17.647'),)
281165 2014 (Decimal('11.765'),)
281165 2015 (Decimal('11.765'),)
281165 2016 (Decimal('11.765'),)
281165 2017 (Decimal('11.765'),)
281165 2018 (Decimal('5.882'),)
320225 2008 (Decimal('0.000'),)
320225 2009 (Decimal('0.000'),)
320225 2010 (Decimal('0.000'),)
320225 2011 (Decimal('6.757'),)
320225 2012 (Decimal('4.054'),)
320225 2013 (Decimal('4.054'),)
320225 2014 (Decimal('9.459'),)
320225 2015 (Decimal('17.568'),)
320225 2016 (Decimal('28.378'),)
320225 2017 (Decimal('24.324'),)
320225 2018 (Decimal('5.405'),)
'''
plt.subplot(2,3,1)
reg_level_year=[2.190,1.460,1.460,6.569,11.679,8.029,13.139,20.438,21.898,8.759,4.380]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('registration year distribution:81731')

plt.subplot(2,3,2)
reg_level_year=[0.000,1.613,4.839,6.452,6.452,16.129,20.968,14.516,11.290,14.516,3.226]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281779')

plt.subplot(2,3,3)
reg_level_year=[0.000,0.730,1.460,1.460,9.489,7.229,12.409,16.058,26.277,16.788,8.029]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('167081')

plt.subplot(2,3,4)
reg_level_year=[0.000,0.000,0.000,5.952,5.952,5.952,15.476,20.238,20.238,20.238,5.952]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('177991')

plt.subplot(2,3,5)
reg_level_year=[4.545,9.091,4.545,9.091,9.091,4.545,13.636,31.818,4.545,4.545,4.545]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('47830')

plt.subplot(2,3,6)
reg_level_year=[0.000,4.762,11.905,9.524,11.905,19.048,7.143,28.571,7.143,0.000,0.000]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('150215')
plt.show()  

plt.subplot(2,2,1)
reg_level_year=[0.000,0.000,0.000,7.692,23.077,7.692,7.692,30.769,0.000,15.385,7.692]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('319860')

plt.subplot(2,2,2)
reg_level_year=[0.000,2.941,2.941,8.824,14.706,17.647,11.765,11.765,11.765,11.765,5.882]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281165')

plt.subplot(2,2,3)
reg_level_year=[0.000,0.000,0.000,6.757,4.054,4.054,9.459,17.568,28.378,24.324,5.405]
year_dist=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('320225')
plt.show() 









#Consumer level distribution (grouped by products)
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
consumer_level_list=[1,3,4,5,6,7]
cursor_6=mydb.cursor()
for product_id in product_top10:
    for level_list in consumer_level_list:
        consumer_city_level='SELECT ROUND(T0.num1/T1.num2*100,3)\
                            FROM(SELECT count(*) AS num1\
                                FROM user\
                                WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.sku_id={x} AND action.type=2\
                                GROUP BY action.user_id\
                                HAVING count(*)>1)\
                                AND user.user_lv_cd={y})T0,\
                                (SELECT count(*) AS num2\
                                 FROM user\
                                 WHERE user_id IN(SELECT user_id\
                                 FROM action\
                                 WHERE action.type=2\
                                 GROUP BY action.user_id\
                                 HAVING count(*)>1)\
                                 AND user.user_lv_cd={y})T1;'.format(x=product_id,y=level_list)
        cursor_6.execute(consumer_city_level)
        consumer_city_level_sql=cursor_6.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(product_id,level_list,city_level_result)
cursor_6.close()
'''
81731 1 (Decimal('0.040'),)
81731 3 (Decimal('0.063'),)
81731 4 (Decimal('0.000'),)
81731 5 (Decimal('0.050'),)
81731 6 (Decimal('0.013'),)
81731 7 (Decimal('0.052'),)
281779 1 (Decimal('0.013'),)
281779 3 (Decimal('0.063'),)
281779 4 (Decimal('0.000'),)
281779 5 (Decimal('0.021'),)
281779 6 (Decimal('0.010'),)
281779 7 (Decimal('0.028'),)
167081 1 (Decimal('0.049'),)
167081 3 (Decimal('0.000'),)
167081 4 (Decimal('0.000'),)
167081 5 (Decimal('0.034'),)
167081 6 (Decimal('0.074'),)
167081 7 (Decimal('0.026'),)
177991 1 (Decimal('0.031'),)
177991 3 (Decimal('0.000'),)
177991 4 (Decimal('0.000'),)
177991 5 (Decimal('0.024'),)
177991 6 (Decimal('0.034'),)
177991 7 (Decimal('0.018'),)
47830 1 (Decimal('0.003'),)
47830 3 (Decimal('0.000'),)
47830 4 (Decimal('0.000'),)
47830 5 (Decimal('0.007'),)
47830 6 (Decimal('0.002'),)
47830 7 (Decimal('0.012'),)
150215 1 (Decimal('0.008'),)
150215 3 (Decimal('0.000'),)
150215 4 (Decimal('0.000'),)
150215 5 (Decimal('0.012'),)
150215 6 (Decimal('0.002'),)
150215 7 (Decimal('0.025'),)
319860 1 (Decimal('0.007'),)
319860 3 (Decimal('0.000'),)
319860 4 (Decimal('0.000'),)
319860 5 (Decimal('0.002'),)
319860 6 (Decimal('0.000'),)
319860 7 (Decimal('0.005'),)
281165 1 (Decimal('0.010'),)
281165 3 (Decimal('0.000'),)
281165 4 (Decimal('0.000'),)
281165 5 (Decimal('0.006'),)
281165 6 (Decimal('0.008'),)
281165 7 (Decimal('0.016'),)
320225 1 (Decimal('0.036'),)
320225 3 (Decimal('0.063'),)
320225 4 (Decimal('0.000'),)
320225 5 (Decimal('0.022'),)
320225 6 (Decimal('0.032'),)
320225 7 (Decimal('0.005'),)
'''
plt.subplot(2,5,1)
product_action_top1=[0.040,0.063,0.000,0.050,0.013,0.052]
type_number1=[1,3,4,5,6,7]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.013,0.063,0.000,0.021,0.010,0.028]
type_number2=[1,3,4,5,6,7]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.049,0.000,0.000,0.034,0.074,0.026]
type_number3=[1,3,4,5,6,7]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.031,0.000,0.000,0.024,0.034,0.018]
type_number4=[1,3,4,5,6,7]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.003,0.000,0.000,0.007,0.002,0.012]
type_number5=[1,3,4,5,6,7]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.008,0.000,0.000,0.012,0.002,0.025]
type_number6=[1,3,4,5,6,7]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.007,0.000,0.000,0.002,0.000,0.005]
type_number7=[1,3,4,5,6,7]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.010,0.000,0.000,0.006,0.008,0.016]
type_number9=[1,3,4,5,6,7]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.036,0.063,0.000,0.022,0.032,0.005]
type_number10=[1,3,4,5,6,7]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()









city_level_num=[1,2,3,4,5,6]
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_7=mydb.cursor()
for product_id in product_top10:
    for city_num_level in city_level_num:
        consumer_city_level='SELECT ROUND(T0.num1/T1.num2*100,3)\
                             FROM (SELECT count(*) AS num1\
                                   FROM user\
                                   WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                                   FROM action\
                                   WHERE action.sku_id={y} AND action.type=2\
                                    GROUP BY action.user_id\
                                    HAVING count(*)>1))T0,\
                                   (SELECT count(*) AS num2\
                                    FROM user\
                                    where user.city_level={x}\
                                    AND user.user_id IN (SELECT user_id\
                                    FROM action\
                                    WHERE action.type=2\
                                    GROUP BY action.user_id\
                                    HAVING count(*)>1))T1;'.format(x=city_num_level,y=product_id)
        cursor_7.execute(consumer_city_level)
        consumer_city_level_sql=cursor_7.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(product_id,city_num_level,city_level_result)
cursor_7.close()
'''
81731 1 (Decimal('0.050'),)
81731 2 (Decimal('0.023'),)
81731 3 (Decimal('0.052'),)
81731 4 (Decimal('0.039'),)
81731 5 (Decimal('0.026'),)
81731 6 (Decimal('0.000'),)
281779 1 (Decimal('0.016'),)
281779 2 (Decimal('0.000'),)
281779 3 (Decimal('0.028'),)
281779 4 (Decimal('0.018'),)
281779 5 (Decimal('0.012'),)
281779 6 (Decimal('0.000'),)
167081 1 (Decimal('0.043'),)
167081 2 (Decimal('0.046'),)
167081 3 (Decimal('0.043'),)
167081 4 (Decimal('0.033'),)
167081 5 (Decimal('0.050'),)
167081 6 (Decimal('0.094'),)
177991 1 (Decimal('0.036'),)
177991 2 (Decimal('0.069'),)
177991 3 (Decimal('0.024'),)
177991 4 (Decimal('0.018'),)
177991 5 (Decimal('0.021'),)
177991 6 (Decimal('0.283'),)
47830 1 (Decimal('0.007'),)
47830 2 (Decimal('0.023'),)
47830 3 (Decimal('0.008'),)
47830 4 (Decimal('0.004'),)
47830 5 (Decimal('0.007'),)
47830 6 (Decimal('0.000'),)
150215 1 (Decimal('0.012'),)
150215 2 (Decimal('0.000'),)
150215 3 (Decimal('0.023'),)
150215 4 (Decimal('0.013'),)
150215 5 (Decimal('0.003'),)
150215 6 (Decimal('0.000'),)
319860 1 (Decimal('0.009'),)
319860 2 (Decimal('0.000'),)
319860 3 (Decimal('0.002'),)
319860 4 (Decimal('0.004'),)
319860 5 (Decimal('0.000'),)
319860 6 (Decimal('0.094'),)
281165 1 (Decimal('0.007'),)
281165 2 (Decimal('0.000'),)
281165 3 (Decimal('0.016'),)
281165 4 (Decimal('0.009'),)
281165 5 (Decimal('0.010'),)
281165 6 (Decimal('0.000'),)
320225 1 (Decimal('0.027'),)
320225 2 (Decimal('0.000'),)
320225 3 (Decimal('0.021'),)
320225 4 (Decimal('0.024'),)
320225 5 (Decimal('0.021'),)
320225 6 (Decimal('0.000'),)
'''
plt.subplot(2,5,1)
product_action_top1=[0.050,0.023,0.052,0.039,0.026,0.000]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.016,0.000,0.028,0.018,0.012,0.000]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.043,0.046,0.043,0.033,0.050,0.094]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.036,0.069,0.024,0.018,0.021,0.283]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.007,0.023,0.008,0.004,0.007,0.000]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.012,0.000,0.023,0.013,0.003,0.000]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.009,0.000,0.002,0.004,0.000,0.094]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.007,0.000,0.016,0.009,0.010,0.000]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.027,0.000,0.021,0.024,0.021,0.000]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()






product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
age_list=[1,2,3,4,5,6]
cursor_8=mydb.cursor()
for product_id in product_top10:
    for age_num in age_list:
        consumer_order_age='SELECT ROUND(T0.num1/T1.num2*100,3)\
                            FROM (SELECT count(*) AS num1\
                                FROM user\
                                WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.sku_id={x} AND action.type=2\
                                GROUP BY action.user_id\
                                HAVING count(*)>1)\
                                AND user.age={y})T0,\
                                (SELECT count(*) AS num2\
                                 FROM user\
                                 WHERE user_id IN (SELECT user_id\
                                FROM action\
                                WHERE action.type=2\
                                GROUP BY action.user_id\
                                HAVING count(*)>1)\
                                AND user.age={y})T1;'.format(x=product_id,y=age_num)
        cursor_8.execute(consumer_order_age)
        consumer_order_age_sql=cursor_8.fetchall()
        for order_age_result in consumer_order_age_sql:
            print(product_id,age_num,order_age_result)
cursor_8.close()
'''
81731 1 (Decimal('0.012'),)
81731 2 (Decimal('0.030'),)
81731 3 (Decimal('0.000'),)
81731 4 (Decimal('0.043'),)
81731 5 (Decimal('0.053'),)
81731 6 (Decimal('0.035'),)
281779 1 (Decimal('0.004'),)
281779 2 (Decimal('0.011'),)
281779 3 (Decimal('0.000'),)
281779 4 (Decimal('0.004'),)
281779 5 (Decimal('0.020'),)
281779 6 (Decimal('0.028'),)
167081 1 (Decimal('0.045'),)
167081 2 (Decimal('0.079'),)
167081 3 (Decimal('0.000'),)
167081 4 (Decimal('0.018'),)
167081 5 (Decimal('0.020'),)
167081 6 (Decimal('0.070'),)
177991 1 (Decimal('0.012'),)
177991 2 (Decimal('0.019'),)
177991 3 (Decimal('0.000'),)
177991 4 (Decimal('0.029'),)
177991 5 (Decimal('0.023'),)
177991 6 (Decimal('0.035'),)
47830 1 (Decimal('0.004'),)
47830 2 (Decimal('0.004'),)
47830 3 (Decimal('0.000'),)
47830 4 (Decimal('0.004'),)
47830 5 (Decimal('0.008'),)
47830 6 (Decimal('0.008'),)
150215 1 (Decimal('0.008'),)
150215 2 (Decimal('0.000'),)
150215 3 (Decimal('0.000'),)
150215 4 (Decimal('0.004'),)
150215 5 (Decimal('0.014'),)
150215 6 (Decimal('0.018'),)
319860 1 (Decimal('0.000'),)
319860 2 (Decimal('0.004'),)
319860 3 (Decimal('0.000'),)
319860 4 (Decimal('0.000'),)
319860 5 (Decimal('0.004'),)
319860 6 (Decimal('0.006'),)
281165 1 (Decimal('0.012'),)
281165 2 (Decimal('0.015'),)
281165 3 (Decimal('0.000'),)
281165 4 (Decimal('0.000'),)
281165 5 (Decimal('0.012'),)
281165 6 (Decimal('0.009'),)
320225 1 (Decimal('0.004'),)
320225 2 (Decimal('0.026'),)
320225 3 (Decimal('0.000'),)
320225 4 (Decimal('0.018'),)
320225 5 (Decimal('0.019'),)
320225 6 (Decimal('0.033'),)
'''
plt.subplot(2,5,1)
product_action_top1=[0.012,0.030,0.000,0.043,0.053,0.035]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[0.004,0.011,0.000,0.004,0.020,0.028]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[0.045,0.079,0.000,0.018,0.020,0.070]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[0.012,0.019,0.000,0.029,0.023,0.035]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[0.004,0.004,0.000,0.004,0.008,0.008]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[0.008,0.000,0.000,0.004,0.014,0.018]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[0.000,0.004,0.000,0.000,0.004,0.006]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[0.012,0.015,0.000,0.000,0.012,0.009]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[0.004,0.026,0.000,0.018,0.019,0.033]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()







#find the top 10 cities with the most users
top10_city='SELECT city,count(*)\
            FROM user\
            GROUP BY city\
            ORDER BY count(*)desc\
            LIMIT 10'
top10_city_sql=pd.read_sql_query(top10_city,mydb)
print(top10_city_sql)
'''
    city  count(*)
0  348.0    163225
1  204.0     85497
2  174.0     71555
3  119.0     69210
4  283.0     45903
5  120.0     38453
6   41.0     37551
7   88.0     33452
8  191.0     29659
9  331.0     28519
'''

product_top10=['348','204','174','119','283','120','41','88','191','331']
num_corr=[163225,85497,71555,69210,45903,38453,37551,33452,29659,28519]
ypos=np.arange(len(product_top10))
plt.xticks(ypos,product_top10)
plt.bar(ypos,num_corr)
plt.show()



#top10 products do not have age 3
top10_city_list=[348,204,174,119,283,120,41,88,191,331]
cursor_9=mydb.cursor()
for city_num in top10_city_list:
    age_dist_city='SELECT age,count(*) as number\
                    FROM user\
                    WHERE user.city=%s\
                    GROUP BY user.age'
    cursor_9.execute(age_dist_city,city_num)
    age_dist_city_sql=cursor_9.fetchall()
    for age_dist_city_result in age_dist_city_sql:
        print(city_num,age_dist_city_result)
cursor_9.close()
'''
348 ('6.0', 49329)
348 ('5.0', 71175)
348 ('2.0', 12810)
348 ('1.0', 14851)
348 ('4.0', 14987)
348 ('', 62)
348 ('3.0', 11)
204 ('6.0', 26508)
204 ('2.0', 6755)
204 ('5.0', 35942)
204 ('4.0', 7712)
204 ('1.0', 8519)
204 ('', 60)
204 ('3.0', 1)
174 ('6.0', 19800)
174 ('5.0', 32291)
174 ('4.0', 10225)
174 ('2.0', 4892)
174 ('1.0', 4318)
174 ('', 21)
174 ('3.0', 8)
119 ('4.0', 9033)
119 ('6.0', 18852)
119 ('5.0', 33916)
119 ('1.0', 3228)
119 ('2.0', 4142)
119 ('', 27)
119 ('3.0', 12)
283 ('2.0', 3296)
283 ('1.0', 3220)
283 ('6.0', 11578)
283 ('4.0', 7113)
283 ('5.0', 20664)
283 ('', 31)
283 ('3.0', 1)
120 ('6.0', 11517)
120 ('2.0', 2437)
120 ('4.0', 5800)
120 ('5.0', 17134)
120 ('1.0', 1548)
120 ('', 17)
41 ('4.0', 3741)
41 ('6.0', 11157)
41 ('5.0', 16395)
41 ('1.0', 3257)
41 ('2.0', 2962)
41 ('', 37)
41 ('3.0', 2)
88 ('5.0', 16278)
88 ('2.0', 1982)
88 ('4.0', 3916)
88 ('6.0', 9436)
88 ('1.0', 1814)
88 ('', 26)
191 ('2.0', 2457)
191 ('5.0', 12731)
191 ('1.0', 2312)
191 ('6.0', 7451)
191 ('4.0', 4683)
191 ('', 25)
331 ('5.0', 13748)
331 ('6.0', 7305)
331 ('1.0', 1693)
331 ('4.0', 3797)
331 ('3.0', 1)
331 ('2.0', 1958)
331 ('', 17)
'''
plt.subplot(2,5,1)
product_action_top1=[14851,12810,0,14987,71175,49329]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('city:348')

plt.subplot(2,5,2)
product_action_top2=[8519,6755,1,7712,35942,26508]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('city:204')

plt.subplot(2,5,3)
product_action_top3=[4318,4892,8,10225,32291,19800]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('city:174')

plt.subplot(2,5,4)
product_action_top4=[3228,4142,12,9033,33916,18852]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('city:119')

plt.subplot(2,5,5)
product_action_top5=[3220,3296,1,7113,20664,11578]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('city:283')

plt.subplot(2,5,6)
product_action_top6=[1548,2437,0,5800,17134,11517]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('city:120')

plt.subplot(2,5,7)
product_action_top7=[3257,2962,2,3741,16395,11157]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('city:41')

plt.subplot(2,5,8)
product_action_top9=[1814,1982,0,3916,16278,9436]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('city:88')

plt.subplot(2,5,9)
product_action_top8=[2312,2457,0,4683,12731,7451]
type_number8=[1,2,3,4,5,6]
plt.bar(type_number8,product_action_top8)
plt.title('city:191')

plt.subplot(2,5,10)
product_action_top10=[1693,1958,1,3797,13748,7305]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('city:331')
plt.show()







#scan convert to order
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_10=mydb.cursor()
for product_id in product_top10:
    product_action_type='SELECT ROUND(T1.type_count/T0.type_count*100,3)\
                         FROM(SELECT count(*) AS type_count\
                         FROM action\
                         WHERE action.sku_id={x} AND action.type=1)T0,\
                         (SELECT count(*) AS type_count\
                         FROM action\
                         WHERE action.sku_id={x} AND action.type=2)T1'.format(x=product_id)
    cursor_10.execute(product_action_type)
    action_type_product_sql=cursor_10.fetchall()
    for action_type_result in action_type_product_sql:
        print(product_id,action_type_result)
cursor_10.close()
'''
81731 (Decimal('16.395'),)
281779 (Decimal('10.976'),)
167081 (Decimal('36.766'),)
177991 (Decimal('20.399'),)
47830 (Decimal('7.902'),)
150215 (Decimal('10.789'),)
319860 (Decimal('9.531'),)
281165 (Decimal('15.935'),)
320225 (Decimal('17.211'),)
'''
product_top10=['81731','281779','167081','177991','47830','150215','319860','281165','320225']
num_corr=[16.395,10.976,36.766,20.399,7.902,10.789,9.531,15.935,17.211]
ypos=np.arange(len(product_top10))
plt.xticks(ypos,product_top10)
plt.bar(ypos,num_corr)
plt.show()





#add to cart convert to order
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_12=mydb.cursor()
for product_id in product_top10:
    product_action_type='SELECT ROUND(T1.type_count/T0.type_count*100,3)\
                         FROM(SELECT count(*) AS type_count\
                         FROM action\
                         WHERE action.sku_id={x} AND action.type=5)T0,\
                         (SELECT count(*) AS type_count\
                          FROM action\
                          WHERE user_id IN (SELECT user_id\
                                            FROM action\
                                            WHERE action.sku_id={x} AND action.type=5)\
                          AND action.sku_id={x} AND action.type=2)T1'.format(x=product_id)
    cursor_12.execute(product_action_type)
    action_type_product_sql=cursor_12.fetchall()
    for action_type_result in action_type_product_sql:
        print(product_id,action_type_result)
cursor_12.close()
'''
81731 (Decimal('58.352'),)
281779 (Decimal('52.273'),)
167081 (Decimal('59.109'),)
177991 (Decimal('58.824'),)
47830 (Decimal('35.000'),)
150215 (Decimal('44.583'),)
319860 (Decimal('21.429'),)
281165 (Decimal('59.483'),)
320225 (Decimal('62.937'),)
'''
product_top10=['81731','281779','167081','177991','47830','150215','319860','281165','320225']
num_corr=[58.352,52.273,59.109,58.824,35.000,44.583,21.429,59.483,62.937]
ypos=np.arange(len(product_top10))
plt.xticks(ypos,product_top10)
plt.bar(ypos,num_corr)
plt.show()






#produt info distribution in cities
top10_city_list=[348,204,174,119,283,120,41,88,191,331]
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_13=mydb.cursor()
for city_num in top10_city_list:
    for product_id in product_top10:
        product_action_type='SELECT ROUND(T1.type_count/T0.type_count*100,3)\
                            FROM(SELECT count(*) AS type_count\
                            FROM action\
                            WHERE action.sku_id={x} AND action.type=1\
                            AND user_id IN(SELECT user_id\
                            FROM user\
                            WHERE user.city={y}))T0,\
                            (SELECT count(*) AS type_count\
                            FROM action\
                            WHERE action.sku_id={x} AND action.type=2\
                            AND user_id IN(SELECT user_id\
                            FROM user\
                            WHERE user.city={y}))T1'.format(x=product_id,y=city_num)
        cursor_13.execute(product_action_type)
        action_type_product_sql=cursor_13.fetchall()
        for action_type_result in action_type_product_sql:
            print(product_id,city_num,action_type_result)
cursor_13.close()
'''
81731 348 (Decimal('17.265'),)
281779 348 (Decimal('8.573'),)
167081 348 (Decimal('28.113'),)
177991 348 (Decimal('19.683'),)
47830 348 (Decimal('5.517'),)
150215 348 (Decimal('11.761'),)
319860 348 (Decimal('9.190'),)
281165 348 (Decimal('14.958'),)
320225 348 (Decimal('10.820'),)
81731 204 (Decimal('19.036'),)
281779 204 (Decimal('12.984'),)
167081 204 (Decimal('25.379'),)
177991 204 (Decimal('23.121'),)
47830 204 (Decimal('7.495'),)
150215 204 (Decimal('10.326'),)
319860 204 (Decimal('8.533'),)
281165 204 (Decimal('13.911'),)
320225 204 (Decimal('13.284'),)
81731 174 (Decimal('16.951'),)
281779 174 (Decimal('9.621'),)
167081 174 (Decimal('38.557'),)
177991 174 (Decimal('24.553'),)
47830 174 (Decimal('8.399'),)
150215 174 (Decimal('12.531'),)
319860 174 (Decimal('8.387'),)
281165 174 (Decimal('18.266'),)
320225 174 (Decimal('20.102'),)
81731 119 (Decimal('17.324'),)
281779 119 (Decimal('12.500'),)
167081 119 (Decimal('38.462'),)
177991 119 (Decimal('28.067'),)
47830 119 (Decimal('9.190'),)
150215 119 (Decimal('13.112'),)
319860 119 (Decimal('12.797'),)
281165 119 (Decimal('17.209'),)
320225 119 (Decimal('20.134'),)
81731 283 (Decimal('19.347'),)
281779 283 (Decimal('11.192'),)
167081 283 (Decimal('42.857'),)
177991 283 (Decimal('24.473'),)
47830 283 (Decimal('6.584'),)
150215 283 (Decimal('13.366'),)
319860 283 (Decimal('8.372'),)
281165 283 (Decimal('15.556'),)
320225 283 (Decimal('10.390'),)
81731 120 (Decimal('16.333'),)
281779 120 (Decimal('12.542'),)
167081 120 (Decimal('41.864'),)
177991 120 (Decimal('25.691'),)
47830 120 (Decimal('6.907'),)
150215 120 (Decimal('12.821'),)
319860 120 (Decimal('10.787'),)
281165 120 (Decimal('17.358'),)
320225 120 (Decimal('19.792'),)
81731 41 (Decimal('16.153'),)
281779 41 (Decimal('8.681'),)
167081 41 (Decimal('28.488'),)
177991 41 (Decimal('14.154'),)
47830 41 (Decimal('5.090'),)
150215 41 (Decimal('9.559'),)
319860 41 (Decimal('7.855'),)
281165 41 (Decimal('14.885'),)
320225 41 (Decimal('12.033'),)
81731 88 (Decimal('18.310'),)
281779 88 (Decimal('9.408'),)
167081 88 (Decimal('28.571'),)
177991 88 (Decimal('21.512'),)
47830 88 (Decimal('11.616'),)
150215 88 (Decimal('11.881'),)
319860 88 (Decimal('13.253'),)
281165 88 (Decimal('14.535'),)
320225 88 (Decimal('14.141'),)
81731 191 (Decimal('15.385'),)
281779 191 (Decimal('10.849'),)
167081 191 (Decimal('44.444'),)
177991 191 (Decimal('13.333'),)
47830 191 (Decimal('9.220'),)
150215 191 (Decimal('10.309'),)
319860 191 (Decimal('9.244'),)
281165 191 (Decimal('14.130'),)
320225 191 (Decimal('20.183'),)
81731 331 (Decimal('15.170'),)
281779 331 (Decimal('9.483'),)
167081 331 (Decimal('35.714'),)
177991 331 (Decimal('15.926'),)
47830 331 (Decimal('5.519'),)
150215 331 (Decimal('12.132'),)
319860 331 (Decimal('7.280'),)
281165 331 (Decimal('12.766'),)
320225 331 (Decimal('12.435'),)
'''
plt.subplot(2,5,1)
product_action_top1=[17.265,8.573,28.113,19.683,5.517,11.761,9.190,14.958,10.820]
type_number1=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number1,product_action_top1)
plt.title('city:348')

plt.subplot(2,5,2)
product_action_top2=[19.036,12.984,25.379,23.121,7.495,10.326,8.533,13.911,13.284]
type_number2=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number2,product_action_top2)
plt.title('city:204')

plt.subplot(2,5,3)
product_action_top3=[16.951,9.621,38.557,24.553,8.339,12.531,8.387,18.266,20.102]
type_number3=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number3,product_action_top3)
plt.title('city:174')

plt.subplot(2,5,4)
product_action_top4=[17.324,12.500,38.462,28.067,9.190,13.112,12.797,17.209,20.134]
type_number4=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number4,product_action_top4)
plt.title('city:119')

plt.subplot(2,5,5)
product_action_top5=[19.347,11.192,42.857,24.473,6.584,13.366,8.372,15.556,10.390]
type_number5=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number5,product_action_top5)
plt.title('city:283')

plt.subplot(2,5,6)
product_action_top6=[16.333,12.542,41.864,25.691,6.907,12.821,10.787,17.358,19.792]
type_number6=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number6,product_action_top6)
plt.title('city:120')


plt.subplot(2,5,7)
product_action_top7=[16.153,8.681,28.488,14.154,5.090,9.559,7.855,14.885,12.033]
type_number7=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number7,product_action_top7)
plt.title('city:41')

plt.subplot(2,5,8)
product_action_top9=[18.310,9.408,28.571,21.512,11.616,11.881,13.253,14.535,14.141]
type_number9=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number9,product_action_top9)
plt.title('city:88')

plt.subplot(2,5,9)
product_action_top8=[15.385,10.849,44.444,13.333,9.220,10.309,9.244,14.130,20.183]
type_number8=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number8,product_action_top8)
plt.title('city:191')

plt.subplot(2,5,10)
product_action_top10=[15.170,9.483,35.714,15.926,5.519,12.132,7.280,12.766,12.435]
type_number10=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number10,product_action_top10)
plt.title('city:331')
plt.show()






top10_city_list=[348,204,174,119,283,120,41,88,191,331]
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_14=mydb.cursor()
for city_num in top10_city_list:
    for product_id in product_top10:
        product_action_type='SELECT ROUND(T1.type_count/T0.type_count*100,3)\
                            FROM(SELECT count(*) AS type_count\
                            FROM action\
                            WHERE action.sku_id={x} AND action.type=5\
                            AND user_id IN(SELECT user_id\
                            FROM user\
                            WHERE user.city={y}))T0,\
                            (SELECT count(*) AS type_count\
                            FROM action\
                            WHERE user_id IN (SELECT user_id\
                                            FROM action\
                                            WHERE action.sku_id={x} AND action.type=5)\
                                            AND action.sku_id={x} AND action.type=2\
                                            AND user_id IN(SELECT user_id\
                                            FROM user\
                                            WHERE user.city={y}))T1'.format(x=product_id,y=city_num)
        cursor_14.execute(product_action_type)
        action_type_product_sql=cursor_14.fetchall()
        for action_type_result in action_type_product_sql:
            print(product_id,city_num,action_type_result)
cursor_14.close()
'''
81731 348 (Decimal('61.765'),)
281779 348 (Decimal('40.000'),)
167081 348 (Decimal('87.500'),)
177991 348 (Decimal('55.000'),)
47830 348 (Decimal('0.000'),)
150215 348 (Decimal('42.105'),)
319860 348 (Decimal('100.000'),)
281165 348 (Decimal('55.000'),)
320225 348 (Decimal('50.000'),)
81731 204 (Decimal('60.714'),)
281779 204 (Decimal('60.000'),)
167081 204 (Decimal('33.333'),)
177991 204 (Decimal('68.750'),)
47830 204 (None,)
150215 204 (Decimal('42.857'),)
319860 204 (None,)
281165 204 (Decimal('60.000'),)
320225 204 (Decimal('0.000'),)
81731 174 (Decimal('68.750'),)
281779 174 (Decimal('50.000'),)
167081 174 (Decimal('64.000'),)
177991 174 (Decimal('66.667'),)
47830 174 (Decimal('25.000'),)
150215 174 (Decimal('52.174'),)
319860 174 (None,)
281165 174 (Decimal('55.556'),)
320225 174 (Decimal('92.308'),)
81731 119 (Decimal('60.000'),)
281779 119 (Decimal('50.000'),)
167081 119 (Decimal('53.571'),)
177991 119 (Decimal('72.727'),)
47830 119 (Decimal('33.333'),)
150215 119 (Decimal('48.000'),)
319860 119 (None,)
281165 119 (Decimal('25.000'),)
320225 119 (Decimal('112.500'),)
81731 283 (Decimal('44.444'),)
281779 283 (Decimal('20.000'),)
167081 283 (Decimal('57.143'),)
177991 283 (Decimal('83.333'),)
47830 283 (None,)
150215 283 (Decimal('33.333'),)
319860 283 (None,)
281165 283 (Decimal('0.000'),)
320225 283 (Decimal('75.000'),)
81731 120 (Decimal('63.158'),)
281779 120 (Decimal('62.500'),)
167081 120 (Decimal('50.000'),)
177991 120 (Decimal('58.333'),)
47830 120 (Decimal('100.000'),)
150215 120 (Decimal('66.667'),)
319860 120 (None,)
281165 120 (Decimal('75.000'),)
320225 120 (Decimal('80.000'),)
81731 41 (Decimal('69.231'),)
281779 41 (Decimal('66.667'),)
167081 41 (Decimal('57.143'),)
177991 41 (Decimal('100.000'),)
47830 41 (Decimal('100.000'),)
150215 41 (Decimal('33.333'),)
319860 41 (None,)
281165 41 (Decimal('50.000'),)
320225 41 (None,)
81731 88 (Decimal('45.455'),)
281779 88 (Decimal('0.000'),)
167081 88 (Decimal('50.000'),)
177991 88 (Decimal('57.143'),)
47830 88 (None,)
150215 88 (Decimal('33.333'),)
319860 88 (None,)
281165 88 (None,)
320225 88 (Decimal('0.000'),)
81731 191 (Decimal('0.000'),)
281779 191 (None,)
167081 191 (Decimal('77.778'),)
177991 191 (None,)
47830 191 (None,)
150215 191 (Decimal('50.000'),)
319860 191 (None,)
281165 191 (Decimal('66.667'),)
320225 191 (Decimal('50.000'),)
81731 331 (Decimal('71.429'),)
281779 331 (Decimal('100.000'),)
167081 331 (Decimal('52.941'),)
177991 331 (Decimal('54.545'),)
47830 331 (None,)
150215 331 (Decimal('0.000'),)
319860 331 (None,)
281165 331 (None,)
320225 331 (Decimal('50.000'),)
'''

plt.subplot(2,5,1)
product_action_top1=[61.765,40.000,87.500,55.000,0.000,42.105,100.000,55.000,50.000]
type_number1=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number1,product_action_top1)
plt.title('city:348')

plt.subplot(2,5,2)
product_action_top2=[60.714,60.000,33.333,68.750,0.000,42.857,0.000,60.000,0.000]
type_number2=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number2,product_action_top2)
plt.title('city:204')

plt.subplot(2,5,3)
product_action_top3=[68.750,50.000,64.000,66.667,25.000,52.174,0.000,55.556,92.308]
type_number3=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number3,product_action_top3)
plt.title('city:174')

plt.subplot(2,5,4)
product_action_top4=[60.000,50.000,53.571,72.727,33.333,48.000,0.000,25.000,112.500]
type_number4=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number4,product_action_top4)
plt.title('city:119')

plt.subplot(2,5,5)
product_action_top5=[44.444,20.000,57.143,83.333,0.000,33.333,0.000,0.000,75.000]
type_number5=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number5,product_action_top5)
plt.title('city:283')

plt.subplot(2,5,6)
product_action_top6=[63.158,62.500,50.000,58.333,100.000,66.667,0.000,75.000,80.000]
type_number6=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number6,product_action_top6)
plt.title('city:120')

plt.subplot(2,5,7)
product_action_top7=[69.231,66.667,57.143,100.000,10.000,33.333,0.000,50.000,0.000]
type_number7=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number7,product_action_top7)
plt.title('city:41')

plt.subplot(2,5,8)
product_action_top9=[45.455,0.000,50.000,57.143,0.000,33.333,0.000,0.000,0.000]
type_number9=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number9,product_action_top9)
plt.title('city:88')

plt.subplot(2,5,9)
product_action_top8=[0.000,0.000,77.778,0.000,0.000,50.000,0.000,66.667,50.000]
type_number8=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number8,product_action_top8)
plt.title('city:191')

plt.subplot(2,5,10)
product_action_top10=[71.429,100.000,52.941,54.545,0.000,0.000,0.000,0.000,50.000]
type_number10=[1,2,3,4,5,6,7,8,9]
plt.bar(type_number10,product_action_top10)
plt.title('city:331')
plt.show()
