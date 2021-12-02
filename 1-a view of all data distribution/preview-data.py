import pymysql
import os
import pandas as pd
import numpy
import matplotlib.pyplot as plot
import seaborn
mydb = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='action'
    )

action_tables=pd.read_sql_query('SHOW TABLES FROM action',mydb)

#action_tables
#schema action info
tables = action_tables['Tables_in_action']
for table_name in tables:
    output=pd.read_sql_query('DESCRIBE {}'.format(table_name),mydb)
    print(table_name)
    print(output)

action_type = 'SELECT action.type AS type, COUNT(*) AS type_count\
               FROM action\
               GROUP BY type\
               ORDER BY type asc'
type_class = pd.read_sql_query(action_type,mydb)
print(type_class)  
#1:scan 2:order 3:follow 4:comment 5:add to cart
'''
   type  type_count
0     1    33151074
1     2     2193489
2     3      441966
3     4      826761
4     5      600979
'''

# find the top/bottom five product choices
action_product_1 = 'SELECT action.sku_id AS product_type, COUNT(*) AS product_count\
               FROM action\
               GROUP BY product_type\
               ORDER BY product_count desc\
               limit 20'
product_class_1 = pd.read_sql_query(action_product_1,mydb)
print(product_class_1) 
'''
    product_type  product_count
0         248051         174313
1         258625          80351
2          31583          66413
3         289214          56244
4         152092          55243
5         224207          54759
6         191016          53285
7         230459          45600
8         217024          41341
9         140105          39686
10         19643          39188
11         16106          38792
12        153599          37491
13        344088          37347
14        360925          37068
15        107331          35510
16        258492          35356
17        171782          34068
18        142280          32080
19        223491          31177
'''
action_product_2 = 'SELECT action.sku_id AS product_type, COUNT(*) AS product_count\
               FROM action\
               GROUP BY product_type\
               ORDER BY product_count asc\
               limit 20'
product_class_2 = pd.read_sql_query(action_product_2,mydb)
print(product_class_2) 
'''
    product_type  product_count
0         256313              1
1         284893              1
2         280602              1
3         320380              1
4         250224              1
5         106062              1
6         163927              1
7         260587              1
8         234603              1
9         324605              1
10        162010              1
11        149067              1
12        328373              1
13        276821              1
14        294122              1
15        261893              1
16         94431              1
17        362039              1
18        297064              1
19        288941              1
'''

#comment info
comment_product_all_1='SELECT comment.sku_id AS product_id, SUM(comment.comments) AS all_comments, SUM(comment.good_comments) AS good, SUM(comment.bad_comments) AS bad\
                    FROM comment\
                    WHERE comment.sku_id IN (248051,258625,31583,289214,152092)\
                    GROUP BY comment.sku_id\
                    ORDER BY all_comments desc'
product_top5_comments=pd.read_sql_query(comment_product_all_1,mydb)
print(product_top5_comments)
'''
   product_id  all_comments     good    bad
0      152092       14996.0  14463.0  253.0
1      248051       10803.0  10599.0  113.0
2      258625        9720.0   9604.0   67.0
3      289214        9463.0   9361.0   59.0
4       31583        8593.0   8397.0  111.0
'''
#good comments are much more than bad ones
comment_product_all_2='SELECT comment.sku_id AS product_id, SUM(comment.comments) AS all_comments, SUM(comment.good_comments) AS good, SUM(comment.bad_comments) AS bad\
                    FROM comment\
                    WHERE comment.sku_id IN (340338,168967,208668,343449,168434)\
                    GROUP BY comment.sku_id\
                    ORDER BY all_comments desc'
product_bottom5_comments=pd.read_sql_query(comment_product_all_2,mydb)
print(product_bottom5_comments)
'''
Empty DataFrame
Columns: [product_id, all_comments, good, bad]
Index: []
'''
# the productID in comment is not full or it means that these products do not have comments.


#product info
product_markettime_1='SELECT YEAR(p.market_time) AS year\
                    FROM product p\
                    WHERE p.sku_id IN (248051,258625,31583,289214,152092)'
product_top5_markettime=pd.read_sql_query(product_markettime_1,mydb)
print(product_top5_markettime)
'''
   year
0  2010
1  2013
2  2014
3  2010
4  2016
'''
product_markettime_2='SELECT YEAR(p.market_time) AS year\
                    FROM product p\
                    WHERE p.sku_id IN (340338,168967,208668,343449,168434)'
product_bottom5_markettime=pd.read_sql_query(product_markettime_2,mydb)
print(product_bottom5_markettime)
'''
   year
0  2017
1  2018
2  2018
3  2018
4  2016
'''
#products with good sales have earlier time to the market than those with bad sales
product_cate='SELECT p.cate\
              FROM product p\
              WHERE p.sku_id IN (248051,258625,31583,289214,152092,224207,191016,230459,217024,140105,19643,16106,153599,344088,360925,107331,258492,171782,142280,223491)\
              GROUP BY p.cate\
              ORDER BY count(*)'
prodcut_action_cate=pd.read_sql_query(product_cate,mydb)
print(prodcut_action_cate)
'''
   cate
0    69
1    55
2    34
3     7
'''
#the category of top 20 product
product_cate_2='SELECT p.cate\
              FROM product p\
              WHERE p.sku_id IN (256313,284893,280602,320380,250224,106062,163927,260587,234603,324605,162010,149067,328373,276821,294122,261893,94431,362039,297064,288941)\
              GROUP BY p.cate\
              ORDER BY count(*)'
prodcut_action_bottom_cate=pd.read_sql_query(product_cate_2,mydb)
print(prodcut_action_bottom_cate)
'''
    cate
0     77
1     49
2     81
3     24
4     27
5     29
6     70
7     14
8     75
9      3
10    67
11    45
12    25
13    68
14    56
15     7
'''
#find that category 7 both exist in two tables.

#product with different shops
product_shop_info='SELECT p.shop_id AS shop\
                   FROM product p\
                   WHERE p.sku_id IN (256313,284893,280602,320380,250224,106062,163927,260587,234603,324605,162010,149067,328373,276821,294122,261893,94431,362039,297064,288941)\
                   GROUP BY shop'
product_top_shop=pd.read_sql_query(product_shop_info,mydb)
print(product_top_shop)
'''
     shop
0    4586
1    6402
2    7563
3    4571
4    1991
5    9708
6    9549
7    1434
8    7242
9   10011
10   4537
11   9932
12    420
13   8077
14   4489
15   6870
16   6509
'''
#top shops corresponding to top 20 product actions.
product_shop_info_2='SELECT p.shop_id AS shop\
                   FROM product p\
                   WHERE p.sku_id IN (256313,284893,280602,320380,250224,106062,163927,260587,234603,324605,162010,149067,328373,276821,294122,261893,94431,362039,297064,288941)\
                   GROUP BY shop'
product_bottom_shop=pd.read_sql_query(product_shop_info_2,mydb)
print(product_bottom_shop)
'''
     shop
0    4586
1    6402
2    7563
3    4571
4    1991
5    9708
6    9549
7    1434
8    7242
9   10011
10   4537
11   9932
12    420
13   8077
14   4489
15   6870
16   6509
'''
#top and bottom are same shop stores.

#shop info
shop_info='SELECT shop_id, fans_num, vip_num, YEAR(shop_reg_tm) AS open_time, shop_score\
           FROM shop\
           ORDER BY fans_num desc\
           LIMIT 20'
shop_top_info=pd.read_sql_query(shop_info,mydb)
print(shop_top_info)
'''
    shop_id  fans_num   vip_num  open_time  shop_score
0     10393   9293487  13841676       2012    9.524399
1      2676   4055951   7311132       2012    9.685927
2      4241   3748112   4868959       2017    9.690087
3      8351   3346267   1665629       2016    9.797118
4      1912   2511707    175996       2015    9.639505
5      5864   2218366   1030803       2018    9.660475
6      3790   2171510    562436       2016    9.760249
7      2149   1569828   1429619       2013    9.615993
8       931   1377103   1109666       2016    9.779993
9      3494   1371624     47026       2015    9.659100
10     9695    996774    633437       2016    9.726270
11     2876    874049     77016       2014    9.388863
12      563    846210    232937       2015    9.573487
13     8925    818073    412683       2013    9.528397
14     1716    810326    338766       2015    9.580392
15     9030    752917   1942664       2013    9.412431
16     6658    740434     87425       2017    9.404424
17      661    721471   1812543       2012    9.620576
18     8238    699027     45550       2014    9.721559
19     1961    650327    909241       2014    9.491085
'''
#these stores has huge fan numbers and high scores
shop_info_2='SELECT shop_id, fans_num, vip_num, YEAR(shop_reg_tm) AS open_time, shop_score\
           FROM shop\
           ORDER BY fans_num asc\
           LIMIT 20'
shop_bottom_info=pd.read_sql_query(shop_info_2,mydb)
print(shop_bottom_info)
'''
    shop_id  fans_num  vip_num open_time  shop_score
0      5330         0        0      None         0.0
1      9445         0        0      None         0.0
2      2189         0        0      None         0.0
3      4280         0        0      None         0.0
4      4130         0        0      None         0.0
5      8831         0        0      None         0.0
6      9645         0        0      None         0.0
7      7278         0        0      None         0.0
8      2232         0        0      None         0.0
9      3334         0        0      None         0.0
10     5523         0        0      None         0.0
11     4500         0        0      None         0.0
12     2480         0        0      None         0.0
13      862         0        0      None         0.0
14     4178         0        0      None         0.0
15     5143         0        0      None         0.0
16     7603         0        0      None         0.0
17     8214         0        0      None         0.0
18     7212         0        0      None         0.0
19     7794         0        0      None         0.0
'''
# may have some null values, they are no reference value

shop_info_year='SELECT shop_id, fans_num, vip_num, YEAR(shop_reg_tm) AS open_time, shop_score\
           FROM shop\
           ORDER BY open_time desc\
           LIMIT 20'
shop_top_opentime_info=pd.read_sql_query(shop_info_year,mydb)
print(shop_top_opentime_info)
'''
   shop_id  fans_num  vip_num  open_time  shop_score
0      9025     23913    16395       2018   10.000000
1      8612        32       35       2018   -1.000000
2      6184       356      488       2018    9.715140
3      5857     11828     2693       2018    9.660500
4      3944    332374    76468       2018    9.496820
5      5458      2600    10119       2018    9.964096
6      8637      1339    41650       2018    9.809818
7      2557      7304    14473       2018    9.868711
8      2674     56338     3658       2018    9.372536
9      6611       833     6469       2018   -1.000000
10    10110        79      577       2018    9.067764
11     4151      1612     9488       2018    9.492322
12    10034       388     5669       2018   -1.000000
13     5850       164      176       2018    9.667254
14     9266       445     3103       2018    8.904498
15     7564       104     1321       2018    9.772339
16     4335       641      587       2018    9.865359
17     6636       450    15327       2018    9.167133
18     8734     20687     5751       2018    9.454771
19     9905       730      228       2018    9.811670
'''
shop_info_year='SELECT AVG(fans_num) AS fans_num_avg, AVG(vip_num) AS vip_num_avg, YEAR(shop_reg_tm) AS open_time, AVG(shop_score) AS score\
                FROM shop\
                WHERE YEAR(shop_reg_tm)IN (2010,2011,2012,2013,2014,2015,2016,2017,2018)\
                GROUP BY YEAR(shop_reg_tm)\
                ORDER BY open_time desc'
shop_top_opentime_info=pd.read_sql_query(shop_info_year,mydb)
print(shop_top_opentime_info)
'''
   fans_num_avg  vip_num_avg  open_time     score
0    15002.5602    9510.3713       2018  7.131176
1    14907.9339   16111.4996       2017  7.907230
2    20957.7315   33078.5740       2016  7.834079
3    22524.8126   56895.3956       2015  7.577819
4    22070.2520   56998.7280       2014  6.822607
5    29551.6912  101131.1290       2013  6.359218
6   115238.6115  247318.8535       2012  6.635966
7    23871.2727  434496.0000       2011  7.607567
8       72.0000   10612.0000       2010 -1.000000
'''
#shop category
shop_info_cate='SELECT cate, count(*) AS store_num\
                FROM shop\
                GROUP BY cate\
                ORDER BY store_num desc'
shop_cate_num=pd.read_sql_query(shop_info_cate,mydb)
print(shop_cate_num)
'''
    cate  store_num
0              2190
1   81.0       1708
2   49.0       1381
3   12.0        906
4   47.0        890
..   ...        ...
85   2.0          1
86  74.0          1
87  56.0          1
88  33.0          1
89  34.0          1
'''
#the top four main business for store and bottom 5 main business.

#user info
user_info_age='SELECT age,count(*) AS num\
           FROM user\
           GROUP BY age\
           ORDER BY num'
user_age_count=pd.read_sql_query(user_info_age,mydb)
print(user_age_count)
'''
   age     num
0  3.0      67
1         2187
2  1.0  117215
3  2.0  120518
4  4.0  210865
5  6.0  438434
6  5.0  719421
'''
user_info_gender='SELECT sex,count(*) AS num\
           FROM user\
           GROUP BY sex\
           ORDER BY num'
user_gender_count=pd.read_sql_query(user_info_gender,mydb)
print(user_gender_count)
'''
    sex     num
0           671
1  -1.0   11866
2   1.0  705867
3   0.0  890303
'''
#-1:male 1:female 0:secret NAN:lost
user_info_regtime='SELECT YEAR(user_reg_tm) AS reg_time,count(*) AS num\
           FROM user\
           GROUP BY reg_time\
           ORDER BY num'
user_regtime_count=pd.read_sql_query(user_info_regtime,mydb)
print(user_regtime_count)
'''
    reg_time     num
0       2003      35
1       2004     124
2       2005     251
3       2006     641
4       2007    1999
5       2008    7678
6       2009   18611
7       2010   43895
8       2011   88866
9       2013  128102
10      2012  129839
11      2018  141966
12      2014  195826
13      2015  280702
14      2016  284751
15      2017  285421
'''
#registration people each year
user_info_userlevel='SELECT user_lv_cd,count(*) AS num\
           FROM user\
           GROUP BY user_lv_cd\
           ORDER BY num'
user_userlevel_count=pd.read_sql_query(user_info_userlevel,mydb)
print(user_userlevel_count)
'''
   user_lv_cd     num
0           2      12
1           4    6588
2           3    9603
3           7  308464
4           5  349352
5           6  445733
6           1  488955
'''
user_info_citylevel='SELECT city_level,count(*) AS num\
           FROM user\
           GROUP BY city_level\
           ORDER BY num'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
 city_level     num
0               1424
1        6.0    5322
2        2.0   24145
3        1.0  341662
4        5.0  374562
5        3.0  389487
6        4.0  472105
'''
