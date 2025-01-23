import requests
import json
import pandas as pd

# 请求头和Cookie
cookies = {
    'JSESSIONID': 'FBDCE474C1196603E73E88BAED9BE731',
    'Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616': '1712994412',
    'SERVERID2': 'Server1',
    'Language': 'zh_CN',
    'clwz_blc_pst_SSO': '872097482.20480',
    'clwz_blc_pst_jwc_xd1xa7xc9xfa': '2097832970.20480',
    '_webvpn_key': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMzMwNDIyMzIxIiwiZ3JvdXBzIjpbNDcsNDZdLCJpYXQiOjE3Mzc2MTM4NTQsImV4cCI6MTczNzcwMDI1NH0.ZvuDw8FEo7wmg4QyjgAQOVFw1Qik6BjkKpklDUZ3aPc',
    'webvpn_username': '202330422321%7C1737613854%7C5c082ba279ad89a5adb2dee74c736325f97934cc',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://xsjw2018-jw.webvpn.scut.edu.cn',
    'priority': 'u=1, i',
    'referer': 'https://xsjw2018-jw.webvpn.scut.edu.cn/jwglxt/design/viewFunc_cxDesignFuncPageIndex.html?gnmkdm=N3050hg003&layout=default',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'func_widget_guid': 'C4D8BB4483741F17E05399C226CA866F',
    'gnmkdm': 'N3050hg003',
}

data = {
    '_search': 'false',
    'nd': '1737614001992',
    'queryModel.showCount': '50',
    'queryModel.currentPage': '1',
    'queryModel.sortName': ' ',
    'queryModel.sortOrder': 'asc',
}

# 发送请求
response = requests.post(
    'https://xsjw2018-jw.webvpn.scut.edu.cn/jwglxt/design/funcData_cxFuncDataList.html',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

# 检查响应状态
if response.status_code == 200:
    try:
        # 解析JSON数据
        data = response.json()
        items = data["items"]

        # 将数据转换为DataFrame
        df = pd.DataFrame(items)

        # 选择需要的列
        df = df[["kcmc", "kcxzmc", "cj", "pm", "xf", "xnmmc"]]  # 增加学分和学年两列

        # 重命名列名
        df.columns = ["课程名称", "课程属性", "分数", "排名", "学分", "学年"]

        # 将数据写入Excel文件
        output_file = "course_results.xlsx"
        df.to_excel(output_file, index=False, engine="openpyxl")

        print(f"数据已成功写入文件：{output_file}")
    except json.JSONDecodeError:
        print("解析JSON数据失败，请检查返回的内容是否为有效的JSON格式。")
    except KeyError as e:
        print(f"JSON数据中缺少必要的字段：{e}")
else:
    print(f"请求失败，状态码：{response.status_code}")