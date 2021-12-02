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

action_tables=pd.read_sql_query('SHOW TABLES FROM action',mydb)
#print(action_tables)

cate_product='SELECT sku_id AS product_id\
                FROM product\
                WHERE cate=81'
product_cate_id=pd.read_sql_query(cate_product,mydb)
print(product_cate_id)
#the number of cate 81 is 23273

#top 10 products in cate 81
top_cate_product='SELECT sku_id AS product_id, count(*) AS num\
                  FROM action\
                  WHERE sku_id IN (SELECT sku_id AS product_id\
                  FROM product\
                  WHERE cate=81)\
                  GROUP BY sku_id\
                  ORDER BY num desc\
                  LIMIT 10'
cate_product_top_sql=pd.read_sql_query(top_cate_product,mydb)
print(cate_product_top_sql)
'''
  product_id    num
0       81731  25650
1      281779  22807
2      167081  15816
3      177991  15419
4       47830  13604
5      150215  12963
6      319860  11713
7       32167  10770
8      281165  10666
9      320225  10426
'''
#draw the plot
product_top10=['81731','281779','167081','177991','47830','150215','319860','32167','281165','320225']
num_corr=[25650,22807,15816,15419,13604,12963,11713,10770,10666,10426]
ypos=np.arange(len(product_top10))
plt.xticks(ypos,product_top10)
plt.bar(ypos,num_corr)
plt.show()

#top 10 products users action distribution 
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_1=mydb.cursor()
for product_id in product_top10:
    product_action_type='SELECT type, count(*) AS type_count\
                         FROM action\
                         WHERE action.sku_id=%s\
                         GROUP BY action.type'
    cursor_1.execute(product_action_type,product_id)
    action_type_product_sql=cursor_1.fetchall()
    for action_type_result in action_type_product_sql:
        print(action_type_result)
cursor_1.close()
#1:scan 2:order 3:follow 4:comment 5:add to cart
'''
product 81731
(1, 20891)
(2, 3425)
(4, 627)
(3, 270)
(5, 437)
product 281779
(1, 19597)
(2, 2151)
(4, 636)
(3, 247)
(5, 176)
product 167081 
(1, 10545)
(2, 3877)
(4, 810)
(5, 494)
(3, 90)
product 177991
(1, 12035)
(2, 2455)
(5, 272)
(4, 515)
(3, 142)
product 47830
(1, 12123)
(2, 958)
(3, 147)
(4, 336)
(5, 40)
product 150215 
(1, 11141)
(2, 1202)
(5, 240)
(4, 291)
(3, 89)
product 319860
(1, 10356)
(2, 987)
(4, 281)
(3, 75)
(5, 14)
product 32167
(1, 10494)
(3, 118)
(5, 69)
(4, 89)
product 281165
(1, 8748)
(2, 1394)
(4, 300)
(5, 116)
(3, 108)
product 320225
(1, 8419)
(2, 1449)
(4, 319)
(3, 96)
(5, 143)
'''
#draw the plot
plt.subplot(2,5,1)
product_action_top1=[20891,3425,627,270,437]
type_number1=[1,2,4,3,5]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[19597,2151,636,247,176]
type_number2=[1,2,4,3,5]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[10545,3877,810,494,90]
type_number3=[1,2,4,5,3]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[12035,2455,272,515,142]
type_number4=[1,2,5,4,3]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[12123,958,147,336,40]
type_number5=[1,2,3,4,5]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[11141,1202,240,291,89]
type_number6=[1,2,5,4,3]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[10356,987,281,75,14]
type_number7=[1,2,4,3,5]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top8=[10494,118,69,89,0]
type_number8=[1,3,5,4,2]
plt.bar(type_number8,product_action_top8,color='#fc031c')
plt.title('product:32167')

plt.subplot(2,5,9)
product_action_top9=[8748,1394,300,116,108]
type_number9=[1,2,4,5,3]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,10)
product_action_top10=[8419,1449,319,96,143]
type_number10=[1,2,4,3,5]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()

#the age distribution of top 10 products
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_2=mydb.cursor()
for product_id in product_top10:
    consumer_order_age='SELECT age,count(*) AS number\
                        FROM user\
                        WHERE user_id IN (SELECT user_id\
                        FROM action\
                        WHERE action.sku_id=%s AND action.type=2)\
                        GROUP BY user.age'
    cursor_2.execute(consumer_order_age,product_id)
    consumer_order_age_sql=cursor_2.fetchall()
    for order_age_result in consumer_order_age_sql:
        print(order_age_result)
cursor_2.close()
#because the product 32167 does not have the order, so it is empty
'''
product:81731
('', 2)
('6.0', 820)
('4.0', 350)
('5.0', 1868)
('2.0', 124)
('1.0', 100)
product:281779
('5.0', 981)
('6.0', 698)
('2.0', 144)
('4.0', 157)
('1.0', 105)
product:167081
('1.0', 314)
('5.0', 1135)
('6.0', 1570)
('2.0', 439)
('4.0', 278)
product:177991
('', 1)
('6.0', 672)
('5.0', 1119)
('4.0', 281)
('2.0', 123)
('1.0', 162)
product:47830
('', 1)
('2.0', 89)
('6.0', 331)
('5.0', 416)
('4.0', 50)
('1.0', 48)
product:150215
('6.0', 382)
('5.0', 588)
('2.0', 58)
('4.0', 79)
('1.0', 48)
product:319860
('5.0', 409)
('6.0', 394)
('2.0', 81)
('4.0', 45)
('1.0', 45)
product:281165
('6.0', 511)
('5.0', 612)
('4.0', 93)
('1.0', 51)
('2.0', 89)
product:320225
('5.0', 569)
('1.0', 62)
('6.0', 471)
('2.0', 117)
('4.0', 138)
'''
#draw the plot to show which age prefer to buy the product
plt.subplot(2,5,1)
product_action_top1=[820,350,1868,124,100,0]
type_number1=[6,4,5,2,1,3]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[981,698,144,157,105,0]
type_number2=[5,6,2,4,1,3]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[314,1135,1570,439,278,0]
type_number3=[1,5,6,2,4,3]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[672,1119,281,123,162,0]
type_number4=[6,5,4,2,1,3]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[89,331,416,50,48,0]
type_number5=[2,6,5,4,1,3]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[382,588,58,79,48,0]
type_number6=[6,5,2,4,1,3]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[409,394,81,45,45,0]
type_number7=[5,6,2,4,1,3]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[511,612,93,51,89,0]
type_number9=[6,5,4,1,2,3]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[569,62,471,117,138,0]
type_number10=[5,1,6,2,4,0]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()
#we can ge the info that age 5 and 6 like to buy these top 10, but no age 3 will buy them

#the gender distribution of top 10 products
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_3=mydb.cursor()
for product_id in product_top10:
    consumer_order_sex='SELECT sex,count(*) AS number\
                        FROM user\
                        WHERE user_id IN (SELECT user_id\
                        FROM action\
                        WHERE action.sku_id=%s AND action.type=2)\
                        GROUP BY user.sex'
    cursor_3.execute(consumer_order_sex,product_id)
    consumer_order_sex_sql=cursor_3.fetchall()
    for order_sex_result in consumer_order_sex_sql:
        print(order_sex_result)
cursor_3.close()
#-1:male 1:female 0:secret
'''
product:81737
('', 2)
('0.0', 2541)
('1.0', 718)
('-1.0', 3)
product:281779
('0.0', 1540)
('1.0', 544)
('-1.0', 1)
product:167081
('0.0', 3120)
('1.0', 600)
('-1.0', 16)
product:177991
('', 1)
('0.0', 1920)
('1.0', 428)
('-1.0', 9)
product:47830
('', 1)
('0.0', 696)
('1.0', 236)
('-1.0', 2)
product:150215
('0.0', 872)
('1.0', 282)
('-1.0', 1)
product:319860
('0.0', 804)
('1.0', 170)
product:281165
('1.0', 322)
('0.0', 1032)
('-1.0', 2)
product:320225
('0.0', 1128)
('1.0', 223)
('-1.0', 6)
'''
#draw the gender plot
plt.subplot(2,5,1)
product_action_top1=[2541,718,3]
type_number1=[0,1,-1]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[1540,544,1]
type_number2=[0,1,-1]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[3120,600,16]
type_number3=[0,1,-1]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[1920,428,9]
type_number4=[0,1,-1]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[696,236,2]
type_number5=[0,1,-1]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[872,282,1]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top6=[804,170,0]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[322,1032,2]
type_number9=[1,0,-1]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[1128,223,6]
type_number10=[0,1,-1]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()
#i do not think the gender data make sence because large parts of people choose keep their gender secret
# we can find more female prefer to buy thenr top 10 goods than males.


#find the earliest time in USER
find_min_date='SELECT MIN(user_reg_tm)\
               FROM user'
min_date_sql=pd.read_sql_query(find_min_date,mydb)
print(min_date_sql)
#2003-06-13 06:19:45


#add one column reg_level to show the level of customers participating time

null_num_in_product='SELECT count(*) AS num\
                     FROM user\
                     WHERE user_id IN (SELECT user_id\
                     FROM action\
                     WHERE action.sku_id IN (81731,281779,167081,177991,47830,150215,319860,32167,281165,320225)\
                     AND action.type = 2)\
                     AND user_reg_tm IS NULL'
null_num_of_time_sql=pd.read_sql_query(null_num_in_product,mydb)
print(null_num_of_time_sql)
#0 there is no row with null time


'''
2003:0
2004:0
2005:1
2006:7
2007:22
2008:121
2009:222
2010:546
2011:1098
2012:1460
2013:1538
2014:2320
2015:3084
2016:2801
2017:2512
2018:928
'''
reg_level_year=[0,0,1,7,22,121,222,546,1098,1460,1538,2320,3084,2801,2512,928]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('registration year distribution')
plt.show()
#notice: 2018 only have the data until april

product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
cursor_4=mydb.cursor()
for product_id in product_top10:
    for year_list in year_dist:
        consumer_reg_tm='SELECT count(*) AS num\
                        FROM user\
                        WHERE user_id IN (SELECT user_id\
                        FROM action\
                        WHERE action.sku_id ={x}\
                        AND action.type = 2)\
                        AND YEAR(user_reg_tm)={y}'.format(x=product_id,y=year_list)
        cursor_4.execute(consumer_reg_tm)
        consumer_reg_tm_sql=cursor_4.fetchall()
        for consumer_reg_tm_result in consumer_reg_tm_sql:
            print(consumer_reg_tm_result)
cursor_4.close()     
 
'''
product:81731
(0,)2003
(0,)2004
(0,)2005
(4,)2006
(5,)2007
(25,)2008
(48,)2009
(125,)2010
(270,)2011
(356,)2012
(356,)2013
(509,)2014
(588,)2015
(501,)2016
(372,)2017
(105,)2018

product:281779
(0,)
(0,)
(0,)
(1,)
(3,)
(17,)
(31,)
(79,)
(165,)
(176,)
(216,)
(303,)
(347,)
(325,)
(329,)
(93,)

product:167081
(0,)
(0,)
(0,)
(2,)
(4,)
(17,)
(30,)
(64,)
(151,)
(226,)
(231,)
(485,)
(722,)
(718,)
(694,)
(392,)

product:177991
(0,)
(0,)
(0,)
(0,)
(0,)
(10,)
(26,)
(43,)
(125,)
(175,)
(223,)
(329,)
(474,)
(417,)
(396,)
(140,)

product:47830
(0,)
(0,)
(0,)
(0,)
(2,)
(13,)
(17,)
(52,)
(51,)
(91,)
(86,)
(127,)
(156,)
(145,)
(147,)
(48,)

product:150215
(0,)
(0,)
(0,)
(0,)
(3,)
(11,)
(26,)
(73,)
(101,)
(150,)
(133,)
(177,)
(203,)
(140,)
(116,)
(22,)

product:319860
(0,)
(0,)
(0,)
(0,)
(2,)
(11,)
(15,)
(46,)
(89,)
(101,)
(105,)
(141,)
(168,)
(160,)
(118,)
(18,)

product:32167
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)

product:281165
(0,)
(0,)
(0,)
(1,)
(1,)
(18,)
(24,)
(67,)
(115,)
(141,)
(143,)
(177,)
(226,)
(207,)
(179,)
(57,)

product:320225
(0,)
(0,)
(1,)
(0,)
(2,)
(5,)
(14,)
(20,)
(75,)
(94,)
(103,)
(147,)
(287,)
(280,)
(248,)
(81,)
'''
plt.subplot(2,3,1)
reg_level_year=[0,0,0,4,5,25,48,125,270,356,356,509,588,501,372,105]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('registration year distribution:81731')

plt.subplot(2,3,2)
reg_level_year=[0,0,0,1,3,17,31,79,165,176,216,303,347,325,329,93]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281779')

plt.subplot(2,3,3)
reg_level_year=[0,0,0,2,4,17,30,64,151,226,231,485,722,718,694,392]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('167081')

plt.subplot(2,3,4)
reg_level_year=[0,0,0,0,0,10,26,43,125,175,223,329,474,417,396,140]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('177991')

plt.subplot(2,3,5)
reg_level_year=[0,0,0,0,2,13,17,52,51,91,86,127,156,145,147,48]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('47830')

plt.subplot(2,3,6)
reg_level_year=[0,0,0,0,3,11,26,73,101,150,133,177,203,140,116,22]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('150215')
plt.show()  

plt.subplot(2,2,1)
reg_level_year=[0,0,0,0,2,11,15,46,89,101,105,141,168,160,118,18]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('319860')

plt.subplot(2,2,2)
reg_level_year=[0,0,0,1,1,18,24,67,115,141,143,177,226,207,179,57]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281165')

plt.subplot(2,2,3)
reg_level_year=[0,0,1,0,2,5,14,20,75,94,103,147,287,280,248,81]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('320225')
plt.show() 


#User level
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_5=mydb.cursor()
for product_id in product_top10:
    consumer_city_level='SELECT user_lv_cd as city_lv,count(*) AS number\
                        FROM user\
                        WHERE user_id IN (SELECT user_id\
                        FROM action\
                        WHERE action.sku_id=%s AND action.type=2)\
                        GROUP BY city_lv'
    cursor_5.execute(consumer_city_level,product_id)
    consumer_city_level_sql=cursor_5.fetchall()
    for city_level_result in consumer_city_level_sql:
        print(city_level_result)
cursor_5.close()
'''
81731
(7, 1046)
(1, 869)
(5, 946)
(6, 393)
(3, 10)

281779
(1, 574)
(5, 564)
(7, 684)
(6, 257)
(3, 6)

167081
(6, 1387)
(7, 564)
(1, 1082)
(5, 651)
(4, 40)
(3, 12)

177991
(2, 1)
(6, 534)
(7, 488)
(1, 760)
(5, 561)
(3, 14)

47830
(7, 345)
(1, 244)
(5, 245)
(6, 98)
(3, 3)

150215
(7, 471)
(1, 267)
(5, 319)
(6, 96)
(3, 2)

319860
(6, 65)
(5, 281)
(7, 402)
(1, 226)

281165
(1, 324)
(7, 478)
(5, 372)
(6, 178)
(3, 3)
(4, 1)

320225
(5, 280)
(1, 467)
(6, 376)
(7, 225)
(3, 8)
(4, 1)
'''

plt.subplot(2,5,1)
product_action_top1=[1046,869,946,393,10,0,0]
type_number1=[7,1,5,6,3,2,4]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[574,564,684,257,6,0,0]
type_number2=[1,5,7,6,3,2,4]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[1387,564,1082,651,40,12,0]
type_number3=[6,7,1,5,4,3,2]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[1,534,488,760,561,14,0]
type_number4=[2,6,7,1,5,3,4]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[234,244,245,98,3,0,0]
type_number5=[7,1,5,6,3,2,4]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[471,267,319,96,2,0,0]
type_number6=[7,1,5,6,3,2,4]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[65,281,402,226,0,0,0]
type_number7=[6,5,7,1,2,3,4]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[324,478,372,178,3,1,2]
type_number9=[1,7,5,6,3,4,2]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[280,467,376,225,8,1,0]
type_number10=[5,1,6,7,3,4,2]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()


#but we find that user_level of 2,3,4 has small amout,so we shou group them by user level except level2
#because level 2 only has 12 data

user_level_num=[1,2,3,4,5,6,7]
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_6=mydb.cursor()
for num_level in user_level_num:
    for product_id in product_top10:
        consumer_user_level='SELECT count(*) AS number\
                            FROM user\
                            WHERE user.user_lv_cd={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id={y} AND action.type=2)'.format(x=num_level,y=product_id)
        cursor_6.execute(consumer_user_level)
        consumer_user_level_sql=cursor_6.fetchall()
        for user_level_result in consumer_user_level_sql:
            print(user_level_result)
cursor_6.close()

'''
user level=1
(869,)
(574,)
(1082,)
(760,)
(244,)
(267,)
(226,)
(0,)
(324,)
(467,)

user level=2
(0,)
(0,)
(0,)
(1,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)

user level=3
(10,)
(6,)
(12,)
(14,)
(3,)
(2,)
(0,)
(0,)
(3,)
(8,)

user level=4
(0,)
(0,)
(40,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(1,)

user level=5
(946,)
(564,)
(651,)
(561,)
(245,)
(319,)
(281,)
(0,)
(372,)
(280,)

user level=6
(393,)
(257,)
(1387,)
(534,)
(98,)
(96,)
(65,)
(0,)
(178,)
(376,)

user level=7
(1046,)
(684,)
(564,)
(488,)
(345,)
(471,)
(402,)
(0,)
(478,)
(225,)
'''

plt.subplot(2,5,1)
product_action_top1=[869,574,1082,760,244,267,226,0,324,467]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('user_level=1')

plt.subplot(2,5,2)
product_action_top2=[0,0,0,1,0,0,0,0,0,0]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('user_level=2')

plt.subplot(2,5,3)
product_action_top3=[10,6,12,14,3,2,0,0,3,8]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('user_level=3')

plt.subplot(2,5,4)
product_action_top4=[0,0,40,0,0,0,0,0,1,1]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('user_level=4')

plt.subplot(2,5,5)
product_action_top5=[946,564,651,561,245,319,281,0,372,280]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('user_level=5')

plt.subplot(2,5,6)
product_action_top6=[392,257,1387,534,98,96,65,0,178,376]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('user_level=6')

plt.subplot(2,5,7)
product_action_top7=[1046,684,564,488,345,471,402,0,478,225]
type_number7=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number7,product_action_top7)
plt.title('user_level=7')
plt.show()



#city level
city_level_num=[1,2,3,4,5,6]
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_7=mydb.cursor()
for city_num_level in city_level_num:
    for product_id in product_top10:
        consumer_city_level='SELECT count(*) AS number\
                            FROM user\
                            WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id={y} AND action.type=2)'.format(x=city_num_level,y=product_id)
        cursor_7.execute(consumer_city_level)
        consumer_city_level_sql=cursor_7.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(city_level_result)
cursor_7.close()
'''
city=1
(668,)
(455,)
(920,)
(518,)
(217,)
(251,)
(215,)
(0,)
(289,)
(325,)

city=2
(33,)
(17,)
(56,)
(40,)
(11,)
(8,)
(11,)
(0,)
(20,)
(18,)

city=3
(925,)
(528,)
(769,)
(631,)
(243,)
(366,)
(262,)
(0,)
(368,)
(313,)

city=4
(1036,)
(611,)
(1017,)
(646,)
(274,)
(331,)
(293,)
(0,)
(390,)
(354,)

city=5
(593,)
(463,)
(961,)
(516,)
(186,)
(198,)
(188,)
(0,)
(285,)
(339,)

city=6
(5,)
(9,)
(11,)
(6,)
(3,)
(1,)
(4,)
(0,)
(3,)
(8,)
'''

plt.subplot(2,5,1)
product_action_top1=[688,455,920,518,217,251,215,0,289,325]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('city_level=1')

plt.subplot(2,5,2)
product_action_top2=[33,17,56,40,11,8,11,0,20,18]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('city_level=2')

plt.subplot(2,5,3)
product_action_top3=[925,528,769,631,243,366,262,0,368,313]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('city_level=3')

plt.subplot(2,5,4)
product_action_top4=[1036,611,1017,646,274,331,293,0,390,354]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('city_level=4')

plt.subplot(2,5,5)
product_action_top5=[593,463,961,516,186,198,188,0,285,339]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('city_level=5')

plt.subplot(2,5,6)
product_action_top6=[5,9,11,6,3,1,4,0,3,8]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('city_level=6')
plt.show()


#put the city level into x-axis
city_level_num=[1,2,3,4,5,6]
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_8=mydb.cursor()
for product_id in product_top10:
    for city_num_level in city_level_num:
        consumer_city_level='SELECT count(*) AS number\
                            FROM user\
                            WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id={y} AND action.type=2)'.format(x=city_num_level,y=product_id)
        cursor_8.execute(consumer_city_level)
        consumer_city_level_sql=cursor_8.fetchall()
        for city_level_result in consumer_city_level_sql:
            print(city_level_result)
cursor_8.close()
'''
(668,)
(33,)
(925,)
(1036,)
(593,)
(5,)

(455,)
(17,)
(528,)
(611,)
(463,)
(9,)

(920,)
(56,)
(769,)
(1017,)
(961,)
(11,)

(518,)
(40,)
(631,)
(646,)
(516,)
(6,)

(217,)
(11,)
(243,)
(274,)
(186,)
(3,)

(251,)
(8,)
(366,)
(331,)
(198,)
(1,)

(215,)
(11,)
(262,)
(293,)
(188,)
(4,)

(289,)
(20,)
(368,)
(390,)
(285,)
(3,)

(325,)
(18,)
(313,)
(354,)
(339,)
(8,)
'''
plt.subplot(2,5,1)
product_action_top1=[668,33,925,1036,593,5]
type_number1=[1,2,3,4,5,6]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')

plt.subplot(2,5,2)
product_action_top2=[455,17,528,611,463,9]
type_number2=[1,2,3,4,5,6]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')

plt.subplot(2,5,3)
product_action_top3=[920,56,769,1017,961,11]
type_number3=[1,2,3,4,5,6]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')

plt.subplot(2,5,4)
product_action_top4=[518,40,631,646,516,6]
type_number4=[1,2,3,4,5,6]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')

plt.subplot(2,5,5)
product_action_top5=[217,11,243,274,186,3]
type_number5=[1,2,3,4,5,6]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')

plt.subplot(2,5,6)
product_action_top6=[251,8,366,331,198,1]
type_number6=[1,2,3,4,5,6]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')

plt.subplot(2,5,7)
product_action_top7=[215,11,262,293,188,4]
type_number7=[1,2,3,4,5,6]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')

plt.subplot(2,5,8)
product_action_top9=[289,20,368,390,285,3]
type_number9=[1,2,3,4,5,6]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')

plt.subplot(2,5,9)
product_action_top10=[325,18,313,354,339,8]
type_number10=[1,2,3,4,5,6]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()



#find that features for people who buy more than once
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_9=mydb.cursor()
for product_id in product_top10:
    consumer_order2_age='SELECT age,count(*) AS number\
                        FROM user\
                        WHERE user_id IN (SELECT action.user_id\
                        FROM action\
                        WHERE action.sku_id=%s AND action.type=2\
                        GROUP BY action.user_id\
                        HAVING count(*)>1)\
                        GROUP BY user.age'
    cursor_9.execute(consumer_order2_age,product_id)
    consumer_order2_age_sql=cursor_9.fetchall()
    for order2_age_result in consumer_order2_age_sql:
        print(order2_age_result)
cursor_9.close()
'''
('', 1)
('5.0', 78)
('6.0', 35)
('2.0', 8)
('4.0', 12)
('1.0', 3)

('5.0', 29)
('6.0', 28)
('2.0', 3)
('4.0', 1)
('1.0', 1)

('4.0', 5)
('6.0', 71)
('2.0', 21)
('5.0', 29)
('1.0', 11)

('5.0', 33)
('4.0', 8)
('6.0', 35)
('1.0', 3)
('2.0', 5)

('5.0', 11)
('6.0', 8)
('2.0', 1)
('4.0', 1)
('1.0', 1)

('6.0', 18)
('5.0', 21)
('1.0', 2)
('4.0', 1)

('5.0', 6)
('2.0', 1)
('6.0', 6)

('6.0', 9)
('1.0', 3)
('5.0', 18)
('2.0', 4)

('6.0', 33)
('5.0', 28)
('1.0', 1)
('2.0', 7)
('4.0', 5)
'''
plt.subplot(1,2,1)
product_action_top1=[820,350,1868,124,100,0]
type_number1=[6,4,5,2,1,3]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')
plt.subplot(1,2,2)
product_action_top2=[78,35,8,12,3,0]
type_number1=[5,6,2,4,1,3]
plt.bar(type_number1,product_action_top2)
plt.title('product:81731')
plt.show()

plt.subplot(1,2,1)
product_action_top3=[981,698,144,157,105,0]
type_number2=[5,6,2,4,1,3]
plt.bar(type_number2,product_action_top3)
plt.title('product:281779')
plt.subplot(1,2,2)
product_action_top4=[29,28,3,1,1,0]
type_number2=[5,6,2,4,1,3]
plt.bar(type_number2,product_action_top4)
plt.title('product:281779')
plt.show()

plt.subplot(1,2,1)
product_action_top3=[314,1135,1570,439,278,0]
type_number3=[1,5,6,2,4,3]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')
plt.subplot(1,2,2)
product_action_top3=[5,71,21,29,11,0]
type_number3=[4,6,2,5,1,3]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')
plt.show()

plt.subplot(1,2,1)
product_action_top4=[672,1119,281,123,162,0]
type_number4=[6,5,4,2,1,3]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')
plt.subplot(1,2,2)
product_action_top4=[33,8,35,3,5,0]
type_number4=[5,4,6,1,2,3]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')
plt.show()

plt.subplot(1,2,1)
product_action_top5=[89,331,416,50,48,0]
type_number5=[2,6,5,4,1,3]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')
plt.subplot(1,2,2)
product_action_top5=[11,8,1,1,1,0]
type_number5=[5,6,2,4,1,3]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')
plt.show()

plt.subplot(1,2,1)
product_action_top6=[382,588,58,79,48,0]
type_number6=[6,5,2,4,1,3]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.subplot(1,2,2)
product_action_top6=[18,21,2,1,0,0]
type_number6=[6,5,1,4,2,3]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.show()

plt.subplot(1,2,1)
product_action_top7=[409,394,81,45,45,0]
type_number7=[5,6,2,4,1,3]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')
plt.subplot(1,2,2)
product_action_top7=[6,1,6,0,0,0]
type_number7=[5,2,6,1,3,4]
plt.bar(type_number7,product_action_top7)
plt.title('product:319860')
plt.show()

plt.subplot(1,2,1)
product_action_top9=[511,612,93,51,89,0]
type_number9=[6,5,4,1,2,3]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')
plt.subplot(1,2,2)
product_action_top9=[9,3,18,4,0,0]
type_number9=[6,1,5,2,3,4]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')
plt.show()

plt.subplot(1,2,1)
product_action_top10=[569,62,471,117,138,0]
type_number10=[5,1,6,2,4,0]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.subplot(1,2,2)
product_action_top10=[33,28,1,7,5,0]
type_number10=[6,5,1,2,4,3]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()


#the gender distribution
product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
cursor_10=mydb.cursor()
for product_id in product_top10:
    consumer_order2_sex='SELECT sex,count(*) AS number\
                        FROM user\
                        WHERE user_id IN (SELECT action.user_id\
                        FROM action\
                        WHERE action.sku_id=%s AND action.type=2\
                        GROUP BY action.user_id\
                        HAVING count(*)>1)\
                        GROUP BY user.sex'
    cursor_10.execute(consumer_order2_sex,product_id)
    consumer_order2_sex_sql=cursor_10.fetchall()
    for order2_sex_result in consumer_order2_sex_sql:
        print(order2_sex_result)
cursor_10.close()
'''
('', 1)
('1.0', 41)
('0.0', 95)

('0.0', 50)
('1.0', 12)

('0.0', 119)
('1.0', 18)

('0.0', 69)
('1.0', 15)

('0.0', 20)
('1.0', 2)

('0.0', 30)
('1.0', 12)

('0.0', 11)
('1.0', 2)

('0.0', 28)
('1.0', 6)

('0.0', 58)
('1.0', 16)
'''
plt.subplot(1,2,1)
product_action_top1=[2541,718,3]
type_number1=[0,1,-1]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')
plt.subplot(1,2,2)
product_action_top1=[41,95,0]
type_number1=[1,0,-1]
plt.bar(type_number1,product_action_top1)
plt.title('product:81731')
plt.show()

plt.subplot(1,2,1)
product_action_top2=[1540,544,1]
type_number2=[0,1,-1]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')
plt.subplot(1,2,2)
product_action_top2=[50,12,0]
type_number2=[0,1,-1]
plt.bar(type_number2,product_action_top2)
plt.title('product:281779')
plt.show()

plt.subplot(1,2,1)
product_action_top3=[3120,600,16]
type_number3=[0,1,-1]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')
plt.subplot(1,2,2)
product_action_top3=[119,18,0]
type_number3=[0,1,-1]
plt.bar(type_number3,product_action_top3)
plt.title('product:167081')
plt.show()

plt.subplot(1,2,1)
product_action_top4=[1920,428,9]
type_number4=[0,1,-1]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')
plt.subplot(1,2,2)
product_action_top4=[69,15,0]
type_number4=[0,1,-1]
plt.bar(type_number4,product_action_top4)
plt.title('product:177991')
plt.show()

plt.subplot(1,2,1)
product_action_top5=[696,236,2]
type_number5=[0,1,-1]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')
plt.subplot(1,2,2)
product_action_top5=[20,2,0]
type_number5=[0,1,-1]
plt.bar(type_number5,product_action_top5)
plt.title('product:47830')
plt.show()

plt.subplot(1,2,1)
product_action_top6=[872,282,1]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.subplot(1,2,2)
product_action_top6=[30,12,0]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.show()

plt.subplot(1,2,1)
product_action_top6=[872,282,1]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.subplot(1,2,2)
product_action_top6=[11,2,0]
type_number6=[0,1,-1]
plt.bar(type_number6,product_action_top6)
plt.title('product:150215')
plt.show()

plt.subplot(1,2,1)
product_action_top9=[322,1032,2]
type_number9=[1,0,-1]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')
plt.subplot(1,2,2)
product_action_top9=[28,6,0]
type_number9=[0,1,-1]
plt.bar(type_number9,product_action_top9)
plt.title('product:281165')
plt.show()

plt.subplot(1,2,1)
product_action_top10=[1128,223,6]
type_number10=[0,1,-1]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.subplot(1,2,2)
product_action_top10=[58,16,0]
type_number10=[0,1,-1]
plt.bar(type_number10,product_action_top10)
plt.title('product:320225')
plt.show()
#the difference is that no male will buy the second time


product_top10=[81731,281779,167081,177991,47830,150215,319860,281165,320225]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
cursor_11=mydb.cursor()
for product_id in product_top10:
    for year_list in year_dist:
        consumer_reg_tm='SELECT count(*) AS num\
                        FROM user\
                        WHERE user_id IN (SELECT user_id\
                        FROM action\
                        WHERE action.sku_id ={x}\
                        AND action.type = 2\
                        GROUP BY action.user_id\
                        HAVING count(*)>1)\
                        AND YEAR(user_reg_tm)={y}'.format(x=product_id,y=year_list)
        cursor_11.execute(consumer_reg_tm)
        consumer_reg_tm_sql=cursor_11.fetchall()
        for consumer_reg_tm_result in consumer_reg_tm_sql:
            print(consumer_reg_tm_result)
cursor_11.close() 
'''
(0,)
(0,)
(0,)
(0,)
(0,)
(3,)
(2,)
(2,)
(9,)
(16,)
(11,)
(18,)
(28,)
(30,)
(12,)
(6,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(3,)
(4,)
(4,)
(10,)
(13,)
(9,)
(7,)
(9,)
(2,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(2,)
(2,)
(13,)
(10,)
(17,)
(22,)
(36,)
(23,)
(11,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(5,)
(5,)
(5,)
(13,)
(17,)
(17,)
(17,)
(5,)

(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(2,)
(1,)
(2,)
(2,)
(1,)
(3,)
(7,)
(1,)
(1,)
(1,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(2,)
(5,)
(4,)
(5,)
(8,)
(3,)
(12,)
(3,)
(0,)
(0,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(3,)
(1,)
(1,)
(4,)
(0,)
(2,)
(1,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)
(1,)
(3,)
(5,)
(6,)
(4,)
(4,)
(4,)
(4,)
(2,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(5,)
(3,)
(3,)
(7,)
(13,)
(21,)
(18,)
(4,)
'''
plt.subplot(1,2,1)
reg_level_year=[0,0,0,4,5,25,48,125,270,356,356,509,588,501,372,105]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('81731')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,3,2,2,9,16,11,18,28,30,12,6]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('81731')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,1,3,17,31,79,165,176,216,303,347,325,329,93]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281779')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,1,3,4,4,10,13,9,7,9,2]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281779')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,2,4,17,30,64,151,226,231,485,722,718,694,392]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('167081')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,1,2,2,13,10,17,22,36,23,11]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('167081')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,0,0,10,26,43,125,175,223,329,474,417,396,140]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('177991')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,0,0,5,5,5,13,17,17,17,5]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('177991')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,0,2,13,17,52,51,91,86,127,156,145,147,48]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('47830')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,1,2,1,2,2,1,3,7,1,1,1]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('47830')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,0,3,11,26,73,101,150,133,177,203,140,116,22]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('150215')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,2,5,4,5,8,3,12,3,0,0]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('150215')
plt.show()  

plt.subplot(1,2,1)
reg_level_year=[0,0,0,0,2,11,15,46,89,101,105,141,168,160,118,18]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('319860')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,0,0,1,3,1,1,4,0,2,1]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('319860')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,0,1,1,18,24,67,115,141,143,177,226,207,179,57]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281165')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,1,1,3,5,6,4,4,4,4,2]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('281165')
plt.show()

plt.subplot(1,2,1)
reg_level_year=[0,0,1,0,2,5,14,20,75,94,103,147,287,280,248,81]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('320225')
plt.subplot(1,2,2)
reg_level_year=[0,0,0,0,0,0,0,0,5,3,3,7,13,21,18,4]
year_dist=[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
plt.bar(year_dist,reg_level_year)
plt.title('320225')
plt.show() 

#user_level
user_level_num=[1,2,3,4,5,6,7]
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_12=mydb.cursor()
for num_level in user_level_num:
    for product_id in product_top10:
        consumer2_user_level='SELECT count(*) AS number\
                            FROM user\
                            WHERE user.user_lv_cd={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id={y} AND action.type=2\
                            GROUP BY action.user_id\
                            HAVING count(*)>1)'.format(x=num_level,y=product_id)
        cursor_12.execute(consumer2_user_level)
        consumer2_user_level_sql=cursor_12.fetchall()
        for user2_level_result in consumer2_user_level_sql:
            print(user2_level_result)
cursor_12.close()
'''
(37,)
(12,)
(45,)
(28,)
(3,)
(7,)
(6,)
(0,)
(9,)
(33,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)

(1,)
(1,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(1,)

(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)
(0,)

(41,)
(17,)
(28,)
(20,)
(6,)
(10,)
(2,)
(0,)
(5,)
(18,)

(7,)
(5,)
(39,)
(18,)
(1,)
(1,)
(0,)
(0,)
(4,)
(17,)

(51,)
(27,)
(25,)
(18,)
(12,)
(24,)
(5,)
(0,)
(16,)
(5,)
'''
plt.subplot(1,2,1)
product_action_top1=[869,574,1082,760,244,267,226,0,324,467]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('user_level=1')
plt.subplot(1,2,2)
product_action_top1=[37,12,45,28,3,7,6,0,9,33]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('user_level_2=1')
plt.show()

plt.subplot(1,2,1)
product_action_top2=[0,0,0,1,0,0,0,0,0,0]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('user_level=2')
plt.subplot(1,2,2)
product_action_top2=[0,0,0,0,0,0,0,0,0,0]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('user_level_2=2')
plt.show()

plt.subplot(1,2,1)
product_action_top3=[10,6,12,14,3,2,0,0,3,8]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('user_level=3')
plt.subplot(1,2,2)
product_action_top3=[1,1,0,0,0,0,0,0,0,1]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('user_level-2=3')
plt.show()

plt.subplot(1,2,1)
product_action_top4=[0,0,40,0,0,0,0,0,1,1]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('user_level=4')
plt.subplot(1,2,2)
product_action_top4=[0,0,0,0,0,0,0,0,0,0]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('user_level_2=4')
plt.show()

plt.subplot(1,2,1)
product_action_top5=[946,564,651,561,245,319,281,0,372,280]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('user_level=5')
plt.subplot(1,2,2)
product_action_top5=[41,17,28,20,6,10,2,0,5,18]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('user_level_2=5')
plt.show()

plt.subplot(1,2,1)
product_action_top6=[392,257,1387,534,98,96,65,0,178,376]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('user_level=6')
plt.subplot(1,2,2)
product_action_top6=[7,5,39,18,1,1,0,0,4,17]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('user_level_2=6')
plt.show()

plt.subplot(1,2,1)
product_action_top7=[1046,684,564,488,345,471,402,0,478,225]
type_number7=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number7,product_action_top7)
plt.title('user_level=7')
plt.subplot(1,2,2)
product_action_top7=[51,27,25,18,12,24,5,0,16,5]
type_number7=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number7,product_action_top7)
plt.title('user_level_2=7')
plt.show()

#city_level
city_level_num=[1,2,3,4,5,6]
product_top10=[81731,281779,167081,177991,47830,150215,319860,32167,281165,320225]
cursor_13=mydb.cursor()
for city_num_level in city_level_num:
    for product_id in product_top10:
        consumer2_city_level='SELECT count(*) AS number\
                            FROM user\
                            WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.sku_id={y} AND action.type=2\
                            GROUP BY action.user_id\
                            HAVING count(*)>1)'.format(x=city_num_level,y=product_id)
        cursor_13.execute(consumer2_city_level)
        consumer2_city_level_sql=cursor_13.fetchall()
        for city2_level_result in consumer2_city_level_sql:
            print(city2_level_result)
cursor_13.close()
'''
(35,)
(11,)
(30,)
(25,)
(5,)
(8,)
(6,)
(0,)
(5,)
(19,)

(1,)
(0,)
(2,)
(3,)
(1,)
(0,)
(0,)
(0,)
(0,)
(0,)

(45,)
(24,)
(37,)
(21,)
(7,)
(20,)
(2,)
(0,)
(14,)
(18,)

(36,)
(17,)
(31,)
(17,)
(4,)
(12,)
(4,)
(0,)
(8,)
(22,)

(19,)
(9,)
(36,)
(15,)
(5,)
(2,)
(0,)
(0,)
(7,)
(15,)

(0,)
(0,)
(1,)
(3,)
(0,)
(0,)
(1,)
(0,)
(0,)
(0,)
'''
plt.subplot(1,2,1)
product_action_top1=[688,455,920,518,217,251,215,0,289,325]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('city_level=1')
plt.subplot(1,2,2)
product_action_top1=[35,11,30,25,5,8,6,0,5,19]
type_number1=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number1,product_action_top1)
plt.title('city_level_2=1')
plt.show()

plt.subplot(1,2,1)
product_action_top2=[33,17,56,40,11,8,11,0,20,18]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('city_level=2')
plt.subplot(1,2,2)
product_action_top2=[1,0,2,3,1,0,0,0,0,0]
type_number2=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number2,product_action_top2)
plt.title('city_level_2=2')
plt.show()

plt.subplot(1,2,1)
product_action_top3=[925,528,769,631,243,366,262,0,368,313]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('city_level=3')
plt.subplot(1,2,2)
product_action_top3=[45,24,37,21,7,20,2,0,14,18]
type_number3=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number3,product_action_top3)
plt.title('city_level_2=3')
plt.show()

plt.subplot(1,2,1)
product_action_top4=[1036,611,1017,646,274,331,293,0,390,354]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('city_level=4')
plt.subplot(1,2,2)
product_action_top4=[36,17,31,17,4,12,4,0,8,22]
type_number4=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number4,product_action_top4)
plt.title('city_level_2=4')
plt.show()

plt.subplot(1,2,1)
product_action_top5=[593,463,961,516,186,198,188,0,285,339]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('city_level=5')
plt.subplot(1,2,2)
product_action_top5=[19,9,36,15,5,2,0,0,7,15]
type_number5=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number5,product_action_top5)
plt.title('city_level_2=5')
plt.show()

plt.subplot(1,2,1)
product_action_top6=[5,9,11,6,3,1,4,0,3,8]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('city_level=6')
plt.subplot(1,2,2)
product_action_top6=[0,0,1,3,0,0,1,0,0,0]
type_number6=[1,2,3,4,5,6,7,8,9,10]
plt.bar(type_number6,product_action_top6)
plt.title('city_level_2=6')
plt.show()
