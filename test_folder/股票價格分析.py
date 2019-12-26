#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:28:36 2018

@author: cheating
"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import yfinance as yf # yahoo專用的拿來拉股票資訊
import datetime

###############################################################################
#                              股票機器人 股票價格分析                            #
###############################################################################
#台灣所有股票
stock =['1101.TW', '1102.TW', '1103.TW', '1104.TW', '1108.TW', '1109.TW', '1110.TW', '1201.TW', '1203.TW', '1210.TW', '1213.TW', '1215.TW', '1216.TW', '1217.TW', '1218.TW', '1219.TW', '1220.TW', '1225.TW', '1227.TW', '1229.TW', '1231.TW', '1232.TW', '1233.TW', '1234.TW', '1235.TW', '1236.TW', '1256.TW', '1262.TW', '1301.TW', '1303.TW', '1304.TW', '1305.TW', '1307.TW', '1308.TW', '1309.TW', '1310.TW', '1312.TW', '1313.TW', '1314.TW', '1315.TW', '1316.TW', '1319.TW', '1321.TW', '1323.TW', '1324.TW', '1325.TW', '1326.TW', '1337.TW', '1338.TW', '1339.TW', '1340.TW', '1402.TW', '1409.TW', '1410.TW', '1413.TW', '1414.TW', '1416.TW', '1417.TW', '1418.TW', '1419.TW', '1423.TW', '1432.TW', '1434.TW', '1435.TW', '1436.TW', '1437.TW', '1438.TW', '1439.TW', '1440.TW', '1441.TW', '1442.TW', '1443.TW', '1444.TW', '1445.TW', '1446.TW', '1447.TW', '1449.TW', '1451.TW', '1452.TW', '1453.TW', '1454.TW', '1455.TW', '1456.TW', '1457.TW', '1459.TW', '1460.TW', '1463.TW', '1464.TW', '1465.TW', '1466.TW', '1467.TW', '1468.TW', '1470.TW', '1471.TW', '1472.TW', '1473.TW', '1474.TW', '1475.TW', '1476.TW', '1477.TW', '1503.TW', '1504.TW', '1506.TW', '1507.TW', '1512.TW', '1513.TW', '1514.TW', '1515.TW', '1516.TW', '1517.TW', '1519.TW', '1521.TW', '1522.TW', '1524.TW', '1525.TW', '1526.TW', '1527.TW', '1528.TW', '1529.TW', '1530.TW', '1531.TW', '1532.TW', '1533.TW', '1535.TW', '1536.TW', '1537.TW', '1538.TW', '1539.TW', '1540.TW', '1541.TW', '1558.TW', '1560.TW', '1568.TW', '1582.TW', '1583.TW', '1587.TW', '1589.TW', '1590.TW', '1592.TW', '1598.TW', '1603.TW', '1604.TW', '1605.TW', '1608.TW', '1609.TW', '1611.TW', '1612.TW', '1614.TW', '1615.TW', '1616.TW', '1617.TW', '1618.TW', '1626.TW', '1701.TW', '1702.TW', '1704.TW', '1707.TW', '1708.TW', '1709.TW', '1710.TW', '1711.TW', '1712.TW', '1713.TW', '1714.TW', '1717.TW', '1718.TW', '1720.TW', '1721.TW', '1722.TW', '1723.TW', '1724.TW', '1725.TW', '1726.TW', '1727.TW', '1730.TW', '1731.TW', '1732.TW', '1733.TW', '1734.TW', '1735.TW', '1736.TW', '1737.TW', '1760.TW', '1762.TW', '1773.TW', '1776.TW', '1783.TW', '1786.TW', '1789.TW', '1802.TW', '1805.TW', '1806.TW', '1808.TW', '1809.TW', '1810.TW', '1817.TW', '1902.TW', '1903.TW', '1904.TW', '1905.TW', '1906.TW', '1907.TW', '1909.TW', '2002.TW', '2006.TW', '2007.TW', '2008.TW', '2009.TW', '2010.TW', '2012.TW', '2013.TW', '2014.TW', '2015.TW', '2017.TW', '2020.TW', '2022.TW', '2023.TW', '2024.TW', '2025.TW', '2027.TW', '2028.TW', '2029.TW', '2030.TW', '2031.TW', '2032.TW', '2033.TW', '2034.TW', '2038.TW', '2049.TW', '2059.TW', '2062.TW', '2069.TW', '2101.TW', '2102.TW', '2103.TW', '2104.TW', '2105.TW', '2106.TW', '2107.TW', '2108.TW', '2109.TW', '2114.TW', '2115.TW', '2201.TW', '2204.TW', '2206.TW', '2207.TW', '2227.TW', '2228.TW', '2231.TW', '2236.TW', '2239.TW', '2243.TW', '2301.TW', '2302.TW', '2303.TW', '2305.TW', '2308.TW', '2312.TW', '2313.TW', '2314.TW', '2316.TW', '2317.TW', '2321.TW', '2323.TW', '2324.TW', '2327.TW', '2328.TW', '2329.TW', '2330.TW', '2331.TW', '2332.TW', '2337.TW', '2338.TW', '2340.TW', '2342.TW', '2344.TW', '2345.TW', '2347.TW', '2348.TW', '2349.TW', '2351.TW', '2352.TW', '2353.TW', '2354.TW', '2355.TW', '2356.TW', '2357.TW', '2358.TW', '2359.TW', '2360.TW', '2362.TW', '2363.TW', '2364.TW', '2365.TW', '2367.TW', '2368.TW', '2369.TW', '2371.TW', '2373.TW', '2374.TW', '2375.TW', '2376.TW', '2377.TW', '2379.TW', '2380.TW', '2382.TW', '2383.TW', '2385.TW', '2387.TW', '2388.TW', '2390.TW', '2392.TW', '2393.TW', '2395.TW', '2397.TW', '2399.TW', '2401.TW', '2402.TW', '2404.TW', '2405.TW', '2406.TW', '2408.TW', '2409.TW', '2412.TW', '2413.TW', '2414.TW', '2417.TW', '2419.TW', '2420.TW', '2421.TW', '2423.TW', '2424.TW', '2425.TW', '2426.TW', '2427.TW', '2428.TW', '2429.TW', '2430.TW', '2431.TW', '2433.TW', '2434.TW', '2436.TW', '2438.TW', '2439.TW', '2440.TW', '2441.TW', '2442.TW', '2443.TW', '2444.TW', '2448.TW', '2449.TW', '2450.TW', '2451.TW', '2453.TW', '2454.TW', '2455.TW', '2456.TW', '2457.TW', '2458.TW', '2459.TW', '2460.TW', '2461.TW', '2462.TW', '2464.TW', '2465.TW', '2466.TW', '2467.TW', '2468.TW', '2471.TW', '2472.TW', '2474.TW', '2475.TW', '2476.TW', '2477.TW', '2478.TW', '2480.TW', '2481.TW', '2482.TW', '2483.TW', '2484.TW', '2485.TW', '2486.TW', '2488.TW', '2489.TW', '2491.TW', '2492.TW', '2493.TW', '2495.TW', '2496.TW', '2497.TW', '2498.TW', '2499.TW', '2501.TW', '2504.TW', '2505.TW', '2506.TW', '2509.TW', '2511.TW', '2514.TW', '2516.TW', '2520.TW', '2524.TW', '2527.TW', '2528.TW', '2530.TW', '2534.TW', '2535.TW', '2536.TW', '2537.TW', '2538.TW', '2539.TW', '2540.TW', '2542.TW', '2543.TW', '2545.TW', '2546.TW', '2547.TW', '2548.TW', '2597.TW', '2601.TW', '2603.TW', '2605.TW', '2606.TW', '2607.TW', '2608.TW', '2609.TW', '2610.TW', '2611.TW', '2612.TW', '2613.TW', '2614.TW', '2615.TW', '2616.TW', '2617.TW', '2618.TW', '2630.TW', '2633.TW', '2634.TW', '2636.TW', '2637.TW', '2642.TW', '2701.TW', '2702.TW', '2704.TW', '2705.TW', '2706.TW', '2707.TW', '2712.TW', '2722.TW', '2723.TW', '2727.TW', '2731.TW', '2739.TW', '2748.TW', '2801.TW', '2809.TW', '2812.TW', '2816.TW', '2820.TW', '2823.TW', '2832.TW', '2834.TW', '2836.TW', '2838.TW', '2841.TW', '2845.TW', '2849.TW', '2850.TW', '2851.TW', '2852.TW', '2855.TW', '2856.TW', '2867.TW', '2880.TW', '2881.TW', '2882.TW', '2883.TW', '2884.TW', '2885.TW', '2886.TW', '2887.TW', '2888.TW', '2889.TW', '2890.TW', '2891.TW', '2892.TW', '2897.TW', '2901.TW', '2903.TW', '2904.TW', '2905.TW', '2906.TW', '2908.TW', '2910.TW', '2911.TW', '2912.TW', '2913.TW', '2915.TW', '2923.TW', '2929.TW', '2936.TW', '2939.TW', '3002.TW', '3003.TW', '3004.TW', '3005.TW', '3006.TW', '3010.TW', '3011.TW', '3013.TW', '3014.TW', '3015.TW', '3016.TW', '3017.TW', '3018.TW', '3019.TW', '3021.TW', '3022.TW', '3023.TW', '3024.TW', '3025.TW', '3026.TW', '3027.TW', '3028.TW', '3029.TW', '3030.TW', '3031.TW', '3032.TW', '3033.TW', '3034.TW', '3035.TW', '3036.TW', '3037.TW', '3038.TW', '3040.TW', '3041.TW', '3042.TW', '3043.TW', '3044.TW', '3045.TW', '3046.TW', '3047.TW', '3048.TW', '3049.TW', '3050.TW', '3051.TW', '3052.TW', '3054.TW', '3055.TW', '3056.TW', '3057.TW', '3058.TW', '3059.TW', '3060.TW', '3062.TW', '3090.TW', '3094.TW', '3130.TW', '3149.TW', '3164.TW', '3167.TW', '3189.TW', '3209.TW', '3229.TW', '3231.TW', '3257.TW', '3266.TW', '3296.TW', '3305.TW', '3308.TW', '3311.TW', '3312.TW', '3321.TW', '3338.TW', '3346.TW', '3356.TW', '3376.TW', '3380.TW', '3383.TW', '3406.TW', '3413.TW', '3416.TW', '3419.TW', '3432.TW', '3437.TW', '3443.TW', '3450.TW', '3454.TW', '3481.TW', '3494.TW', '3501.TW', '3504.TW', '3514.TW', '3515.TW', '3518.TW', '3519.TW', '3528.TW', '3532.TW', '3533.TW', '3535.TW', '3536.TW', '3545.TW', '3550.TW', '3557.TW', '3561.TW', '3576.TW', '3579.TW', '3583.TW', '3588.TW', '3591.TW', '3593.TW', '3596.TW', '3605.TW', '3607.TW', '3617.TW', '3622.TW', '3645.TW', '3653.TW', '3661.TW', '3665.TW', '3669.TW', '3673.TW', '3679.TW', '3682.TW', '3686.TW', '3694.TW', '3698.TW', '3701.TW', '3702.TW', '3703.TW', '3704.TW', '3705.TW', '3706.TW', '3708.TW', '4104.TW', '4106.TW', '4108.TW', '4119.TW', '4133.TW', '4137.TW', '4141.TW', '4142.TW', '4144.TW', '4148.TW', '4155.TW', '4164.TW', '4190.TW', '4306.TW', '4414.TW', '4426.TW', '4438.TW', '4526.TW', '4532.TW', '4536.TW', '4545.TW', '4551.TW', '4552.TW', '4555.TW', '4557.TW', '4560.TW', '4562.TW', '4566.TW', '4720.TW', '4722.TW', '4725.TW', '4737.TW', '4739.TW', '4746.TW', '4755.TW', '4763.TW', '4764.TW', '4807.TW', '4904.TW', '4906.TW', '4912.TW', '4915.TW', '4916.TW', '4919.TW', '4927.TW', '4930.TW', '4934.TW', '4935.TW', '4938.TW', '4942.TW', '4943.TW', '4952.TW', '4956.TW', '4958.TW', '4960.TW', '4968.TW', '4976.TW', '4977.TW', '4984.TW', '4994.TW', '4999.TW', '5007.TW', '5203.TW', '5215.TW', '5225.TW', '5234.TW', '5243.TW', '5258.TW', '5259.TW', '5264.TW', '5269.TW', '5284.TW', '5285.TW', '5288.TW', '5305.TW', '5388.TW', '5434.TW', '5469.TW', '5471.TW', '5484.TW', '5515.TW', '5519.TW', '5521.TW', '5522.TW', '5525.TW', '5531.TW', '5533.TW', '5534.TW', '5538.TW', '5607.TW', '5608.TW', '5706.TW', '5871.TW', '5880.TW', '5906.TW', '5907.TW', '6005.TW', '6024.TW', '6108.TW', '6112.TW', '6115.TW', '6116.TW', '6117.TW', '6120.TW', '6128.TW', '6133.TW', '6136.TW', '6139.TW', '6141.TW', '6142.TW', '6145.TW', '6152.TW', '6153.TW', '6155.TW', '6164.TW', '6165.TW', '6166.TW', '6168.TW', '6172.TW', '6176.TW', '6177.TW', '6183.TW', '6184.TW', '6189.TW', '6191.TW', '6192.TW', '6196.TW', '6197.TW', '6201.TW', '6202.TW', '6205.TW', '6206.TW', '6209.TW', '6213.TW', '6214.TW', '6215.TW', '6216.TW', '6224.TW', '6225.TW', '6226.TW', '6230.TW', '6235.TW', '6239.TW', '6243.TW', '6251.TW', '6257.TW', '6269.TW', '6271.TW', '6277.TW', '6278.TW', '6281.TW', '6282.TW', '6283.TW', '6285.TW', '6288.TW', '6289.TW', '6405.TW', '6409.TW', '6412.TW', '6414.TW', '6415.TW', '6416.TW', '6422.TW', '6431.TW', '6442.TW', '6443.TW', '6449.TW', '6451.TW', '6452.TW', '6456.TW', '6464.TW', '6477.TW', '6504.TW', '6505.TW', '6525.TW', '6531.TW', '6533.TW', '6541.TW', '6552.TW', '6573.TW', '6579.TW', '6581.TW', '6582.TW', '6591.TW', '6605.TW', '6625.TW', '8011.TW', '8016.TW', '8021.TW', '8033.TW', '8039.TW', '8046.TW', '8070.TW', '8072.TW', '8081.TW', '8101.TW', '8103.TW', '8105.TW', '8110.TW', '8112.TW', '8114.TW', '8131.TW', '8150.TW', '8163.TW', '8201.TW', '8210.TW', '8213.TW', '8215.TW', '8222.TW', '8249.TW', '8261.TW', '8271.TW', '8341.TW', '8374.TW', '8404.TW', '8411.TW', '8422.TW', '8427.TW', '8429.TW', '8442.TW', '8443.TW', '8454.TW', '8463.TW', '8464.TW', '8466.TW', '8467.TW', '8473.TW', '8478.TW', '8480.TW', '8481.TW', '8488.TW', '8497.TW', '8499.TW', '8926.TW', '8940.TW', '8996.TW', '9103.TW', '9105.TW', '9136.TW', '9802.TW', '9902.TW', '9904.TW', '9905.TW', '9906.TW', '9907.TW', '9908.TW', '9910.TW', '9911.TW', '9912.TW', '9914.TW', '9917.TW', '9918.TW', '9919.TW', '9921.TW', '9924.TW', '9925.TW', '9926.TW', '9927.TW', '9928.TW', '9929.TW', '9930.TW', '9931.TW', '9933.TW', '9934.TW', '9935.TW', '9937.TW', '9938.TW', '9939.TW', '9940.TW', '9941.TW', '9942.TW', '9943.TW', '9944.TW', '9945.TW', '9946.TW', '9955.TW', '9958.TW', '910322.TW', '911608.TW', '911616.TW', '911619.TW', '911622.TW', '911868.TW',
    '1259.TWO','1264.TWO','1268.TWO','1333.TWO','1336.TWO','1565.TWO','1566.TWO','1569.TWO','1570.TWO','1580.TWO','1584.TWO','1586.TWO','1593.TWO','1595.TWO','1597.TWO','1599.TWO','1742.TWO','1752.TWO','1777.TWO','1781.TWO','1784.TWO','1785.TWO','1787.TWO','1788.TWO','1795.TWO','1796.TWO','1799.TWO','1813.TWO','1815.TWO','2035.TWO','2061.TWO','2063.TWO','2064.TWO','2065.TWO','2066.TWO','2067.TWO','2221.TWO','2230.TWO','2233.TWO','2235.TWO','2596.TWO','2640.TWO','2641.TWO','2643.TWO','2718.TWO','2719.TWO','2729.TWO','2732.TWO','2734.TWO','2736.TWO','2740.TWO','2745.TWO','2916.TWO','2926.TWO','2937.TWO','3064.TWO','3066.TWO','3067.TWO','3071.TWO','3073.TWO','3078.TWO','3081.TWO','3083.TWO','3085.TWO','3086.TWO','3088.TWO','3089.TWO','3092.TWO','3093.TWO','3095.TWO','3105.TWO','3114.TWO','3115.TWO','3118.TWO','3122.TWO','3128.TWO','3131.TWO','3141.TWO','3144.TWO','3147.TWO','3152.TWO','3162.TWO','3163.TWO','3169.TWO','3171.TWO','3176.TWO','3188.TWO','3191.TWO','3202.TWO','3205.TWO','3206.TWO','3207.TWO','3211.TWO','3213.TWO','3217.TWO','3218.TWO','3219.TWO','3221.TWO','3224.TWO','3226.TWO','3227.TWO','3228.TWO','3230.TWO','3232.TWO','3234.TWO','3236.TWO','3252.TWO','3259.TWO','3260.TWO','3264.TWO','3265.TWO','3268.TWO','3272.TWO','3276.TWO','3284.TWO','3285.TWO','3287.TWO','3288.TWO','3289.TWO','3290.TWO','3293.TWO','3294.TWO','3297.TWO','3299.TWO','3303.TWO','3306.TWO','3310.TWO','3313.TWO','3317.TWO','3322.TWO','3323.TWO','3324.TWO','3325.TWO','3332.TWO','3339.TWO','3354.TWO','3360.TWO','3362.TWO','3363.TWO','3372.TWO','3373.TWO','3374.TWO','3379.TWO','3388.TWO','3390.TWO','3402.TWO','3426.TWO','3428.TWO','3431.TWO','3434.TWO','3438.TWO','3441.TWO','3444.TWO','3452.TWO','3455.TWO','3465.TWO','3466.TWO','3479.TWO','3483.TWO','3484.TWO','3489.TWO','3490.TWO','3491.TWO','3492.TWO','3498.TWO','3499.TWO','3508.TWO','3511.TWO','3512.TWO','3516.TWO','3520.TWO','3521.TWO','3522.TWO','3523.TWO','3526.TWO','3527.TWO','3529.TWO','3531.TWO','3537.TWO','3540.TWO','3541.TWO','3546.TWO','3548.TWO','3551.TWO','3552.TWO','3555.TWO','3556.TWO','3558.TWO','3562.TWO','3563.TWO','3564.TWO','3567.TWO','3570.TWO','3577.TWO','3580.TWO','3581.TWO','3587.TWO','3594.TWO','3609.TWO','3611.TWO','3615.TWO','3623.TWO','3624.TWO','3625.TWO','3628.TWO','3629.TWO','3630.TWO','3631.TWO','3632.TWO','3642.TWO','3646.TWO','3652.TWO','3663.TWO','3666.TWO','3672.TWO','3675.TWO','3680.TWO','3684.TWO','3685.TWO','3687.TWO','3689.TWO','3691.TWO','3693.TWO','3707.TWO','3709.TWO','3710.TWO','4102.TWO','4103.TWO','4105.TWO','4107.TWO','4109.TWO','4111.TWO','4113.TWO','4114.TWO','4116.TWO','4120.TWO','4121.TWO','4123.TWO','4126.TWO','4127.TWO','4128.TWO','4129.TWO','4130.TWO','4131.TWO','4138.TWO','4147.TWO','4152.TWO','4153.TWO','4160.TWO','4161.TWO','4162.TWO','4163.TWO','4167.TWO','4168.TWO','4171.TWO','4173.TWO','4174.TWO','4175.TWO','4180.TWO','4183.TWO','4188.TWO','4192.TWO','4198.TWO','4205.TWO','4207.TWO','4303.TWO','4304.TWO','4305.TWO','4401.TWO','4402.TWO','4406.TWO','4413.TWO','4415.TWO','4416.TWO','4417.TWO','4419.TWO','4420.TWO','4429.TWO','4430.TWO','4432.TWO','4433.TWO','4502.TWO','4503.TWO','4506.TWO','4510.TWO','4513.TWO','4523.TWO','4527.TWO','4528.TWO','4529.TWO','4530.TWO','4533.TWO','4534.TWO','4535.TWO','4541.TWO','4542.TWO','4543.TWO','4549.TWO','4550.TWO','4554.TWO','4556.TWO','4561.TWO','4563.TWO','4609.TWO','4702.TWO','4706.TWO','4707.TWO','4711.TWO','4712.TWO','4714.TWO','4716.TWO','4721.TWO','4726.TWO','4728.TWO','4729.TWO','4735.TWO','4736.TWO','4741.TWO','4743.TWO','4744.TWO','4747.TWO','4754.TWO','4806.TWO','4903.TWO','4905.TWO','4907.TWO','4908.TWO','4909.TWO','4911.TWO','4933.TWO','4939.TWO','4944.TWO','4946.TWO','4950.TWO','4953.TWO','4972.TWO','4973.TWO','4974.TWO','4979.TWO','4987.TWO','4995.TWO','5009.TWO','5011.TWO','5013.TWO','5014.TWO','5015.TWO','5016.TWO','5102.TWO','5201.TWO','5202.TWO','5205.TWO','5206.TWO','5209.TWO','5210.TWO','5211.TWO','5212.TWO','5213.TWO','5220.TWO','5230.TWO','5245.TWO','5251.TWO','5255.TWO','5263.TWO','5272.TWO','5274.TWO','5278.TWO','5287.TWO','5289.TWO','5291.TWO','5299.TWO','5301.TWO','5302.TWO','5304.TWO','5306.TWO','5309.TWO','5310.TWO','5312.TWO','5314.TWO','5315.TWO','5317.TWO','5321.TWO','5324.TWO','5328.TWO','5340.TWO','5344.TWO','5345.TWO','5347.TWO','5348.TWO','5349.TWO','5351.TWO','5353.TWO','5355.TWO','5356.TWO','5364.TWO','5371.TWO','5381.TWO','5383.TWO','5386.TWO','5392.TWO','5398.TWO','5403.TWO','5410.TWO','5425.TWO','5426.TWO','5432.TWO','5438.TWO','5439.TWO','5443.TWO','5450.TWO','5452.TWO','5455.TWO','5457.TWO','5460.TWO','5464.TWO','5465.TWO','5468.TWO','5474.TWO','5475.TWO','5478.TWO','5480.TWO','5481.TWO','5483.TWO','5487.TWO','5488.TWO','5489.TWO','5490.TWO','5493.TWO','5498.TWO','5508.TWO','5511.TWO','5512.TWO','5514.TWO','5516.TWO','5520.TWO','5523.TWO','5529.TWO','5530.TWO','5536.TWO','5601.TWO','5603.TWO','5604.TWO','5609.TWO','5701.TWO','5703.TWO','5704.TWO','5820.TWO','5864.TWO','5878.TWO','5902.TWO','5903.TWO','5904.TWO','5905.TWO','6015.TWO','6016.TWO','6020.TWO','6021.TWO','6023.TWO','6026.TWO','6101.TWO','6103.TWO','6104.TWO','6109.TWO','6111.TWO','6113.TWO','6114.TWO','6118.TWO','6121.TWO','6122.TWO','6123.TWO','6124.TWO','6125.TWO','6126.TWO','6127.TWO','6129.TWO','6130.TWO','6134.TWO','6138.TWO','6140.TWO','6143.TWO','6144.TWO','6146.TWO','6147.TWO','6148.TWO','6150.TWO','6151.TWO','6154.TWO','6156.TWO','6158.TWO','6160.TWO','6161.TWO','6163.TWO','6167.TWO','6169.TWO','6170.TWO','6171.TWO','6173.TWO','6174.TWO','6175.TWO','6179.TWO','6180.TWO','6182.TWO','6185.TWO','6186.TWO','6187.TWO','6188.TWO','6190.TWO','6194.TWO','6195.TWO','6198.TWO','6199.TWO','6203.TWO','6204.TWO','6207.TWO','6208.TWO','6210.TWO','6212.TWO','6217.TWO','6218.TWO','6219.TWO','6220.TWO','6221.TWO','6222.TWO','6223.TWO','6227.TWO','6228.TWO','6229.TWO','6231.TWO','6233.TWO','6234.TWO','6236.TWO','6237.TWO','6238.TWO','6240.TWO','6241.TWO','6242.TWO','6244.TWO','6245.TWO','6246.TWO','6247.TWO','6248.TWO','6259.TWO','6261.TWO','6263.TWO','6264.TWO','6265.TWO','6266.TWO','6270.TWO','6274.TWO','6275.TWO','6276.TWO','6279.TWO','6284.TWO','6287.TWO','6290.TWO','6291.TWO','6292.TWO','6294.TWO','6298.TWO','6411.TWO','6417.TWO','6419.TWO','6426.TWO','6432.TWO','6435.TWO','6438.TWO','6441.TWO','6446.TWO','6457.TWO','6461.TWO','6462.TWO','6465.TWO','6469.TWO','6470.TWO','6472.TWO','6482.TWO','6485.TWO','6486.TWO','6488.TWO','6492.TWO','6494.TWO','6496.TWO','6499.TWO','6506.TWO','6508.TWO','6509.TWO','6510.TWO','6512.TWO','6523.TWO','6530.TWO','6532.TWO','6535.TWO','6538.TWO','6542.TWO','6547.TWO','6548.TWO','6556.TWO','6560.TWO','6561.TWO','6568.TWO','6569.TWO','6570.TWO','6574.TWO','6576.TWO','6577.TWO','6593.TWO','6594.TWO','6596.TWO','6603.TWO','6609.TWO','6612.TWO','6613.TWO','6615.TWO','6803.TWO','7402.TWO','8024.TWO','8027.TWO','8032.TWO','8034.TWO','8038.TWO','8040.TWO','8042.TWO','8043.TWO','8044.TWO','8047.TWO','8048.TWO','8049.TWO','8050.TWO','8054.TWO','8059.TWO','8064.TWO','8066.TWO','8067.TWO','8068.TWO','8069.TWO','8071.TWO','8074.TWO','8076.TWO','8077.TWO','8080.TWO','8083.TWO','8084.TWO','8085.TWO','8086.TWO','8087.TWO','8088.TWO','8091.TWO','8092.TWO','8093.TWO','8096.TWO','8097.TWO','8099.TWO','8107.TWO','8109.TWO','8111.TWO','8121.TWO','8147.TWO','8155.TWO','8171.TWO','8176.TWO','8182.TWO','8183.TWO','8234.TWO','8240.TWO','8255.TWO','8277.TWO','8279.TWO','8287.TWO','8289.TWO','8291.TWO','8299.TWO','8342.TWO','8349.TWO','8354.TWO','8358.TWO','8383.TWO','8390.TWO','8401.TWO','8403.TWO','8409.TWO','8410.TWO','8415.TWO','8416.TWO','8420.TWO','8421.TWO','8424.TWO','8431.TWO','8432.TWO','8433.TWO','8435.TWO','8436.TWO','8440.TWO','8446.TWO','8450.TWO','8462.TWO','8472.TWO','8476.TWO','8477.TWO','8489.TWO','8905.TWO','8906.TWO','8908.TWO','8913.TWO','8916.TWO','8917.TWO','8921.TWO','8923.TWO','8924.TWO','8927.TWO','8928.TWO','8929.TWO','8930.TWO','8931.TWO','8932.TWO','8933.TWO','8934.TWO','8935.TWO','8936.TWO','8937.TWO','8938.TWO','8941.TWO','8942.TWO','9949.TWO','9950.TWO','9951.TWO','9960.TWO','9962.TWO']
today = datetime.date.today()
start = datetime.datetime.now() - datetime.timedelta(days=1095) #先設定要爬的時間
end = datetime.date.today()

# 與yahoo請求
pd.core.common.is_list_like = pd.api.types.is_list_like
yf.pdr_override()

# 取得股票資料
stock = data.get_data_yahoo(stock, start, end)

buy=[]
for i in stock['Close'].columns:
    thelow=stock['Close'][i].mean()-stock['Close']['1101.TW'].std()*0
    if thelow > stock['Close'][i].iloc[len(stock['Close'][i])-1]:
        buy.append(i)
