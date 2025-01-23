import requests
import json
import pandas as pd

# 请求头和Cookie
cookies = {

}

headers = {

}

params = {

}

data = {

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
