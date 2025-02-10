from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

cookies = {
    'll': '"118212"',
    'bid': 'QcTXeGyhtGE',
    '_pk_id.100001.8cb4': '09486f994268ab04.1738913757.',
    'dbcl2': '"227017213:D4eZVHwPiIM"',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    '__utmv': '30149280.22701',
    '__yadk_uid': 'K9qLEVvspN244q0xy8ftVEgOzQetJCVc',
    '_vwo_uuid_v2': 'DBAE0F0F4869FEB2573E55766296F7A27|f3adb816615ab310a83a7472c17ce5a4',
    'douban-fav-remind': '1',
    'ck': 'N3SW',
    'ap_v': '0,6.0',
    'frodotk_db': '"3a5c5f8185f6ef4faf151e8491e4cded"',
    '__utmc': '30149280',
    '__utmz': '30149280.1739089168.6.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1739091894%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D',
    '_pk_ses.100001.8cb4': '1',
    '__utma': '30149280.1273408214.1738913757.1739089168.1739091894.7',
    '__utmt': '1',
    '__utmb': '30149280.8.10.1739091894',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
}

base_url = 'https://www.douban.com/doulist/4059268/'

# 创建一个新的工作簿
wb = Workbook()
ws = wb.active
# 添加表头
ws.append(['电影名字', '评分', '导演', '主演', '类型', '制片国家/地区', '年份'])

# 以 25 为步长从 0 到 125 循环
for start in range(0, 151, 25):
    if start == 0:
        url = base_url
    else:
        url = f'{base_url}?start={start}&sort=time&playable=0&sub_type='

    response = requests.get(url, cookies=cookies, headers=headers)
    # 打印响应状态码
    print(f"当前请求的 URL: {url}")
    print(f"响应状态码: {response.status_code}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_items = soup.find_all('div', class_='doulist-item')
        for item in movie_items:
            # 提取电影名字
            title_div = item.find('div', class_='title')
            if title_div:
                movie_name = title_div.find('a').text.strip()
            else:
                movie_name = '未找到电影名字'
            # 提取评分
            rating_div = item.find('div', class_='rating')
            if rating_div:
                rating_span = rating_div.find('span', class_='rating_nums')
                rating = rating_span.text.strip() if rating_span else '暂无评分'
            else:
                rating = '暂无评分'
            # 提取 abstract 部分
            abstract_div = item.find('div', class_='abstract')
            if abstract_div:
                lines = abstract_div.get_text(separator='\n').strip().split('\n')
                director = None
                actors = None
                movie_type = None
                country = None
                year = None
                for line in lines:
                    if '导演:' in line:
                        director = line.replace('导演:', '').strip()
                    elif '主演:' in line:
                        actors = line.replace('主演:', '').strip()
                    elif '类型:' in line:
                        movie_type = line.replace('类型:', '').strip()
                    elif '制片国家/地区:' in line:
                        country = line.replace('制片国家/地区:', '').strip()
                    elif '年份:' in line:
                        year = line.replace('年份:', '').strip()
            else:
                director = '未找到导演信息'
                actors = '未找到主演信息'
                movie_type = '未找到类型信息'
                country = '未找到制片国家/地区信息'
                year = '未找到年份信息'

            # 将提取的信息写入 Excel 表格
            ws.append([movie_name, rating, director, actors, movie_type, country, year])
    else:
        print(f"请求 {url} 失败，状态码: {response.status_code}")

# 保存工作簿
wb.save('movies.xlsx')