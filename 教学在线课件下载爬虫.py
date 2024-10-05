import requests
from bs4 import BeautifulSoup
import requests
import os

cookies = {
    'JSESSIONID': '5B1B6F80897D1DF9129E497A09E40CC3.TM1',
    'DWRSESSIONID': 'wWXft$wWHxf83RfsvJiE5Eujr0p',
    'Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616': '1712994412',
    'Hm_lvt_242c27c7689290b81407f20c9264ca25': '1725874356,1726138697,1727343615,1728108644',
    'HMACCOUNT': '6C635DCFB517FC01',
    'Hm_lpvt_242c27c7689290b81407f20c9264ca25': '1728108899',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'JSESSIONID=5B1B6F80897D1DF9129E497A09E40CC3.TM1; DWRSESSIONID=wWXft$wWHxf83RfsvJiE5Eujr0p; Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616=1712994412; Hm_lvt_242c27c7689290b81407f20c9264ca25=1725874356,1726138697,1727343615,1728108644; HMACCOUNT=6C635DCFB517FC01; Hm_lpvt_242c27c7689290b81407f20c9264ca25=1728108899',
    'priority': 'u=0, i',
    'referer': 'https://eonline.jw.scut.edu.cn/meol/common/script/left.jsp?lid=33667&groupid=4',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'frame',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}

params = {
    'lid': '33667',
    'folderid': '174258',
}

response = requests.get(
    'https://eonline.jw.scut.edu.cn/meol/common/script/listview.jsp',
    params=params,
    cookies=cookies,
    headers=headers,
)
homePage=response.text
# print(homePage)
soup = BeautifulSoup(homePage,'html.parser')
all_title1=soup.findAll("a")
# for title1 in all_title1:
#     print(title1)
# 查找所有的<a>标签
all_links = soup.find_all("a")
# 初始化一个空数组来存储完整的URL
full_urls = []

# 遍历所有的<a>标签并构建完整的URL
for link in all_links:
    href = link.get('href')
    if href and '###' not in href:  # 如果href属性存在
        # 如果href不是绝对路径，则拼接基础URL
        if href.startswith('preview'):
            full_url = 'https://eonline.jw.scut.edu.cn/meol/common/script/' + href
            # 将完整的URL添加到数组中
            full_urls.append(full_url)
            print(full_url)


import requests

cookies = {
    'JSESSIONID': '5B1B6F80897D1DF9129E497A09E40CC3.TM1',
    'DWRSESSIONID': 'wWXft$wWHxf83RfsvJiE5Eujr0p',
    'Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616': '1712994412',
    'Hm_lvt_242c27c7689290b81407f20c9264ca25': '1725874356,1726138697,1727343615,1728108644',
    'HMACCOUNT': '6C635DCFB517FC01',
    'Hm_lpvt_242c27c7689290b81407f20c9264ca25': '1728108903',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'JSESSIONID=5B1B6F80897D1DF9129E497A09E40CC3.TM1; DWRSESSIONID=wWXft$wWHxf83RfsvJiE5Eujr0p; Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616=1712994412; Hm_lvt_242c27c7689290b81407f20c9264ca25=1725874356,1726138697,1727343615,1728108644; HMACCOUNT=6C635DCFB517FC01; Hm_lpvt_242c27c7689290b81407f20c9264ca25=1728108903',
    'priority': 'u=0, i',
    'referer': 'https://eonline.jw.scut.edu.cn/meol/common/script/listview.jsp?lid=33667&folderid=155132',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}

params = {
    'fileid': '1908543',
    'resid': '155142',
    'lid': '33667',
}
full_download_urls = []
for url in full_urls:
    response = requests.get(
        url,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    homePage = response.text
    # print(homePage)
    soup = BeautifulSoup(homePage, 'html.parser')
    all_links = soup.find_all("a", class_="icon32 lv-download")  # 限定class以筛选特定的链接

    # 遍历所有的<a>标签并提取href属性
    for link in all_links:
        href = link.get('href')
        if href:  # 如果href属性存在
            # 如果href不是绝对路径，则拼接基础URL
            if not href.startswith(('http://', 'https://')):
                full_url = 'https://eonline.jw.scut.edu.cn/' + href.lstrip('/')
            else:
                full_url = href
            # 将完整的URL添加到数组中
            full_download_urls.append(full_url)

# 打印数组中的所有URL
for url in full_download_urls:
    print(url)

# 指定保存文件的目录
save_directory = r"C:\Users\abc\Desktop\文件\学习资料\复习课件讲义\离散数学"

# 确保目录存在
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# 遍历每个URL
for index, url in enumerate(full_download_urls, start=1):
    try:
        # 发起HTTP GET请求
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 生成文件名，例如：1.pdf, 2.pdf, ...
        file_name = f"{index}.pptx"  # 假设文件是PDF格式，根据实际情况调整
        file_path = os.path.join(save_directory, file_name)

        # 保存文件
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # 过滤掉保持连接的chunk
                    file.write(chunk)

        print(f"文件已下载并保存到：{file_path}")

    except requests.RequestException as e:
        print(f"下载失败：{url}，错误信息：{e}")

print("所有文件下载完成。")




