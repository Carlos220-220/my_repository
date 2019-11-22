import requests
import json


def get_weather():
    t_url = "https://www.amap.com/service/cityList?version=201911219"
    w_url = "https://www.amap.com/service/weather?adcode={}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    while True:
        response = requests.get(url=t_url, headers=headers).content.decode("utf-8")
        response = json.loads(response)
        if response["update"]:
            break

    all_data = response["data"]["cityData"]["provinces"]
    lst = list()
    for value in all_data.values():
        lst.append(value)

    msg = dict()
    for ct in lst:
        name = ct['cities']
        for i in name:
            p_name = i["name"]
            p_code = i["adcode"]
            msg[p_name] = p_code
        if not name:
            name = ct["name"]
            code = ct["adcode"]
            msg[name] = code

    for c in msg.items():
        w_response = requests.get(url=w_url.format(c[1]), headers=headers).content.decode("utf-8")
        w_response = json.loads(w_response)
        try:
            get_data = w_response["data"]["data"]
        except Exception as e:
            pass
        else:
            n_data = get_data[0]
            t_data = get_data[1]

            report_time = n_data["report_time"]
            get_now_msg = n_data["forecast_data"][0]
            n_max_temp = get_now_msg["max_temp"]
            n_min_temp = get_now_msg["min_temp"]
            n_weather_name = get_now_msg["weather_name"]
            n_wind_direction_desc = get_now_msg["wind_direction_desc"]
            n_wind_power_desc = get_now_msg["wind_power_desc"]
            print(c[0])
            # print(report_time)
            # print(n_max_temp)
            # print(n_min_temp)
            # print(n_weather_name)
            # print(n_wind_direction_desc)
            # print(n_wind_power_desc)

            get_tomorrow_msg = t_data["forecast_data"][0]
            t_max_temp = get_tomorrow_msg["max_temp"]
            t_min_temp = get_tomorrow_msg["min_temp"]
            t_weather_name = get_tomorrow_msg["weather_name"]
            t_wind_direction_desc = get_tomorrow_msg["wind_direction_desc"]
            t_wind_power_desc = get_tomorrow_msg["wind_power_desc"]
            # print(t_max_temp)
            # print(t_min_temp)
            # print(t_weather_name)
            # print(t_wind_direction_desc)
            # print(t_wind_power_desc)

            with open("全国天气数据.txt", "a", encoding="utf-8") as wf:
                wf.write(
"""
城市:{},发布时间:{}
今日天气:{}~{}°C
天气状况:{}
风向:{},风力{}级
明日天气:{}~{}°C
天气状况:{}
风向:{},风力{}级
""".format(c[0], report_time, n_max_temp, n_min_temp, n_weather_name, n_wind_direction_desc,
n_wind_power_desc,
t_max_temp, t_min_temp, t_weather_name, t_wind_direction_desc, t_wind_power_desc)
                )


if __name__ == '__main__':
    get_weather()
