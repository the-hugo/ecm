import csv
import json
import time
import requests
import math

def request_heatmpap(url, id):
    request = [
        {
            "variables": {
                "deviceType": "d",
                "currency": "USD",
                "hotelId": id,
                "checkOut": "2024-06-14",
                "rangeLow": 0.2,
                "rangeHigh": 0.8
            },
            "extensions": {
                "preRegisteredQueryId": "6eacd21961c01c66"
            }
        }
    ]
    #  if always error change cookie and x-requested-by
    headers = {
        "cookie": "TASameSite=1; TAUnique=%1%enc%3Au%2FKH8yQEGOQTegLLIkrpW8vVzrWrB0%2F4kjL03oi4j7g2jHwltRJPGQ%3D%3D; TASSK=enc%3AAJRX%2FVirFQxh3L%2FWxzIIJifHMc5WZOSjC5CsLacwCJkioVsG3hAwHyxqX5CpZYTYTInWf1F9gvG06JZHPKhp1LGdKAPGuNkLXCRUdEDtOVHDlmzTlzXC3Hx1ccZfybQMMw%3D%3D; OptanonAlertBoxClosed=2023-08-10T08:05:36.557Z; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.501.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.11031; _ga=GA1.1.105187867.1691654737; VRMCID=%1%V1*id.10568*llp.%2FRestaurants-g187791-oa30-Rome_Lazio%5C.html*e.1692278351437; TALanguage=ALL; _lr_env_src_ats=false; eupubconsent-v2=CPwSHvAPwSHvAAcABBENDfCsAP_AAH_AACiQGBtX_T5eb2vi83ZcN7tkaYwP55y3o2wjhhaIEe0NwIOH7BoCJ2MwvBV4JiACGBAkkiKBAQVlHGBcCQAAgIgRiSKMYk2MjzNKJLJAilMbM0MYCD9mnsHT2ZCY70-uO7_zvneBtgBJgoXEADYEhATLRhBAgAGEYQFQAgAoAEgKADCEAEBOwKAj1gIAAACAAEAAAAAIIgAQAACQBIRAAAAYCAQAAQCAAEAAoQCAAiQABYAWgAEAAoBoSAUUAQgGEGBCBEKYEAQAAAAAAAAAAAAAAAAEAoEAMAB0AFwAbIA8ACIAGEAToAuQBnADbAHaAQOCACAAdACuAIgAYQBOgDOAHaAQODABgAdAEQAMIAzgB2gEDhAAcAHQBEADCAJ0AZwA7QCBwoAGAYQBnAEDhgAUAVwBhAGcANsAgcOAEAA6AFcARAAwgCdAGcAO0AgcQABgGEAZwBA4kADAIgAYQCBxQAOADoAiABhAE6AM4AdoBA4A.f_gAD_gAAAAA; datadome=tzEZOnCvtHoqBKs4Ij2R5qasduxdlRCuc6u3WTJxV2yuU7PcLfU7JQPadonIN~BMuovV54~mJV61M0YMKCxbJ1Kw1EYX9YVcCHPs_oQJQk_TRLS7W1KBqRhrLaAM7sXl; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%229e8b7f45-985b-091a-b024-e76dfb63b1a6%22%2C%22c%22%3A1694077354560%2C%22l%22%3A1702560056155%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%223613b575-4691-f6e0-7ed7-c0be5b4f51e0%22%2C%22e%22%3A1702560196689%2C%22c%22%3A1702560128689%2C%22l%22%3A1702560136689%7D; TADCID=MIzIJi2ooOnHeCrDABQCCKy0j55CTpGVsECjuwJMq3pcFeKMjCDk4YadHjfPS1ZiDrob5Ik7ONULmTGvnMrKojMy4BLYwCKE2UE; __vt=z3PooCJNSrtYutJ-ABQCCQPEFUluRFmojcP0P3EgGio5tW7Y8iBVb4i51UwgXEGY3ac4mzgrW2KM3IgIJFOPMNOJ5bjAed0KRKdF-dvG1oVQvq4HlM4O-anfOt8VFBXyg1FKCTD5FwkgG_uOnl8fufW9lw; ServerPool=A; PMC=V2*MS.51*MD.20231221*LD.20231221; TART=%1%enc%3AE3oCyyJK6VtTuWx%2Bpeycdu23uWqLkF1rI7v%2Bk2m0e%2BiNQ4kjO%2FcEEGFZztUNyX8DUHBdG3udNiw%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1702560080814*AZ.1*RS.1; TAUD=LA-1702544327894-1*RDD-1-2023_12_14*ARDD-1921999-2023_12_27.2023_12_28*HD-15752924-2023_12_14.2023_12_15*VRD-15752925-2023_12_14.2023_12_15*G-15752926-2.1.-1.*VRG-15752927-2.0*LG-607522852-2.1.T.*LD-607522854-.....; TASID=1E3F6B2CBD1045B08B762AE32F74C074; _abck=B696544D010E502E37A2B8896BFBAAFC~-1~YAAQTI8UAvHJC1uMAQAAP9XCiwvGGbz9jsQU/hwQxLB+idGFDZeWFZLADxeEDqVYso2imds770bGsFPsatkyb6qZ99QDywm+5Ewu0DhVLeOqUqtjkFJI9mmIDhH1uoWZVrGgH/A5tpfhQUbq9WNvpvhLYWS83Vruz+wNC+PY+iK9XZhtzPAsCe7HdwwCf8WKyqCpzGJ5fqei0th8O6jigea6TkVn9ebOxFQ9wMcYz/HBk2jPfvYxJYskrr+bOANqxDNgbJjSeqmAryYk0jpXR93+u6DTAc70BDgs0Uh0NeM6HsRCfzpka+6TIgyXuqmvBvFHZxMj8toTV4FDiM5iG0X8uP+KXLw1xF29WRZ/CPEgXJ9mbX53y9oayG738A57cDRkf8sw12XgioZid3ob~-1~-1~-1; bm_sz=CC7A9CFB639A3D2EE112AD7551C41FF7~YAAQTI8UAvLJC1uMAQAAP9XCixb0PJH+SBDZQIwCCSZSjvRiyAGCKqq4uN0tWpkvJ4ZiY85o+z0LzjfFZKHG7AByYceTrlow6gxdaFSA/+bNVqRXdkCpbvNR8EHq9V7H+axvIoNUsuwHowOBLtEhh24KCCZDn9IvWngeEDS0qTPG1Dzd2Gz3nplSWwApiRf79g2u96aeZILfbR92oBKnGg8Lvl9MLncwlHbR7xOf40V3uqzHh4ziS0dzas6xVU6Kc5/zAaFCFQApsITkfjRHxcq3WJfn2XlufhN+UTyf26U1H1zm111bbw==~4339248~3425589; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+21+2023+10%3A44%3A15+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=202310.2.0&isIABGlobal=false&hosts=&consentId=d441c948-c24d-4205-b448-c56915616069&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CV2STACK42%3A0&geolocation=DE%3BBY&AwaitingReconsent=false&browserGpcFlag=0; TASession=V2ID.1E3F6B2CBD1045B08B762AE32F74C074*SQ.2*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.187791*EAU._; PAC=AHHpvneN-1z-SVLxBi8nqwqk4U6BgeJY8UojXF-q3lqFT0MruhNTxRSt-5Os2l_OUrNgzHfvLmpjqw85mZUNCgjeaw2spaY6xGfMkVPCi2Q0xcrxeLNRTMwKFpoCX7iuONngc9HW73qztlrneHTJvbZdheczWhZydunSzM66ri-G-3PcCId8sMm4uJDbvEClVw%3D%3D; pbjs_sharedId=ccfcb963-e8d8-4501-8903-617217db298b; pbjs_sharedId_cst=qSwpLEwsRA%3D%3D; _ga_QX0Q50ZC9P=GS1.1.1703151855.22.0.1703151855.60.0.0; __gads=ID=67a9e384c621d837:T=1691654736:RT=1703151852:S=ALNI_MZL6G0ZJ2UtWkjFEZIjg3-g3DBnkg; __gpi=UID=00000c5da7c0892e:T=1691654736:RT=1703151852:S=ALNI_MaW6pSlD80w367lOAHP1NBi-LWvZg; _lr_sampling_rate=100; _lr_retry_request=true; pbjs_unifiedID=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-21T09%3A44%3A19%22%7D; pbjs_unifiedID_cst=qSwpLEwsRA%3D%3D",
        "authority": "www.tripadvisor.com",
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.tripadvisor.com",
        "referer": "https://www.tripadvisor.com" + url,
        "sec-ch-device-memory": "8",
        "sec-ch-ua": "^\^Chromium^^;v=^\^116^^, ^\^Not",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "x-requested-by": "a39cb5fed11dcb561dfc8c3ddc7b3e42786f40895372e5206de5d3bd76c4f834"
    }
    response = requests.post(GRAPHQL_URL, json=request, headers=headers)
    response = response.json()
    all_price_days = []
    heatmap_data = response[0]["data"].get("HPS_getHotelPriceCalendarHeatmap", [])
    if heatmap_data:
        day_heatmaps = heatmap_data[0].get("dayHeatmaps", {})
        if day_heatmaps:
            average_price_days = day_heatmaps.get("averagePriceDays")
            cheap_price_days = day_heatmaps.get("cheapPriceDays")
            high_price_days = day_heatmaps.get("highPriceDays")

            if average_price_days is not None:
                all_price_days.extend(average_price_days)
            if cheap_price_days is not None:
                all_price_days.extend(cheap_price_days)
            if high_price_days is not None:
                all_price_days.extend(high_price_days)
        try:
            all_price_days.sort()
            print("\nPrice Days", all_price_days)
            return all_price_days
        except:
            pass


def request_api(url, loc, day, modified_date):
    request = [
        {
            "variables": {
                "request": {
                    "hotelId": loc,
                    "trackingEnabled": True,
                    "requestCaller": "Hotel_Review",
                    "impressionPlacement": "resp_hr_persistent_footer",
                    "pageLoadUid": "627c0ef8-399d-48b8-8726-335c9ad259f4",
                    "sessionId": "0368FEACF1FE446DA8567C05BE0A8D0D",
                    "currencyCode": "USD",
                    "requestNumber": 1,
                    "spAttributionToken": None,
                    "shapeStrategy": "DEFAULT_DESKTOP_OFFER_SHAPE",
                    "sequenceId": 0,
                    "travelInfo": {
                        "checkInDate": day,
                        "checkOutDate": modified_date,
                        "usedDefaultDates": False,
                        "rooms": 1,
                        "adults": 2,
                        "childAgesPerRoom": []
                    },
                    "allowOptimusDisplayPrice": False
                },
                "locationId": loc
            },
            "extensions": {
                "preRegisteredQueryId": "945694db97215825"
            }
        }
    ]

    #  if always error change cookie and x-requested-by
    headers = {
        "cookie": "TASameSite=1; TAUnique=%1%enc%3Au%2FKH8yQEGOQTegLLIkrpW8vVzrWrB0%2F4kjL03oi4j7g2jHwltRJPGQ%3D%3D; TASSK=enc%3AAJRX%2FVirFQxh3L%2FWxzIIJifHMc5WZOSjC5CsLacwCJkioVsG3hAwHyxqX5CpZYTYTInWf1F9gvG06JZHPKhp1LGdKAPGuNkLXCRUdEDtOVHDlmzTlzXC3Hx1ccZfybQMMw%3D%3D; OptanonAlertBoxClosed=2023-08-10T08:05:36.557Z; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.501.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.11031; _ga=GA1.1.105187867.1691654737; VRMCID=%1%V1*id.10568*llp.%2FRestaurants-g187791-oa30-Rome_Lazio%5C.html*e.1692278351437; TALanguage=ALL; _lr_env_src_ats=false; eupubconsent-v2=CPwSHvAPwSHvAAcABBENDfCsAP_AAH_AACiQGBtX_T5eb2vi83ZcN7tkaYwP55y3o2wjhhaIEe0NwIOH7BoCJ2MwvBV4JiACGBAkkiKBAQVlHGBcCQAAgIgRiSKMYk2MjzNKJLJAilMbM0MYCD9mnsHT2ZCY70-uO7_zvneBtgBJgoXEADYEhATLRhBAgAGEYQFQAgAoAEgKADCEAEBOwKAj1gIAAACAAEAAAAAIIgAQAACQBIRAAAAYCAQAAQCAAEAAoQCAAiQABYAWgAEAAoBoSAUUAQgGEGBCBEKYEAQAAAAAAAAAAAAAAAAEAoEAMAB0AFwAbIA8ACIAGEAToAuQBnADbAHaAQOCACAAdACuAIgAYQBOgDOAHaAQODABgAdAEQAMIAzgB2gEDhAAcAHQBEADCAJ0AZwA7QCBwoAGAYQBnAEDhgAUAVwBhAGcANsAgcOAEAA6AFcARAAwgCdAGcAO0AgcQABgGEAZwBA4kADAIgAYQCBxQAOADoAiABhAE6AM4AdoBA4A.f_gAD_gAAAAA; datadome=tzEZOnCvtHoqBKs4Ij2R5qasduxdlRCuc6u3WTJxV2yuU7PcLfU7JQPadonIN~BMuovV54~mJV61M0YMKCxbJ1Kw1EYX9YVcCHPs_oQJQk_TRLS7W1KBqRhrLaAM7sXl; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%229e8b7f45-985b-091a-b024-e76dfb63b1a6%22%2C%22c%22%3A1694077354560%2C%22l%22%3A1702560056155%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%223613b575-4691-f6e0-7ed7-c0be5b4f51e0%22%2C%22e%22%3A1702560196689%2C%22c%22%3A1702560128689%2C%22l%22%3A1702560136689%7D; TADCID=MIzIJi2ooOnHeCrDABQCCKy0j55CTpGVsECjuwJMq3pcFeKMjCDk4YadHjfPS1ZiDrob5Ik7ONULmTGvnMrKojMy4BLYwCKE2UE; __vt=z3PooCJNSrtYutJ-ABQCCQPEFUluRFmojcP0P3EgGio5tW7Y8iBVb4i51UwgXEGY3ac4mzgrW2KM3IgIJFOPMNOJ5bjAed0KRKdF-dvG1oVQvq4HlM4O-anfOt8VFBXyg1FKCTD5FwkgG_uOnl8fufW9lw; ServerPool=A; PMC=V2*MS.51*MD.20231221*LD.20231221; TART=%1%enc%3AE3oCyyJK6VtTuWx%2Bpeycdu23uWqLkF1rI7v%2Bk2m0e%2BiNQ4kjO%2FcEEGFZztUNyX8DUHBdG3udNiw%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1702560080814*AZ.1*RS.1; TAUD=LA-1702544327894-1*RDD-1-2023_12_14*ARDD-1921999-2023_12_27.2023_12_28*HD-15752924-2023_12_14.2023_12_15*VRD-15752925-2023_12_14.2023_12_15*G-15752926-2.1.-1.*VRG-15752927-2.0*LG-607522852-2.1.T.*LD-607522854-.....; TASID=1E3F6B2CBD1045B08B762AE32F74C074; _abck=B696544D010E502E37A2B8896BFBAAFC~-1~YAAQTI8UAvHJC1uMAQAAP9XCiwvGGbz9jsQU/hwQxLB+idGFDZeWFZLADxeEDqVYso2imds770bGsFPsatkyb6qZ99QDywm+5Ewu0DhVLeOqUqtjkFJI9mmIDhH1uoWZVrGgH/A5tpfhQUbq9WNvpvhLYWS83Vruz+wNC+PY+iK9XZhtzPAsCe7HdwwCf8WKyqCpzGJ5fqei0th8O6jigea6TkVn9ebOxFQ9wMcYz/HBk2jPfvYxJYskrr+bOANqxDNgbJjSeqmAryYk0jpXR93+u6DTAc70BDgs0Uh0NeM6HsRCfzpka+6TIgyXuqmvBvFHZxMj8toTV4FDiM5iG0X8uP+KXLw1xF29WRZ/CPEgXJ9mbX53y9oayG738A57cDRkf8sw12XgioZid3ob~-1~-1~-1; bm_sz=CC7A9CFB639A3D2EE112AD7551C41FF7~YAAQTI8UAvLJC1uMAQAAP9XCixb0PJH+SBDZQIwCCSZSjvRiyAGCKqq4uN0tWpkvJ4ZiY85o+z0LzjfFZKHG7AByYceTrlow6gxdaFSA/+bNVqRXdkCpbvNR8EHq9V7H+axvIoNUsuwHowOBLtEhh24KCCZDn9IvWngeEDS0qTPG1Dzd2Gz3nplSWwApiRf79g2u96aeZILfbR92oBKnGg8Lvl9MLncwlHbR7xOf40V3uqzHh4ziS0dzas6xVU6Kc5/zAaFCFQApsITkfjRHxcq3WJfn2XlufhN+UTyf26U1H1zm111bbw==~4339248~3425589; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+21+2023+10%3A44%3A15+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=202310.2.0&isIABGlobal=false&hosts=&consentId=d441c948-c24d-4205-b448-c56915616069&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CV2STACK42%3A0&geolocation=DE%3BBY&AwaitingReconsent=false&browserGpcFlag=0; TASession=V2ID.1E3F6B2CBD1045B08B762AE32F74C074*SQ.2*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.187791*EAU._; PAC=AHHpvneN-1z-SVLxBi8nqwqk4U6BgeJY8UojXF-q3lqFT0MruhNTxRSt-5Os2l_OUrNgzHfvLmpjqw85mZUNCgjeaw2spaY6xGfMkVPCi2Q0xcrxeLNRTMwKFpoCX7iuONngc9HW73qztlrneHTJvbZdheczWhZydunSzM66ri-G-3PcCId8sMm4uJDbvEClVw%3D%3D; pbjs_sharedId=ccfcb963-e8d8-4501-8903-617217db298b; pbjs_sharedId_cst=qSwpLEwsRA%3D%3D; _ga_QX0Q50ZC9P=GS1.1.1703151855.22.0.1703151855.60.0.0; __gads=ID=67a9e384c621d837:T=1691654736:RT=1703151852:S=ALNI_MZL6G0ZJ2UtWkjFEZIjg3-g3DBnkg; __gpi=UID=00000c5da7c0892e:T=1691654736:RT=1703151852:S=ALNI_MaW6pSlD80w367lOAHP1NBi-LWvZg; _lr_sampling_rate=100; _lr_retry_request=true; pbjs_unifiedID=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-21T09%3A44%3A19%22%7D; pbjs_unifiedID_cst=qSwpLEwsRA%3D%3D",
        "authority": "www.tripadvisor.com",
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.tripadvisor.com",
        "referer": "https://www.tripadvisor.com" + url,
        "sec-ch-device-memory": "8",
        "sec-ch-ua": "^\^Chromium^^;v=^\^116^^, ^\^Not",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "x-requested-by": "a39cb5fed11dcb561dfc8c3ddc7b3e42786f40895372e5206de5d3bd76c4f834"
    }
    time.sleep(6)
    response = requests.post(GRAPHQL_URL, json=request, headers=headers)
    response = response.json()
    dollars = []
    try:
        lowest_price = response[0]['data']['HPS_getWebHROffers']['lowestPrice']
        chevron_offers = response[0]['data']['HPS_getWebHROffers']['chevronOffers']
        chevron_prices = [offer['priceText'] for offer in chevron_offers if offer is not [None]]
        for i in chevron_prices:
            if "$" in i:
                dollars.append(i)
    except:
        save_record({"price": "error", "loc": loc})
    # dollars = find_strings_with_dollar_sign(response)
    print(dollars)
    return dollars


def find_strings_with_dollar_sign(data):
    dollar_strings = []
    if isinstance(data, list):
        for item in data:
            dollar_strings.extend(find_strings_with_dollar_sign(item))
    elif isinstance(data, dict):
        for key, value in data.items():
            dollar_strings.extend(find_strings_with_dollar_sign(value))
    elif isinstance(data, str) and '$' in data:
        dollar_strings.append(data)
    return dollar_strings


def get_ids_from_hotel_url(url):
    url = url.split('-')
    geo = url[1]
    loc = url[2]
    return (int(geo[1:]), int(loc[1:]))


def read_csv(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.extend(row)


def save_record(data):
    with open("prices_venice.csv", "a+", encoding="UTF-8", newline="") as file:  # !!! output file name
        fieldnames = ["loc", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)


GRAPHQL_URL = "https://www.tripadvisor.com/data/graphql/ids"


if __name__ == "__main__":
    data_list = []
    read_csv("links_venice_clean.csv")  # !!! input file name
    for hotel in data_list:
        time.sleep(6)
        geo, loc = get_ids_from_hotel_url(hotel)
        heatmapdays = request_heatmpap(hotel, loc)
        if len(heatmapdays) < 1:
            print("Trying DEFAULT")
            response = request_api(hotel, loc, "2024-09-15", "2023-09-16") # !!! for heatmap, check-in and check-out date
            if len(response) > 0:
                numeric_values = [int(amount[1:]) for amount in response if amount[1:].isdigit()]
                try:
                    average_value = sum(numeric_values) / len(numeric_values)
                    print(average_value)
                    save_record({"price": average_value, "loc": loc})
                except:
                    save_record({"price": "null value", "loc": loc})            
            else:
                save_record({"price": "no price", "loc": loc})
                print("RESPONSE:", response)
                print(hotel)
        counter = 0
        for date in heatmapdays:
            counter += 1
            if counter == 30:  # set max iteration length
                save_record({"price": "no price", "loc": loc})
                print("\nNO PRICES", hotel)
                break
            time.sleep(3)
            year, month, day = map(int, date.split('-'))
            day += 1
            if day > 31:
                day = 1
                month += 1
            if month > 12:
                month = 1
                year += 1
            modified_date = f"{year:04d}-{month:02d}-{day:02d}"
            print("trying date:", date, "and", modified_date)
            response = request_api(hotel, loc, date, modified_date)
            if len(response) > 0:
                numeric_values = [int(amount[1:]) for amount in response if amount[1:].isdigit()]
                try:
                    average_value = sum(numeric_values) / len(numeric_values)
                    print(average_value)
                    save_record({"price": average_value, "loc": loc})
                except:
                    save_record({"price": "null value", "loc": loc})
                break
            else:
                continue
        print("\nELMO")