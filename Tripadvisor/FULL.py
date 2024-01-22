import json
import re
import requests
from typing import Dict
import csv
import time

def parse_hotel_page(url: str) -> Dict:
    """Parse hotel data from hotel pages using Requests."""
    headers = {
        "cookie": "TASameSite=1; TAUnique=%1%enc%3Au%2FKH8yQEGOQTegLLIkrpW8vVzrWrB0%2F4kjL03oi4j7g2jHwltRJPGQ%3D%3D; TASSK=enc%3AAJRX%2FVirFQxh3L%2FWxzIIJifHMc5WZOSjC5CsLacwCJkioVsG3hAwHyxqX5CpZYTYTInWf1F9gvG06JZHPKhp1LGdKAPGuNkLXCRUdEDtOVHDlmzTlzXC3Hx1ccZfybQMMw%3D%3D; OptanonAlertBoxClosed=2023-08-10T08:05:36.557Z; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.501.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.11031; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _ga=GA1.1.105187867.1691654737; _lr_env_src_ats=false; VRMCID=%1%V1*id.10568*llp.%2FRestaurants-g187791-oa30-Rome_Lazio%5C.html*e.1692278351437; pbjs_sharedId=f9e74d2f-efbb-4cf3-8954-9ade47197af6; RT='z=1&dm=www.tripadvisor.com&si=322d1533-3317-45f0-b62a-d492f9be7df7&ss=lm96xuca&sl=0&tt=0&ld=1avmc&ul=32ry&hd=3322'; TALanguage=ALL; TADCID=rrKCatH-3oNDmiZrABQCCKy0j55CTpGVsECjuwJMq3g0b32Ijw6wWOXey6u8mWHz0scFAskyGT2z0GrieTQt_8YFSAbZJ3Ef9CE; PAC=AOT-dM6DuLq0iE9Pu2RgxiWFUs4mdujwCt_5UmCCIMsZ8R3vPIideAS-Ayf81J4JzScIdXZyXxnaIRQdw4SBvEvJSvIA6gVvRZANu2XaVJTX7Bn7xkzYhFop9GRYFuUVBFOh5v43qWQzRDwnL70XJIWXoT0Is9ktyGULz3Uw1iTKi3P6wl8vnXUZhMLMQXcZEIwuo0olK228TIb15DczCOP2TuxZhfG8J_wkANJmhI3OSeivugf3VpTOIZX4hB9RDQ%3D%3D; PMC=V2*MS.6*MD.20230810*LD.20230914; TASID=C9F5A95486494D498DFB9273026A9B8E; _abck=B696544D010E502E37A2B8896BFBAAFC~-1~YAAQTI8UAsdtsYiKAQAAU6u2kgpbW6foLe5NB/5MAKZoR/X9Q/mgNTP/5NeHntzcePv5og/QhDOHbrrKxgiTqTbB8v09T9HlxnQDv0NmfSZOyIscBwlnsrvTt7WhrRzFFjCA7e1VdtvpmxXzh3IYrBDJGsn8JxyzpAjuSXAFdis9puqYBpG3clO3a4UKanWp2H+Olk4cPY6SRfvM+WV26DB6TdBq3s/qz64Mqny+zBc99cgo11mDOdb6weYt61ojm/fULAFlc7xDYqDnruqKmZKzKXYbjiSWF83jKMP8dzP9rlcmD1lmDb7cXfBKNbZEabdt/uJ3DRh0hpEprAqISy7Y1E/1NDKBljDo1ufq/0hbjBNzZOG9FaRsZWN1lE1iHGqn7JeKRwDNXTFwRj30~-1~-1~-1; bm_sz=93FF4053B2C4FD1518B1A48C420F253F~YAAQTI8UAshtsYiKAQAAU6u2khXATC8sYKCKZ00ZUL5qrJOl4Cm6QSOI+6BU/y/3Gf0PRwYdXHzghAfggVkR7pKpbryDfs2ouWWl+VsPuSavgzAUoAr6oS0/VWNKjPt4Iv1tRnGTClw7IM3iMafPJUYnFwiBrdFH6ec5NFqgpRS743xHNtdCvRCgOHZnZn3eI7Rmuw+huo+sdBdLmI1rp1OE9ZPlI/ABA9Imt+iS7XHm88FPLI4E6AuMzo0Cq5OObyknkUOQxrMW8JbvcOFKdQCi1RZ3OFaP8OXNAK7eP7Qs10zx8k3/AQ==~3162933~3421506; TATravelInfo=V2*AY.2023*AM.9*AD.24*DY.2023*DM.9*DD.25*A.2*MG.-1*HP.2*FL.3*DSM.1694678560533*RS.1*RY.2023*RM.9*RD.7*RH.20*RG.2; eupubconsent-v2=CPwSHvAPwSHvAAcABBENDWCsAP_AAH_AACiQGBtX_T5eb2vi-3ZcN7tkaYwP55y3o2wjhhaIEe0NwIOH7BoCJ2MwvBV4JiACGBAkkiKBAQVlHGBcCQAAgIgRiSKMYk2MjzNKJLJAilMbM0MYCD9mnsHT2ZCY70-uO7_zvneBtgBJgoXEADYEhATLRhBAgAGEYQFQAgAoAEgKADCEAEBOwKAj1gIAAACAAEAAAAAIIgAQAACQBIRAAAAYCAQAAQCAAEAAoQCAAiQABYAWgAEAAoBoSAUUAQgGEGBCBEKYEAQAAAAAAAAAAAAAAAAEAoEAMAB0AFwAbIA8ACIAGEAToAuQBnADbAHaAQOCACAAdACuAIgAYQBOgDOAHaAQODABgAdAEQAMIAzgB2gEDhAAcAHQBEADCAJ0AZwA7QCBwoAGAYQBnAEDhgAUAVwBhAGcANsAgcOAEAA6AFcARAAwgCdAGcAO0AgcQABgGEAZwBA4kADAIgAYQCBxQAOADoAiABhAE6AM4AdoBA4A.f_gAD_gAAAAA; _pbjs_userid_consent_data=2972944405373433; TART=%1%enc%3AE3oCyyJK6VsiV1RAriBqnZx3JfD2Bcb3yRWQoIhsrLcdMjDdqxbGSVMQoKKnX5kdRsNr41gHGgI%3D; _lr_sampling_rate=100; _lr_retry_request=true; ServerPool=C; SRT=%1%enc%3AE3oCyyJK6VsiV1RAriBqnZx3JfD2Bcb3yRWQoIhsrLcdMjDdqxbGSVMQoKKnX5kdRsNr41gHGgI%3D; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%229e8b7f45-985b-091a-b024-e76dfb63b1a6%22%2C%22c%22%3A1694077354560%2C%22l%22%3A1694678953374%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%226f03f882-441c-b6f2-d643-a79b5506b18e%22%2C%22e%22%3A1694679547706%2C%22c%22%3A1694678953373%2C%22l%22%3A1694679247706%7D; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+14+2023+10%3A39%3A39+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=d441c948-c24d-4205-b448-c56915616069&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&geolocation=DE%3BBY&AwaitingReconsent=false; _ga_QX0Q50ZC9P=GS1.1.1694678561.13.1.1694680780.60.0.0; __gads=ID=67a9e384c621d837:T=1691654736:RT=1694681894:S=ALNI_MZL6G0ZJ2UtWkjFEZIjg3-g3DBnkg; __gpi=UID=00000c5da7c0892e:T=1691654736:RT=1694681894:S=ALNI_MaW6pSlD80w367lOAHP1NBi-LWvZg; __vt=7EoVkJVAp0RWpKvXABQCCQPEFUluRFmojcP0P3EgGigSR-8A1wjK5Vynyh3bRKzJHE8aXnGxAaQhfiJctHXeoQdXwRkzhKuteMj_pxSOrIny-RR3pN2OYjLCW0y3hTregLnBVHcuYirOSj4tSN5S9QOp9g; TASession=V2ID.C9F5A95486494D498DFB9273026A9B8E*SQ.37*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.en*FA.1*DF.0*TRA.false*LD.241729*EAU._; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7C; TAUD=LA-1691654844191-1*RDD-1-2023_08_10*HDD-2422506293-2023_09_17.2023_09_18*RD-2443660169-2023_09_07.25560545*ARDD-3023716566-2023_09_24.2023_09_25*LD-3027093730-2023.9.24.2023.9.25*LG-3027093735-2.1.F.; TAReturnTo=%1%%2FHotel_Review-g2089121-d241729-Reviews-or10-Lopesan_Costa_Meloneras_Resort_Spa-Meloneras_Gran_Canaria_Canary_Islands.html; datadome=56g26Virg~XYRXcN7QfyQjWU3~NXjU5y8cxR-cHge5-VLgqjXI5u6QMnhsBQQh0VWQdvVSTxzrspuuXkWnEOJ~v09SIP~0FSUp8EZrps7lQYLI0pM-~0Jbep26LSEdHL; roybatty=TNI1625!AIsSCgpQEZ9kqpmdc2jgSEstxXoiNI89g4q931nU4NDV4w%2FW0eIvXu5VJC2cSLxw6V2%2BVXNlgEmyhyUv%2BRUXFmks0KiY7RpyXHBp%2FwThtiZjgZsjbS5xx%2FnI6Lh7s4HREzpAGlGTcx79WkuJCUotKo8BZOnWK%2FjXKnXrfj%2FkeJa2%2C1",
        "authority": "www.tripadvisor.com",
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.tripadvisor.com",
        "referer": "https://www.tripadvisor.com/" + url,
        "sec-ch-device-memory": "8",
        "sec-ch-ua": "^\^Chromium^^;v=^\^116^^, ^\^Not",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "x-requested-by": "TNI1625!AObMdBZi1Fmcp8iF2YaS74eAKkuf2dzjZbqbc4sWgdjHZSrF4usjMKEJdITNUeLQ+bcFU9+JIpFiFvx2W0E2/ov3PeV+0p/qMLqdsL+KxumH87/OBx8+M54wQTq7Do6dax8Djczy5km1TJrON783AQ6hNK2x0MLlwH+tR+zT7m2L"
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
            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    except requests.RequestException as e:
        print(f"Error making the request: {e}")
    return record


def write_to_csv(data, file_path):
    # Check if the file exists, create headers if not
    file_exists = False
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=";")
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
read_csv("links_naples.csv")
counter = 0
for hotel in data_list:
    counter +=1
    result = parse_hotel_page("https://www.tripadvisor.de/"+hotel)
    print(f"Hotel {counter} of {len(data_list)}")
    csv_file_path = 'output2.csv'
    write_to_csv(result, csv_file_path)
    time.sleep(8)