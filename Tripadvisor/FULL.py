import json
import re
import requests
from typing import Dict
import csv
import time

def parse_hotel_page(url: str) -> Dict:
    """Parse hotel data from hotel pages using Requests."""
    headers = {
        "cookie": "TAUnique=%1%enc%3AmUgm0McqpcSMRhzIP%2B4IYL3Tn%2Fwl2OM0RS9zpn%2BIYr%2B6nJGzCaUponDUfZsDRYwrNox8JbUSTxk%3D; TASameSite=1; TASSK=enc%3AADGpJdO%2FJ7NrK%2BC%2B3M47lgUyR9mDoPzEWXHVIciltHfG0nYaPsmhQAUL2%2BZTegh41mbLcDy9tMDHNeCMuhdtPLWcp3s1OByL55YAUfKKZ6WsyXzbtTpbpEzxyMxPP6g5nw%3D%3D; OptanonAlertBoxClosed=2023-12-06T16:53:19.535Z; eupubconsent-v2=CP2XLJgP2XLJgAcABBENAdEsAP_gAEPgACiQg1QooAAgAEAAQAAwACIAFAAhABUAGQAOQAeACGAEgASwAnACgAFUALAAtABfADEAMoAaABqADmAHYAfABCgCIAIwASQAmABOACgAFWALQAtwBdAF-AMIAxQBkAGUANEAbABtADfAHIAc4A7gDxAIAAhYBEAEXAI4AjwBJwCVAJaATIBNgCdAFDAKQApQBUACtAFlALgAuQBfQDAAMEAYYAxwBnQDSANWAa4BsADggHEAckA8QDzgHwAfMA-wD9gH-AgEBBgEHAIjARgBGoCOAI6ASKAkoCTQEtAS4AmABOACdQE9AT8AosBSAFJAKaAVmArwCvgFmALgAXMAuwBeQC-gGBAMUAZIAzUBnAGdANBAaYBqADaAG2ANwAcIA7YB3wDzQHqAesA94B8gD6gH7gP-BAECBAIFAQSAgyBCQEJwIXAhgBDYCIAERQIlAiaBFIEVAIsAReAjUBHACOwEegJEASWAlQBK0CWQJaAS8AmIBMsCaQJqATZAnECcoE7ATuAn-BQwFEQKMAo2BSAFIgKTgUsBS4CmwFRAKkgVSBVQCrgFZQK-Ar-BYYFiwLIAsoBZgCzwFogLVgWuBbMC3QLegXCBcUC5QLmgXQBd0C8gLzgXsBe8C_QL-gYABgYDGQIrwTZBN6CcAJwhBqEGqC4AAiABQAFwAOAA8ACoAFwAOAAeABAACQAF8AMQAygBoAGoAPAAfgBEACYAFAAKYAVYAuAC6AGIANAAbwA_ACEgEQARIAjgBLACaAFKAMAAYYAywBmgDZAHIAPiAfYB-wD_AQAAg4BEYCLAIwARqAjgCOgEiAJKAT8AqABcwC8gF9AMUAZ8A14BtADcAHSAO2AfYA_4CJgEXgI9ASIAlQBKwCYoEyATKAmcBOwCh4FIAUiApMBTYCpAFVQLEAsUBZQC0QFsALdAXIAugBdoC74F5AXmAvoBgkE2wTcgm8Cb4E4Qg1AFAgBAAOgAuADZAIgAYQBOgC5AIHBAAwAOgBXAEQAMIAnQCBwYAOADoALgA2QCIAGEAXIBA4QAHAB0ANkAiABhAE6ALkAgcKABgBcAMIBA4YADAFcAYQCBw4AOADoAVwBEADCAJ0AgcBFcgACAMIBA4kADAIgAYQCBxQAKADoAiABhAE6AQOAA.f_wACHwAAAAA; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.320.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.12831.13632.13731.14237.16831; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; _ga=GA1.1.1892302918.1701881601; TADCID=LZBANZA-0UYC-s0CABQCmq6heh9ZSU2yA8SXn9Wv5HsQMKae7AW7FGH1nie2WVNc39velVbl-67rbPaD-w4B5RjApGxVuDqAWYA; PMC=V2*MS.59*MD.20231206*LD.20240122; TATravelInfo=V2*AY.2024*AM.2*AD.4*DY.2024*DM.2*DD.5*A.2*MG.-1*HP.2*FL.3*DSM.1705918280607*RS.1; TART=%1%enc%3A3UjHP0hxMoEeiWiEb4hn1GHdFnlXt5jRmxFA%2BVelwUBTuWubB3XaBU6D0OhtTnOMFioeLofXw4s%3D; TASID=BB80A659EB4D416596C18074D91A62F4; PAC=AP9kFRw5UwC_oDwiuqSzBCUPvHEUWh9i03QEAzBnN_p2qXMF2f3jt31bfigVC6k6eIpRDo6Q61MCBdWG1JPA13X1E5A2FjYhfPkbH_LCO7FIVDbzi6EoghhhyNkNLWBsDfe5XfMrBZtDL8rVYpJJ8sC2UGsQanaMFC-OuojgZhFm8-lCzPKjPihrebD2roIxnXZNTQ2uzGt6Hm6WYEygZsJU_mNZ5vzPBTWSLcdQSDT-sA9UO14uSdgzlw1AjehBfw%3D%3D; SRT=%1%enc%3A3UjHP0hxMoEeiWiEb4hn1GHdFnlXt5jRmxFA%2BVelwUBTuWubB3XaBU6D0OhtTnOMFioeLofXw4s%3D; ServerPool=T; TAReturnTo=%1%%2FHotel_Review-g187785-d8604500-Reviews-Villa_Albina-Naples_Province_of_Naples_Campania.html; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%2276279e69-e576-8fe5-a943-3e74d708fd36%22%2C%22c%22%3A1701881600023%2C%22l%22%3A1705942452110%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%225a59d448-fc72-dd21-7f19-a3b2dd13e4bc%22%2C%22e%22%3A1705942512123%2C%22c%22%3A1705942452109%2C%22l%22%3A1705942452123%7D; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jan+22+2024+17%3A55%3A27+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=cf5cfbae-de30-4da5-9c53-1c40df81c719&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1%2CV2STACK42%3A1&geolocation=DE%3BBY&AwaitingReconsent=false; _ga_QX0Q50ZC9P=GS1.1.1705941818.7.1.1705942527.60.0.0; __vt=9NKZw6WCeRgWmnDqABQCwRB1grfcRZKTnW7buAoPsSrvdHXuBK-z08V_f3yB0F6_Wk1B-3L9EaO-m91TD2AecO8N9_IIHEw0i3mmbL36N9arxVgItjHpeCwdxQsTWs49veNrbiPXa8Nus7U18uITZOJLQzc; roybatty=TNI1625!AM5Bq1wx0H7iFah7dOU8n6l9h0SwUhUCGqoM2xxa1CvImheozkii47A7G2xOLbSLTsd5SQYc%2F2MNGG98fxCr0aSR8NUqCF8o1CKhcjLoUF4QdH8m9T%2FjLyUpd1BYk5j7PFxTyCDhbx70uxd%2BKZjAtPX1Tdbja22QkUzH3%2FGt6i14V0nKIV7qP2MQPLNHtn%2B76A%3D%3D%2C1; datadome=JqIb~xPo3h5jRTfxXXs4KhBnTMYlz9q7QWQUDI3ClkAticceUC9Bl7qf9X9pagajtmd2WCcglEfU2n4JAd1_J8~oJBA8Swlc~40gbwUfLCIMjw3K4Ng9i3qzmoRmkbVl; TASession=V2ID.BB80A659EB4D416596C18074D91A62F4*SQ.8*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.de*FA.1*DF.0*TRA.true*LD.8604500*EAU._; TAUD=LA-1705487191630-1*RDD-1-2024_01_17*HDD-431088877-2024_02_04.2024_02_05*LD-456311195-2024.2.4.2024.2.5*LG-456311197-2.1.F.",
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.tripadvisor.com",
        "referer": "https://www.tripadvisor.com/" + url,
        "sec-ch-device-memory": "8",
        "sec-ch-ua": "^\^Chromium^^;v=^\^116^^, ^\^Not",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "x-requested-by": "7030db09-f35d-476a-9764-51f91b696a8d"
    }
    url2 = url.split('-')
    id = url2[2]
    id = int(id[1:])
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        match = re.search(r'window\.__WEB_CONTEXT__\s*=\s*({.*?});', response.text)
        pattern = r'amenityNameLocalized&quot;:&quot;(.*?)&quot;'
        pattern2 = r'([\d,\.]+) von 5 Sternen'
        pattern3 = r'"streetAddress":"([^"]*)"'

        adress = re.findall(pattern3, response.text)
        matches = re.findall(pattern, response.text)
        match2 = re.search(pattern2, response.text)
        if match2:
            match2 = match2.group(1)
        else:
            match2 = ["None"]
        if match:
            json_data_str = match.group(1)
            json_data_str_fixed = re.sub(r'([{,])(\s*)([a-zA-Z_][a-zA-Z0-9_]*)(\s*):', r'\1\2"\3":', json_data_str)
            try:
                json_data = json.loads(json_data_str_fixed)
                heat_map_data = \
                json_data['pageManifest']['redux']['api']['responses'][f'/data/1.0/hotelDetail/{id}/heatMap']['data'][
                    'items']
                prices = [float(entry['priceDisplay'][:-1].replace(',', '.')) for entry in heat_map_data]
                average_price = sum(prices) / len(prices) if prices else 0
                record = {"price": f"{average_price}", "amenities": matches, "sterne": match2, "adress": adress, "ID": id}
                return record
            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    except requests.RequestException as e:
        print(f"Error making the request: {e}")



def write_to_csv(data, file_path):
    # Check if the file exists, create headers if not
    file_exists = False
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            if headers:
                file_exists = True
    except FileNotFoundError:
        pass

    # Open the file in append mode
    with open(file_path, 'a+', newline='') as file:
        fieldnames = ["price", "amenities", "sterne", "adress", "ID"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write headers only if the file is newly created
        if not file_exists:
            csv_writer.writeheader()

        # Write the data to the CSV file
        csv_writer.writerow(data)

def read_csv(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.extend(row)

data_list = list()
read_csv("links_berlin_cem.csv")
counter = 0
for hotel in data_list:
    counter +=1
    result = parse_hotel_page("https://www.tripadvisor.de/"+hotel)
    print(f"Hotel {counter} of {len(data_list)}")
    csv_file_path = 'berlin.csv'
    write_to_csv(result, csv_file_path)
    time.sleep(8)