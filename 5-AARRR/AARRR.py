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

#we find the the hottest store first
hot_shop_1='select shop_id, fans_num as HOT\
            from shop\
            ORDER BY HOT desc\
            limit 1'
hot_shop_1_sql=pd.read_sql_query(hot_shop_1,mydb)
print(hot_shop_1_sql)

'''
   shop_id      HOT
0    10393  9293487
'''
#but we recognize that the shop_id can not connect with user information, we decide to see the whole data warehouse as a store 


#acquisition







#let scan people as store exposure rate
'''
SELECT 
    COUNT(*)
FROM
    action
WHERE
    action.action_time BETWEEN '2018-03-01 00:00:00' AND '2018-04-01 00:00:00'
        AND type = 2
'''
#each week pageviews from 2018-02-01 to 2018-04-16

'''
SELECT 
    count(*)
FROM
    action
WHERE
    MONTH(action_time) = 10
        AND YEAR(action_time) = 2017
        AND action.type = 1
'''
#2018 feb first week the number is 4430542
#2018 feb second week the number is 2131124
#2018  feb third week the number is 3006060
#2018 mar first week the number is 3338314
#2018 mar second week the number is 3245769
#2018 mar third week the number is 3395521
#2018 mar forh week the number is 3192226
#2018 april first week the number is 2080353
#2018 april second week the number is 2660349
#2018 april third week the number is 2729852
#mean:3021011






#from 2018-3-26 to 2018-4-16 each day exposure rate

#2018-3-26:  456563 
#2018-3-27:  1261
#2018-3-28:  4104
#2018-3-29:  430325
#2018-3-30:  396813
#2018-3-31(6):  408838
#2018-4-1(7):  382487
#2018-4-2:  371459
#2018-4-3:  382552
#2018-4-4:  347724
#2018-4-5:  381521
#2018-4-6:  407292
#2018-4-7(6):  393055
#2018-4-8(7):  376775
#2018-4-9:  411051
#2018-4-10:  415218
#2018-4-11:  401979
#2018-4-12:  395577
#2018-4-13:  385001
#2018-4-14:  371922
#2018-4-15:  349140












#new consumer each week / new consumers everyday(order number)
'''
SELECT 
    count(*)
FROM
    action
WHERE
    MONTH(action_time) = 10
        AND YEAR(action_time) = 2017
        AND action.type = 1
'''
#2018 feb first week the number is 222220
#2018 feb second week the number is 68269
#2018  feb third week the number is 172471
#2018 mar first week the number is 233781
#2018 mar second week the number is 231075
#2018 mar third week the number is 224536
#2018 mar forh week the number is 223631
#2018 april first week the number is 220594
#2018 april second week the number is 203370
#2018 april third week the number is 219289






#from2018-3-26 to 2018-4-16 order rate each day
#2018-3-26: 30935
#2018-3-27:  31464
#2018-3-28:  41368
#2018-3-29:  30762
#2018-3-30:  28768
#2018-3-31(6):  29215
#2018-4-1(7):  28082
#2018-4-2:  29342
#2018-4-3:  29713
#2018-4-4:  25600
#2018-4-5:  27378
#2018-4-6:  30028
#2018-4-7(6):  30613
#2018-4-8(7):  30696
#2018-4-9:  32101
#2018-4-10:  33267
#2018-4-11:  32496
#2018-4-12:  31830
#2018-4-13:  30376
#2018-4-14(6):  30644
#2018-4-15(7):  28575









#exposure rate each day for each city level
'''
cursor_3=mydb.cursor()
city_level_num=[1,2,3,4,5,6]
for city_num_level in city_level_num:
    city_pageviews_month='SELECT count(*) AS num1\
                            FROM user\
                            WHERE user.city_level={x} AND user.user_id IN (SELECT user_id\
                            FROM action\
                            WHERE action.action_time BETWEEN "2018-02-01 00:00:00" AND "2018-03-01 00:00:00" AND action.type=1)'.format(x=city_num_level)
    cursor_3.execute(city_pageviews_month)
    city_pageviews_month_sql=cursor_3.fetchall()
    for city_pageviews_month_result in city_pageviews_month_sql:
        print(city_num_level,city_pageviews_month_result)
cursor_3.close()
'''
#citylevel=1
#2018 feb first week the number is 88370
#2018 feb second week the number is 59013
#2018  feb third week the number is 76144
#2018 mar first week the number is 88224
#2018 mar second week the number is 89780
#2018 mar third week the number is 88693
#2018 mar forh week the number is 86451
#2018 april first week the number is 67151
#2018 april second week the number is 79122
#2018 april third week the number is 79151
#citylevel=2
#2018 feb first week the number is 4357
#2018 feb second week the number is 2953
#2018  feb third week the number is 4527
#2018 mar first week the number is 5655
#2018 mar second week the number is 5664
#2018 mar third week the number is 5782
#2018 mar forh week the number is 5579
#2018 april first week the number is 4431
#2018 april second week the number is 5168
#2018 april third week the number is 5156
#citylevel=3
#2018 feb first week the number is 120394
#2018 feb second week the number is 81139
#2018  feb third week the number is 102361
#2018 mar first week the number is 116780
#2018 mar second week the number is 114979
#2018 mar third week the number is 110710
#2018 mar forh week the number is 105989
#2018 april first week the number is 82245
#2018 april second week the number is 98128
#2018 april third week the number is 97599
#citylevel=4
#2018 feb first week the number is 128043
#2018 feb second week the number is 86383
#2018  feb third week the number is 112841
#2018 mar first week the number is 130235
#2018 mar second week the number is 128712
#2018 mar third week the number is 126351
#2018 mar forh week the number is 121467
#2018 april first week the number is 94346
#2018 april second week the number is 111265
#2018 april third week the number is 110359
#citylevel=5
#2018 feb first week the number is 85835
#2018 feb second week the number is 56062
#2018  feb third week the number is 75584
#2018 mar first week the number is 89392
#2018 mar second week the number is 90857
#2018 mar third week the number is 90560
#2018 mar forh week the number is 88629
#2018 april first week the number is 68334
#2018 april second week the number is 81202
#2018 april third week the number is 81091
#citylevel=6
#2018 feb first week the number is 1170
#2018 feb second week the number is 768
#2018  feb third week the number is 1092
#2018 mar first week the number is 1301
#2018 mar second week the number is 1337
#2018 mar third week the number is 1329
#2018 mar forh week the number is 1355
#2018 april first week the number is 974
#2018 april second week the number is 1215
#2018 april third week the number is 1190










#exposure rate for each city
#City=1
#2018-3-26:  22363
#2018-3-27:  156
#2018-3-28:  615
#2018-3-29:  21420
#2018-3-30:  20443
#2018-3-31(6):  19900
#2018-4-1(7):  19267
#2018-4-2:  19877
#2018-4-3:  20583
#2018-4-4:  18737
#2018-4-5:  18922
#2018-4-6:  20689
#2018-4-7(6):  20016
#2018-4-8(7):  19692
#2018-4-9:  20905
#2018-4-10:  20961
#2018-4-11:  20839
#2018-4-12:  20631
#2018-4-13:  19812
#2018-4-14:  18994
#2018-4-15:  17729
#City=2
#2018-3-26:  1425
#2018-3-27:  9
#2018-3-28:  43
#2018-3-29:  1310
#2018-3-30:  1292
#2018-3-31(6):  1281
#2018-4-1(7):  1364
#2018-4-2:  1219
#2018-4-3:  1356
#2018-4-4:  1172
#2018-4-5:  1188
#2018-4-6:  1353
#2018-4-7(6):  1308
#2018-4-8(7):  1300
#2018-4-9:  1292
#2018-4-10:  1280
#2018-4-11:  1357
#2018-4-12:  1323
#2018-4-13:  1223
#2018-4-14:  1160
#2018-4-15:  1137
#City=3
#2018-3-26:  26430
#2018-3-27:  213
#2018-3-28:  755
#2018-3-29:  25107
#2018-3-30:  23803
#2018-3-31(6):  23732
#2018-4-1(7):  23938
#2018-4-2:  24099
#2018-4-3:  24713
#2018-4-4:  22127
#2018-4-5:  23160
#2018-4-6:  24720
#2018-4-7(6):  24244
#2018-4-8(7):  24320
#2018-4-9:  25132
#2018-4-10:  25060
#2018-4-11:  24594
#2018-4-12:  23871
#2018-4-13:  23523
#2018-4-14:  23332
#2018-4-15:  21640
#City=4
#2018-3-26:  30898
#2018-3-27:  236
#2018-3-28:  903
#2018-3-29:  29156
#2018-3-30:  27889
#2018-3-31(6):  27447
#2018-4-1(7):  27138
#2018-4-2:  27516
#2018-4-3:  28415
#2018-4-4:  25295
#2018-4-5:  26039
#2018-4-6:  28242
#2018-4-7(6):  27427
#2018-4-8(7):  27686
#2018-4-9:  28978
#2018-4-10:  28819
#2018-4-11:  28831
#2018-4-12:  27868
#2018-4-13:  26742
#2018-4-14:  26072
#2018-4-15:  24537
#City=5
#2018-3-26:  22385
#2018-3-27:  138
#2018-3-28:  569
#2018-3-29:  21539
#2018-3-30:  20841
#2018-3-31(6):  20005
#2018-4-1(7):  19479
#2018-4-2:  20202
#2018-4-3:  21047
#2018-4-4:  19053
#2018-4-5:  19410
#2018-4-6:  20848
#2018-4-7(6):  20355
#2018-4-8(7):  19924
#2018-4-9:  21278
#2018-4-10:  21004
#2018-4-11:  21118
#2018-4-12:  21150
#2018-4-13:  20015
#2018-4-14:  19557
#2018-4-15:  18217
#City=6
#2018-3-26:  337
#2018-3-27:  2
#2018-3-28:  8
#2018-3-29:  332
#2018-3-30:  284
#2018-3-31(6):  276
#2018-4-1(7):  277
#2018-4-2:  303
#2018-4-3:  330
#2018-4-4:  271
#2018-4-5:  295
#2018-4-6:  320
#2018-4-7(6):  314
#2018-4-8(7):  301
#2018-4-9:  295
#2018-4-10:  312
#2018-4-11:  329
#2018-4-12:  323
#2018-4-13:  310
#2018-4-14:  279
#2018-4-15:  277














#Weekly purchases in each city level
#citylevel=1
#2018 feb first week the number is 38644
#2018 feb second week the number is 11823
#2018  feb third week the number is 29512
#2018 mar first week the number is 40278
#2018 mar second week the number is 41842
#2018 mar third week the number is 41139
#2018 mar forh week the number is 41254
#2018 april first week the number is 39537
#2018 april second week the number is 37222
#2018 april third week the number is 40241
#citylevel=2
#2018 feb first week the number is 1780
#2018 feb second week the number is 683
#2018  feb third week the number is 2117
#2018 mar first week the number is 3085
#2018 mar second week the number is 2978
#2018 mar third week the number is 2981
#2018 mar forh week the number is 2959
#2018 april first week the number is 2881
#2018 april second week the number is 2799
#2018 april third week the number is 2890
#citylevel=3
#2018 feb first week the number is 49450
#2018 feb second week the number is 16576
#2018  feb third week the number is 36898
#2018 mar first week the number is 48533
#2018 mar second week the number is 47598
#2018 mar third week the number is 45339
#2018 mar forh week the number is 43764
#2018 april first week the number is 43112
#2018 april second week the number is 41048
#2018 april third week the number is 43560
#citylevel=4
#2018 feb first week the number is 52842
#2018 feb second week the number is 17778
#2018  feb third week the number is 43274
#2018 mar first week the number is 58007
#2018 mar second week the number is 56567
#2018 mar third week the number is 55846
#2018 mar forh week the number is 54550
#2018 april first week the number is 53542
#2018 april second week the number is 50459
#2018 april third week the number is 53394
#citylevel=5
#2018 feb first week the number is 39352
#2018 feb second week the number is 11737
#2018  feb third week the number is 32302
#2018 mar first week the number is 44708
#2018 mar second week the number is 45978
#2018 mar third week the number is 45375
#2018 mar forh week the number is 45317
#2018 april first week the number is 43397
#2018 april second week the number is 41632
#2018 april third week the number is 44767
#citylevel=6
#2018 feb first week the number is 522
#2018 feb second week the number is 159
#2018  feb third week the number is 464
#2018 mar first week the number is 666
#2018 mar second week the number is 676
#2018 mar third week the number is 638
#2018 mar forh week the number is 670
#2018 april first week the number is 595
#2018 april second week the number is 614
#2018 april third week the number is 654








#Daily purchases in each city
#City=1
#2018-3-26:  6047
#2018-3-27:  6024
#2018-3-28:  6918
#2018-3-29:  5863
#2018-3-30:  5525
#2018-3-31(6):  5411
#2018-4-1(7):  5252
#2018-4-2:  5453
#2018-4-3:  5668
#2018-4-4:  4924
#2018-4-5:  5217
#2018-4-6:  5757
#2018-4-7(6):  5794
#2018-4-8(7):  5656
#2018-4-9:  6035
#2018-4-10:  6470
#2018-4-11:  6146
#2018-4-12:  6085
#2018-4-13:  5864
#2018-4-14:  5832
#2018-4-15:  5319
#City=2
#2018-3-26:  454
#2018-3-27:  413
#2018-3-28:  484
#2018-3-29:  403
#2018-3-30:  376
#2018-3-31(6):  404
#2018-4-1(7):  428
#2018-4-2:  403
#2018-4-3:  439
#2018-4-4:  352
#2018-4-5:  368
#2018-4-6:  441
#2018-4-7(6):  464
#2018-4-8(7):  393
#2018-4-9:  423
#2018-4-10:  423
#2018-4-11:  447
#2018-4-12:  442
#2018-4-13:  412
#2018-4-14:  423
#2018-4-15:  407
#City=3
#2018-3-26:  6289
#2018-3-27:  6407
#2018-3-28:  7939
#2018-3-29:  6204
#2018-3-30:  5720
#2018-3-31(6):  6008
#2018-4-1(7):  6055
#2018-4-2:  6073
#2018-4-3:  6112
#2018-4-4:  5154
#2018-4-5:  5659
#2018-4-6:  5978
#2018-4-7(6):  6476
#2018-4-8(7):  6567
#2018-4-9:  6725
#2018-4-10:  6803
#2018-4-11:  6299
#2018-4-12:  6337
#2018-4-13:  6265
#2018-4-14:  6559
#2018-4-15:  6119
#City=4
#2018-3-26:  7928
#2018-3-27:  8170
#2018-3-28:  9662
#2018-3-29:  7699
#2018-3-30:  7268
#2018-3-31(6):  7515
#2018-4-1(7):  7229
#2018-4-2:  7737
#2018-4-3:  7542
#2018-4-4:  6316
#2018-4-5:  6932
#2018-4-6:  6231
#2018-4-7(6):  7908
#2018-4-8(7):  7959
#2018-4-9:  8188
#2018-4-10:  8580
#2018-4-11:  8234
#2018-4-12:  7887
#2018-4-13:  7428
#2018-4-14:  7625
#2018-4-15:  7270
#City=5
#2018-3-26:  6485
#2018-3-27:  6611
#2018-3-28:  7356
#2018-3-29:  6563
#2018-3-30:  6159
#2018-3-31(6):  6023
#2018-4-1(7):  5667
#2018-4-2:  6103
#2018-4-3:  6302
#2018-4-4:  5632
#2018-4-5:  5799
#2018-4-6:  6376
#2018-4-7(6):  6350
#2018-4-8(7):  6445
#2018-4-9:  6722
#2018-4-10:  6930
#2018-4-11:  6907
#2018-4-12:  6934
#2018-4-13:  6536
#2018-4-14:  6428
#2018-4-15:  5964
#City=6
#2018-3-26:  91
#2018-3-27:  93
#2018-3-28:  99
#2018-3-29:  97
#2018-3-30:  80
#2018-3-31(6):  81
#2018-4-1(7):  82
#2018-4-2:  87
#2018-4-3:  99
#2018-4-4:  71
#2018-4-5:  92
#2018-4-6:  87
#2018-4-7(6):  106
#2018-4-8(7):  99
#2018-4-9:  97
#2018-4-10:  93
#2018-4-11:  107
#2018-4-12:  104
#2018-4-13:  107
#2018-4-14:  94
#2018-4-15:  83











#Top ten provinces where exposure mainly comes from
'''
SELECT 
    province, COUNT(*) AS num
FROM
    user
WHERE
    user_id IN (SELECT 
            user_id
        FROM
            action
        WHERE
            action.action_time BETWEEN '2018-04-09 00:00:00' AND '2018-04-16 00:00:00'
                AND type = 1)
GROUP BY province
ORDER BY num asc
LIMIT 11
'''

#feb first week
'''
'20.0','68444'
'11.0','61834'
'6.0','30971'
'7.0','29318'
'26.0','25972'
'23.0','24146'
'30.0','19482'
'29.0','15842'
'8.0','15614'
'1.0','13802'
'''
'''
'18.0','358'
'24.0','606'
'4.0','1181'
'9.0','2612'
'13.0','2635'
'5.0','3067'
'27.0','3098'
'10.0','3411'
'16.0','4242'
'2.0','4663'
'''
#feb second week
'''
'20.0','43012'
'11.0','42707'
'6.0','21417'
'7.0','20151'
'26.0','17287'
'23.0','16696'
'30.0','13047'
'29.0','10612'
'8.0','10494'
'1.0','9628'
'''
'''
'18.0','246'
'24.0','445'
'4.0','785'
'13.0','1667'
'9.0','1936'
'5.0','2017'
'27.0','2074'
'10.0','2309'
'16.0','2793'
'2.0','3063'
'''
# feb third week
'''
'20.0','60608'
'11.0','49630'
'6.0','26602'
'7.0','24119'
'23.0','22064'
'26.0','20213'
'30.0','17898'
'29.0','13505'
'8.0','13249'
'19.0','11464'
'''
'''
'18.0','371'
'24.0','625'
'4.0','1141'
'13.0','2417'
'27.0','2786'
'9.0','2925'
'5.0','3164'
'10.0','3661'
'16.0','4104'
'2.0','4216'
'''
#march first week
'''
'20.0','77027'
'11.0','53890'
'6.0','29852'
'7.0','26234'
'23.0','24584'
'26.0','22230'
'30.0','21045'
'29.0','15591'
'8.0','14830'
'19.0','13683'
'''
'''
'18.0','470'
'24.0','780'
'4.0','1284'
'13.0','2881'
'27.0','3215'
'9.0','3418'
'5.0','3808'
'10.0','4493'
'2.0','4883'
'3.0','5003'
'''
#march second week
'''
'20.0','76291'
'11.0','52997'
'6.0','29897'
'7.0','26487'
'23.0','24286'
'26.0','22583'
'30.0','20333'
'29.0','15793'
'8.0','14775'
'25.0','13902'
'''
'''
'18.0','488'
'24.0','781'
'4.0','1290'
'13.0','2820'
'27.0','3281'
'9.0','3519'
'5.0','3872'
'10.0','4614'
'3.0','5034'
'2.0','5040'
'''
#march third week
'''
'20.0','75375'
'11.0','50689'
'6.0','29635'
'7.0','26501'
'23.0','23002'
'26.0','22310'
'30.0','20044'
'29.0','15873'
'8.0','14219'
'25.0','13829'
'''
'''
'18.0','535'
'24.0','775'
'4.0','1295'
'13.0','2839'
'27.0','3154'
'9.0','3619'
'5.0','3965'
'10.0','4525'
'3.0','4739'
'2.0','4858'
'''
#march forth week
'''
'20.0','73102'
'11.0','48074'
'6.0','28528'
'7.0','26208'
'23.0','22249'
'26.0','21729'
'30.0','19322'
'29.0','15425'
'8.0','13741'
'25.0','13299'
'''
'''
'18.0','528'
'24.0','755'
'4.0','1244'
'13.0','2723'
'27.0','3147'
'9.0','3466'
'5.0','3874'
'10.0','4390'
'3.0','4543'
'2.0','4614'
'''
#april first week
'''
'20.0','56844'
'11.0','37263'
'6.0','21855'
'7.0','20509'
'23.0','17354'
'26.0','16803'
'30.0','15099'
'29.0','12034'
'8.0','10479'
'25.0','10185'
'''
'''
'18.0','429'
'24.0','603'
'4.0','954'
'13.0','2054'
'27.0','2449'
'9.0','2827'
'5.0','2944'
'10.0','3426'
'3.0','3540'
'2.0','3696'
'''
#april second week
'''
'20.0','65974'
'11.0','45208'
'6.0','25916'
'7.0','24050'
'23.0','20692'
'26.0','20363'
'30.0','18347'
'29.0','14042'
'8.0','12792'
'25.0','12190'
'''
'''
'18.0','456'
'24.0','666'
'4.0','1152'
'13.0','2490'
'27.0','2930'
'9.0','3261'
'5.0','3377'
'10.0','4121'
'3.0','4275'
'2.0','4379'
'''
#april third week
'''
'20.0','66528'
'11.0','44490'
'6.0','26024'
'7.0','23741'
'23.0','20593'
'26.0','20236'
'30.0','17692'
'29.0','14067'
'8.0','12496'
'25.0','12035'
'''
'''
'18.0','462'
'24.0','660'
'4.0','1114'
'13.0','2437'
'27.0','2892'
'9.0','3142'
'5.0','3426'
'10.0','3978'
'3.0','4223'
'2.0','4244'
'''




























#The top ten provinces where purchases are mainly from
#feb first week
'''
'20.0','29715'
'11.0','24950'
'6.0','12924'
'7.0','12646'
'26.0','11910'
'23.0','9994'
'30.0','8355'
'29.0','7098'
'8.0','6565'
'1.0','5708'
'''
'''
'18.0','114'
'24.0','233'
'4.0','497'
'9.0','763'
'13.0','1167'
'27.0','1261'
'5.0','1340'
'10.0','1413'
'2.0','1857'
'16.0','1965'
'''
#feb second week
'''
'20.0','9247'
'11.0','8375'
'6.0','4377'
'7.0','3620'
'23.0','3601'
'26.0','3267'
'30.0','3148'
'8.0','2230'
'25.0','1960'
'29.0','1917'
'''
'''
'18.0','46'
'24.0','94'
'4.0','162'
'9.0','323'
'13.0','356'
'27.0','378'
'5.0','493'
'2.0','558'
'10.0','605'
'3.0','648'
'''
# feb third week
'''
'20.0','25088'
'11.0','15837'
'6.0','10012'
'23.0','8652'
'7.0','8165'
'30.0','8036'
'26.0','6890'
'29.0','5097'
'8.0','5033'
'25.0','4662'
'''
'''
'18.0','162'
'24.0','257'
'4.0','461'
'13.0','1006'
'9.0','1052'
'27.0','1125'
'5.0','1644'
'2.0','1691'
'3.0','1819'
'16.0','1920'
'''
#march first week
'''
'20.0','38669'
'11.0','19381'
'6.0','13127'
'23.0','10712'
'30.0','10453'
'7.0','10400'
'26.0','8913'
'25.0','7075'
'29.0','6963'
'19.0','6615'
'''
'''
'18.0','216'
'24.0','384'
'4.0','628'
'9.0','1286'
'13.0','1373'
'27.0','1519'
'2.0','2159'
'5.0','2203'
'3.0','2219'
'10.0','2623'
'''
#march second week
'''
'20.0','37486'
'11.0','19109'
'6.0','13281'
'7.0','10745'
'23.0','10543'
'30.0','9725'
'26.0','9408'
'25.0','7548'
'29.0','7307'
'19.0','6454'
'''
'''
'18.0','239'
'24.0','400'
'4.0','625'
'13.0','1390'
'9.0','1503'
'27.0','1530'
'3.0','2171'
'5.0','2234'
'2.0','2253'
'10.0','2634'
'''
#march third week
'''
'20.0','36580'
'11.0','18371'
'6.0','13168'
'7.0','10796'
'23.0','9713'
'30.0','9712'
'26.0','9363'
'25.0','7572'
'29.0','7167'
'19.0','6310'
'''
'''
'18.0','237'
'24.0','374'
'4.0','589'
'13.0','1339'
'9.0','1473'
'27.0','1480'
'3.0','2083'
'2.0','2127'
'5.0','2294'
'10.0','2545'
'''
#march forth week
'''
'20.0','35981'
'11.0','17376'
'6.0','12932'
'7.0','11460'
'23.0','9561'
'26.0','9414'
'30.0','9251'
'25.0','7451'
'29.0','7234'
'19.0','6152'
'''
'''
'18.0','236'
'24.0','335'
'4.0','568'
'13.0','1336'
'9.0','1428'
'27.0','1539'
'3.0','2033'
'2.0','2081'
'5.0','2241'
'10.0','2416'
'''
#april first week
'''
'20.0','34643'
'11.0','17556'
'6.0','12570'
'7.0','10894'
'23.0','9349'
'30.0','9132'
'26.0','8984'
'25.0','7148'
'29.0','7141'
'19.0','5944'
'''
'''
'18.0','214'
'24.0','352'
'4.0','597'
'13.0','1239'
'9.0','1378'
'27.0','1528'
'3.0','1993'
'2.0','2073'
'5.0','2175'
'10.0','2375'
'''
#april second week
'''
'20.0','31983'
'11.0','16902'
'6.0','11789'
'7.0','10144'
'30.0','9168'
'23.0','9137'
'26.0','8900'
'25.0','6851'
'29.0','6777'
'19.0','5692'
'''
'''
'18.0','210'
'24.0','324'
'4.0','565'
'13.0','1226'
'27.0','1359'
'9.0','1444'
'3.0','1944'
'5.0','1968'
'2.0','1993'
'10.0','2309'
'''
#april third week
'''
'20.0','34743'
'11.0','17635'
'6.0','12627'
'7.0','10675'
'23.0','9707'
'26.0','9574'
'30.0','9252'
'25.0','7258'
'29.0','7215'
'19.0','6038'
'''
'''
'18.0','238'
'24.0','327'
'4.0','549'
'13.0','1283'
'9.0','1445'
'27.0','1514'
'2.0','2052'
'3.0','2066'
'5.0','2159'
'10.0','2411'
'''













#activation








#DAU daily active user / Daily active users
'''
user_info_citylevel='SELECT COUNT(DISTINCT user_id)\
                    FROM action\
                    WHERE user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-03-19 00:00:00" AND "2018-03-20 00:00:00")'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#Query the daily DAU for the last four weeks
#2018-3-19:  120926
#2018-3-20:  121422
#2018-3-21:  117954
#2018-3-22:  114788
#2018-3-23:  113729
#2018-3-24(6): 109388
#2018-3-25(7): 113822
#2018-3-26:  115331
#2018-3-27:  39606
#2018-3-28:  45438
#2018-3-29:  110581
#2018-3-30:  105563
#2018-3-31(6):  103627
#2018-4-1(7):  102606
#2018-4-2:  105062
#2018-4-3:  108093
#2018-4-4:  97017
#2018-4-5:  99208
#2018-4-6:  107027
#2018-4-7(6):  104609
#2018-4-8(7):  105820
#2018-4-9:  110950
#2018-4-10:  110829
#2018-4-11:  110851
#2018-4-12:  107959
#2018-4-13:  104147
#2018-4-14:  101775
#2018-4-15:  95325





#WAU
#3.19-3.25:  464571
#3.26-4.1:   402642
#4.2-4.8:    430982
#4.9-4.15:   435512






#MAU
#3.19-4.15:  1014067







#Calculate the activity rate, calculate the data from 2.5 to 4.15, and calculate the activity rate per week

#Weekly active users
#2018 feb first week the number is 463784
#2018 feb second week the number is 303112
#2018  feb third week the number is 406294
#2018 mar first week the number is 482808
#2018 mar second week the number is 485207
#2018 mar third week the number is 478378
#2018 mar forh week the number is  464571
#2018 april first week the number is 402642
#2018 april second week the number is 430982
#2018 april third week the number is 435512







'''
user_info_citylevel='SELECT COUNT(DISTINCT user_id)\
                    FROM action\
                    WHERE user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-09 00:00:00" AND "2018-04-16 00:00:00" )\
                        AND user_id NOT IN (SELECT user_id\
                                            FROM action\
                                            WHERE action.action_time BETWEEN "2018-02-05 00:00:00" AND "2018-04-09 00:00:00")'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''


#Number of newly added users per week (assuming that there are no users before the start of 2.5)
#2018 feb first week the number is   463784
#2018 feb second week the number is  113648
#2018  feb third week the number is  164814
#2018 mar first week the number is   175723
#2018 mar second week the number is  151129
#2018 mar third week the number is   128564
#2018 mar forh week the number is    111704
#2018 april first week the number is 93923
#2018 april second week the number is 85773
#2018 april third week the number is 81484


#Active weekly users
#2018 feb first week the number is   0
#2018 feb second week the number is  189464
#2018  feb third week the number is  241480
#2018 mar first week the number is   307085
#2018 mar second week the number is  334078
#2018 mar third week the number is   349814
#2018 mar forh week the number is    352867
#2018 april first week the number is 308719
#2018 april second week the number is 345209
#2018 april third week the number is  354028



#Percentage of active users per week (number of active users per week/number of active users per week)
#2018 feb first week the number is   0
#2018 feb second week the number is  62.506%
#2018  feb third week the number is  59.435%
#2018 mar first week the number is   63.604%
#2018 mar second week the number is  68.853%
#2018 mar third week the number is   73.125%
#2018 mar forh week the number is    75.955%
#2018 april first week the number is 76.673%
#2018 april second week the number is 80.098%
#2018 april third week the number is  81.302%




#Active percentage of new users per week (number of active new users/number of active users per week)
#2018 feb first week the number is   100%
#2018 feb second week the number is  37.494%
#2018  feb third week the number is  40.564%
#2018 mar first week the number is   36.396%
#2018 mar second week the number is  31.147%
#2018 mar third week the number is   26.875%
#2018 mar forh week the number is    24.045%
#2018 april first week the number is 23.327%
#2018 april second week the number is 19.902%
#2018 april third week the number is  18.698%



#Cumulative number of old users
#2.5-2.11:  0
#2.12-2.18：463784
#2.19-2.25:  577432
#2.26-3.5:  742246
#3.5-3.11:  917969
#3.12-2.18: 1069098
#3.19-3.25: 1197662
#3.26-4.1:  1309366
#4.2-4.8:   1403289
#4.9-4.15:  1489062


#Active rate of old users (promotion)
#2018 feb first week the number is   0%
#2018 feb second week the number is  40.852%
#2018  feb third week the number is  41.819%
#2018 mar first week the number is   41.372%
#2018 mar second week the number is  36.393%
#2018 mar third week the number is   32.72%
#2018 mar forh week the number is    29.463%
#2018 april first week the number is 23.578%
#2018 april second week the number is 24.6%
#2018 april third week the number is  23.775%




#Calculate the bounce rate, the number of people with only one operation
'''
SELECT 
    COUNT(*)
FROM
    (SELECT 
        COUNT(*) AS num
    FROM
        action
    WHERE
        action.action_time BETWEEN '2018-04-09 00:00:00' AND '2018-04-16 00:00:00'
    GROUP BY user_id)T0
WHERE
    T0.num = 1
'''

#Total number of users: 1570546
#Number of people with only one operation: 117029
#Bounce rate: 7.451%









#Calculate the proportion of users who operate once a day: the proportion of users who operate once per day
'''
user_info_citylevel='SELECT COUNT(DISTINCT user_id)\
                    FROM action\
                    WHERE user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-09 00:00:00" AND "2018-04-10 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-10 00:00:00" AND "2018-04-11 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-11 00:00:00" AND "2018-04-12 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-12 00:00:00" AND "2018-04-13 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-13 00:00:00" AND "2018-04-14 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-14 00:00:00" AND "2018-04-15 00:00:00")\
                         AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-04-15 00:00:00" AND "2018-04-16 00:00:00")'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''

#Number of users with operations per day
#3.19-3.25: 4574
#3.26-4.1:  386
#4.2-4.8:   3191
#4.9-4.15:  3614

#WAU
#3.19-3.25:  464571
#3.26-4.1:   402642
#4.2-4.8:    430982
#4.9-4.15:   435512

#Percentage per week
#3.19-3.25: 0.984%
#3.26-4.1:  0.096%
#4.2-4.8:   0.74%
#4.9-4.15:  0.83%








#User loyalty
'''
user_info_citylevel='SELECT COUNT(*)\
                     FROM (SELECT COUNT(*) AS num\
                     FROM action\
                     WHERE action.action_time BETWEEN "2018-02-05 00:00:00" AND "2018-04-16 00:00:00"\
                     GROUP BY user_id)T0\
                     WHERE T0.num >40'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''

#The number of operations <=20 times in three months: 1168593
#20-40:  220153
#40-60:  78565
#60-80:  36417
#80-100: 19891
#>100:   46927

#Total number of users: 1570546

#The number of operations <=20 times in three months: 74.407%
#20-40:  14.018%
#40-60:  5.002%
#60-80:  2.319%
#80-100: 1.267%
#>100:   2.988%





















#retention

#We calculate the retention rate for the next day from 3.19 to 4.15, the retention rate for 3 days, the retention rate for 7 days, and the retention rate for 30 days.
'''
Retention rate on the 1st day (ie "second stay"): (the number of newly added users that day, the number of users who have logged in on the first day after the newly added day) / the total number of newly added users on the first day;
Retention rate on the second day: (the number of newly added users on the day, the number of users who have logged in on the second day after the newly added day) / the total number of newly added users on the first day;
Retention rate on the 3rd day: (the number of users who have logged in on the 3rd day after the new day among the newly added users on the day) / the total number of newly added users on the first day;
Retention rate on the 7th day: (Among the newly added users that day, the number of users who have logged in on the 7th day after the newly added day)/Total number of newly added users on the first day;
Retention rate on the 30th day: (Among the new users that day, the number of users who have logged in on the 30th day after the new day)/Total number of new users on the first day

user_info_citylevel='SELECT COUNT(DISTINCT user_id)\
                    FROM action\
                    WHERE user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-02-19 00:00:00" AND "2018-02-20 00:00:00" )\
                        AND user_id NOT IN (SELECT user_id\
                                            FROM action\
                                            WHERE action.action_time BETWEEN "2018-02-05 00:00:00" AND "2018-02-19 00:00:00")\
                        AND user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-02-26 00:00:00" AND "2018-02-27 00:00:00" )'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''

#User retention rate
'''
user_info_citylevel='SELECT COUNT(DISTINCT user_id)\
                    FROM action\
                    WHERE user_id IN (SELECT user_id\
                                        FROM action\
                                        WHERE action.action_time BETWEEN "2018-03-19 00:00:00" AND "2018-03-20 00:00:00" )\
                        AND user_id IN (SELECT user_id\
                                            FROM action\
                                            WHERE action.action_time BETWEEN "2018-03-22 00:00:00" AND "2018-03-23 00:00:00")'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#3.19User number：120926
#3.20Number of users still online：38208
#3.22Number of users still online：30043
#3.26Number of users still online：25397
#4.15Number of users still online：16685

#Next day retention rate：31.596%
#3 days retention rate： 24.844%
#7 days retention rate:  21.002%
#30 days retention rate：13.798%

#We calculate the next-day retention rate from 2.19 to 3.18, the 3-day retention rate, the 7-day retention rate, and the 30-day retention rate

#2.19User number：78980
#2.20Number of users still online：25510
#2.22 Number of users still online：21611
#2.26 Number of users still online：18999
#3.18 Number of users still online：16058

#Next day retention rate：32.299%
#3 day retention rate： 27.363%
#7 day retention rate:  24.055%
#30 day retention rate：20.332%





#New user retention rate

#3.19Number of new users：17109
#3.20Number of users still online：3094
#3.22Number of users still online：1848
#3.26Number of users still online：1070
#4.15Number of users still online：525

#Next day retention rate：18.084%
#3 retention rate： 10.801%
#7 retention rate:  6.254%
#30 retention rate：3.069%

#We calculate the next-day retention rate from 2.19 to 3.18, the 3-day retention rate, the 7-day retention rate, and the 30-day retention rate

#2.19Number of new users：16795
#2.20Number of users still online：3141
#2.22Number of users still online：2268
#2.26Number of users still online：1800
#3.18Number of users still online：1259

#Next day retention rate：18.702%
#3 retention rate： 13.504%
#7 retention rate:  10.717%
#30 retention rate：7.496%




#Retention rate of old users

#3.19Number of old online users：103817
#3.20Number of old users still online：35114
#3.22Number of old users still online：28195
#3.26Number of old users still online：24327
#4.15Number of old users still online：16160

#Next day retention rate：33.823%
#3 day retention rate： 27.158%
#7  day retention rate:  23.433%
#30  day retention rate：15.556%















#Churn funnel frame
#Statistics on the total
#scan-order-comment
#sacn:100%
#Percentage from browsing to purchase: 5.556% and the number of scans, each user may browse several times before purchasing
##Percentage that will be evaluated after purchase: 37.692%

#According to each user, does not contain duplicate user_id
#scan-order-comment
#sacn:100%
#Percentage of each user from browsing to purchase: 100% Each user has purchased at least once
##Percentage that each user will evaluate after purchase: 24.688% The number of users who have commented at least once


#Quantity purchased directly by each user
'''
user_info_citylevel='SELECT ROUND(T1.type_count / T0.type_count * 100, 3)\
                    FROM (SELECT COUNT(DISTINCT user_id) AS type_count\
                        FROM action\
                        WHERE  action.type = 1 ) T0,\
                        (SELECT COUNT(DISTINCT user_id) AS type_count\
                        FROM action\
                        WHERE action.user_id IN \
                                (SELECT user_id\
                                FROM action\
                                WHERE action.type = 1)\
                                AND action.user_id NOT IN\
                                (SELECT user_id\
                                FROM action\
                                WHERE action.type = 3 or action.type= 5)\
                        AND action.type = 2) T1'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''

#scan-order-comment
#sacn:100%
#Percentage of each user from browsing to direct purchase: 73.663% How many users purchase directly
##Percentage that each user will evaluate directly after purchase: 16.295% Comment after purchase without adding to the shopping cart or paying attention



#scan-follow-order-comment

#According to each user, it is not necessary to repeat user_id
#sacn:100%
#Percentage from browsing to following: 13.524%
##Percentage of each user who will buy after following: 13.524%
#Percentage that each user will evaluate: 5.586%


#scan- add to cart-order-comment

#According to each user, does not contain duplicate user_id
#sacn:100%
#Percentage from browsing to adding to cart: 15.83%
##The percentage of each user who will buy after adding to the shopping cart: 15.83%
#Percentage that each user will evaluate: 4.019%

















#renevue



#scan convert to add to cart
'''
SELECT 
    ROUND(T1.type_count / T0.type_count * 100, 3)
FROM
    (SELECT 
        COUNT(*) AS type_count
    FROM
        action
    WHERE
        action.type = 1) T0,
    (SELECT 
        COUNT(*) AS type_count
    FROM
        action
    WHERE
        action.user_id IN (SELECT 
                user_id
            FROM
                action
            WHERE
                action.type = 1)
            AND action.type = 5) T1
'''


'''
user_info_citylevel='SELECT ROUND(T1.type_count / T0.type_count * 100, 3)\
                        FROM (SELECT COUNT(*) AS type_count\
                        FROM action\
                        WHERE action.action_time BETWEEN "2018-04-09 00:00:00" AND "2018-04-16 00:00:00" AND action.type = 1 ) T0,\
                        (SELECT COUNT(*) AS type_count\
                        FROM action\
                        WHERE action.user_id IN \
                        (SELECT user_id\
                            FROM action\
                        WHERE action.action_time BETWEEN "2018-04-09 00:00:00" AND "2018-04-16 00:00:00" AND action.type = 1)\
                            AND action.type = 5) T1'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#The percentage of conversion from browsing to shopping cart is 1.801%
#We found out from those who browsed

#2018 feb first week the number is 0%
#2018 feb second week the number is 0%
#2018  feb third week the number is 0%
#2018 mar first week the number is 0%
#2018 mar second week the number is 0%
#2018 mar third week the number is 0%
#2018 mar forh week the number is 0%
#2018 april first week the number is 0%
#2018 april second week the number is 2.561%
#2018 april third week the number is 19.374%





#scan convert to order 

#Percentage from browsing to direct purchase: 5.556%


#2018 feb first week the number is 4.41%
#2018 feb second week the number is 3.2%
#2018  feb third week the number is 5.737%
#2018 mar first week the number is 7.002%
#2018 mar second week the number is 7.119%
#2018 mar third week the number is 6.612%
#2018 mar forh week the number is 7.005%
#2018 april first week the number is 10.603%
#2018 april second week the number is 7.644%
#2018 april third week the number is 8.033%




#order to comment 
'''
user_info_citylevel='SELECT ROUND(T1.type_count / T0.type_count * 100, 3)\
                        FROM (SELECT COUNT(*) AS type_count\
                        FROM action\
                        WHERE  action.type = 5 ) T0,\
                        (SELECT COUNT(*) AS type_count\
                        FROM action\
                        WHERE action.user_id IN \
                        (SELECT user_id\
                            FROM action\
                        WHERE action.type = 5)\
                            AND action.type = 3) T1'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#Percentage that will be evaluated after purchase: 37.692%

#2018 feb first week the number is 38.579%
#2018 feb second week the number is 59.586%
#2018  feb third week the number is 29.972%
#2018 mar first week the number is 34.817%
#2018 mar second week the number is 37.046%
#2018 mar third week the number is 39.896%
#2018 mar forh week the number is 40.026%
#2018 april first week the number is 41.63%
#2018 april second week the number is 42.27%
#2018 april third week the number is 40.254%




#The percentage of people who will choose to follow after browsing: 1.317%
#The percentage of people who will pay attention after placing an order: 20.149%
#How many commenters follow: 30.106%
#The percentage of people who will follow after adding to the shopping cart 22.807%







#Repurchase rate, analyzed according to each user
'''
user_info_citylevel='SELECT COUNT(*)\
                    FROM (SELECT COUNT(*) AS num\
                            FROM action\
                            WHERE action.type=2\
                            GROUP BY user_id)T0'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#Number of repurchases：326618
#Total number of purchases：1608707
#Repurchase rate：20.303%


#Repurchase rate of different city levels
'''
cursor_3=mydb.cursor()
city_level_num=[1,2,3,4,5,6]
for city_num_level in city_level_num:
    city_pageviews_month='SELECT count(*) AS num1\
                            FROM user\
                            WHERE user.city_level={x} AND user.user_id IN (SELECT T0.user_id_1\
                            FROM (SELECT user_id AS user_id_1, COUNT(*) AS num\
                                   FROM action\
                                    WHERE action.type=2\
                                    GROUP BY action.user_id)T0\
                                  WHERE T0.num>1)'.format(x=city_num_level)
    cursor_3.execute(city_pageviews_month)
    city_pageviews_month_sql=cursor_3.fetchall()
    for city_pageviews_month_result in city_pageviews_month_sql:
        print(city_num_level,city_pageviews_month_result)
cursor_3.close()
'''
#level=1
#Number of repurchases：69478
#Total number of purchases：341662
#Repurchase rate：20.338%

#level=2
#Number of repurchases：4363
#Total number of purchases：24145
#Repurchase rate：18.07%

#level=3
#Number of repurchases：85816
#Total number of purchases：389487
#Repurchase rate：22.033%

#level=4
#Number of repurchases：93164
#Total number of purchases：472105
#Repurchase rate：19.734%

#level=5
#Number of repurchases：72492
#Total number of purchases：374562
#Repurchase rate：20.857%

#level=6
#Number of repurchases：1061
#Total number of purchases：5322
#Repurchase rate：19.936%

























#RFM
#Tableau
#We use tableau to count the number of purchases made by each user and the most recent purchase time
#Level of detail expressions (also called LOD expressions)
'''
select user_id, max(action_time) as last_active
from action
where action_time<='2018-04-16 00:00:00' and action.type=2
group by user_id



select user_id, count(*) as num
from action
where type=2 
      and action.action_time BETWEEN '2018-02-05 00:00:00' AND '2018-04-16 00:00:00'
group by user_id
order by num desc
'''
'''
For the number of purchases
0-10 level=1
11-20 level=2
20-30 level=3
30-40 level=4
40=50 level=5
50-75 level=6
76-100 level=7
100-150 level=8
151-200 level=9
>200 level=10



For the most recent purchase time

2.5-2.11 level=1
2.12-2.18 level=2
2.19=2.25 level=3
2.26-3.4 level=4
3.5-.3.11 level=5
3.12-3.18 level=6
3.19-3.25 level=7
3.26-4.1 level=8
4.2-4.8 level=9
4.9-4.15 level=10
'''



'''
user_info_citylevel='SELECT COUNT(*)\
                    FROM action\
                    WHERE action.user_id="1187177" \
                        AND action.type=5\
                        AND action.action_time BETWEEN "2018-04-15 00:00:00" AND "2018-04-16 00:00:00"'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
'''
#scan
#2018-3-19:  0
#2018-3-20:  0
#2018-3-21:  57
#2018-3-22:  82
#2018-3-23:  80
#2018-3-24(6): 24
#2018-3-25(7): 16
#2018-3-26:  21
#2018-3-27:  0
#2018-3-28:  0
#2018-3-29:  59
#2018-3-30:  2
#2018-3-31(6):  1
#2018-4-1(7):  1
#2018-4-2:  3
#2018-4-3:  3
#2018-4-4:  2
#2018-4-5:  2
#2018-4-6:  7
#2018-4-7(6): 14 
#2018-4-8(7):  43
#2018-4-9:  63
#2018-4-10:  44
#2018-4-11:  77
#2018-4-12:  10
#2018-4-13:  26
#2018-4-14:  17
#2018-4-15:  4





#order2
#2018-3-19:  0
#2018-3-20:  0
#2018-3-21:  11
#2018-3-22:  10
#2018-3-23:  16
#2018-3-24(6): 3
#2018-3-25(7): 3
#2018-3-26:  6
#2018-3-27:  0
#2018-3-28:  1
#2018-3-29:  5
#2018-3-30:  0
#2018-3-31(6):  0
#2018-4-1(7):  0
#2018-4-2:  0
#2018-4-3:  0
#2018-4-4:  0
#2018-4-5:  0
#2018-4-6:  5
#2018-4-7(6):  3
#2018-4-8(7):  15
#2018-4-9:  34
#2018-4-10:  15
#2018-4-11:  49
#2018-4-12:  5
#2018-4-13:  5
#2018-4-14:  2
#2018-4-15:  0





#add to cart5
#2018-3-19:  0
#2018-3-20:  0
#2018-3-21:  0
#2018-3-22:  0
#2018-3-23:  0
#2018-3-24(6): 0
#2018-3-25(7): 0
#2018-3-26:  0
#2018-3-27:  0
#2018-3-28:  0
#2018-3-29:  0
#2018-3-30:  0
#2018-3-31(6):  0
#2018-4-1(7):  0
#2018-4-2:  0
#2018-4-3:  0
#2018-4-4:  0
#2018-4-5:  0
#2018-4-6:  0
#2018-4-7(6):  0
#2018-4-8(7):  18
#2018-4-9:  42
#2018-4-10:  14
#2018-4-11:  67
#2018-4-12:  4
#2018-4-13:  6
#2018-4-14:  3
#2018-4-15:  0


#comment4
#2018-3-19:  0
#2018-3-20:  0
#2018-3-21:  0
#2018-3-22:  0
#2018-3-23:  0
#2018-3-24(6): 0
#2018-3-25(7): 0
#2018-3-26:  0
#2018-3-27:  0
#2018-3-28:  0
#2018-3-29:  0
#2018-3-30:  0
#2018-3-31(6):  0
#2018-4-1(7):  0
#2018-4-2:  0
#2018-4-3:  0
#2018-4-4:  0
#2018-4-5:  0
#2018-4-6:  0
#2018-4-7(6):  0
#2018-4-8(7):  0
#2018-4-9:  0
#2018-4-10:  0
#2018-4-11:  0
#2018-4-12:  0
#2018-4-13:  0
#2018-4-14:  0
#2018-4-15:  0









'''
user_info_citylevel='SELECT cate\
                     FROM product\
                     WHERE sku_id IN (SELECT sku_id\
                                       FROM action\
                                        WHERE action.user_id=1187177 AND action.type=1)\
                     GROUP by cate'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)

'''



user_info_citylevel='SELECT count(*)\
                     FROM action\
                     WHERE user_id=1187177 AND action.type=1\
                            AND sku_id IN (SELECT sku_id\
                                       FROM product\
                                        WHERE cate=10)'
user_citylevel_count=pd.read_sql_query(user_info_citylevel,mydb)
print(user_citylevel_count)
