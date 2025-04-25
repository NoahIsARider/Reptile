import re
import requests
from requests.exceptions import RequestException
import pymysql
import time

# 连接到 MySQL 数据库
def connect_to_mysql():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="douban_top250",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# 创建表
def create_table(connection):
    try:
        with connection.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS douban_top250 (
                id INT AUTO_INCREMENT PRIMARY KEY,
                movie_rank INT,
                title VARCHAR(255),
                score FLOAT,
                num_of_votes INT,
                director VARCHAR(255),
                release_year VARCHAR(255),  # 修改为 VARCHAR(255) 以容纳多个年份
                country VARCHAR(255),
                theme VARCHAR(255),
                summary TEXT,
                movie_url VARCHAR(255)
            )
            """
            cursor.execute(create_table_query)
        connection.commit()
    except pymysql.Error as err:
        print(f"Error creating table: {err}")

# 获取单页 HTML 内容
def get_one_page(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://movie.douban.com/top250?start=225&filter=',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 解析单页 HTML 内容并插入到数据库
def parse_one_page(html, connection):
    # 修改后的正则表达式，处理多个年份的情况
    pattern = re.compile(
        '<li>.*?<em class="">(\d+).*?href="(.*?)">.*?alt="(.*?)".*?</a>.*?<p class="">.*?:(.*?)[^A-Za-z.]'
        '[<br>|&nbsp;&nbsp;&nbsp;].*?([\d() ]+)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n.*?:average">([1-9]\d*\.\d*|0\.\d*[1-9]\d*).*?'
        + '<span>(\d+)人评价</span>.*?(?:<p class="quote"><span class="inq">(.*?)</span></p>)?.*?</li>', re.S
    )
    items = re.findall(pattern, html)
    try:
        with connection.cursor() as cursor:
            insert_query = """
            INSERT INTO douban_top250 (movie_rank, title, score, num_of_votes, director, release_year, country, theme, summary, movie_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            for index, item in enumerate(items):
                movie_rank = int(item[0])
                name = item[2]
                score = float(item[7])
                num_of_votes = int(item[8])
                director = item[3]
                # 处理多个年份的情况
                release_year = item[4].strip()
                country = item[5]
                theme = item[6]
                # 如果没有评论，item[9] 为空字符串
                summary = item[9] if item[9] else ''
                movie_url = item[1]

                # 打印数据清洗结果和过程监督信息
                print(f"Processing movie {index + 1}:")
                print(f"  Movie Rank: {movie_rank}")
                print(f"  Title: {name}")
                print(f"  Score: {score}")
                print(f"  Number of Votes: {num_of_votes}")
                print(f"  Director: {director}")
                print(f"  Release Year: {release_year}")
                print(f"  Country: {country}")
                print(f"  Theme: {theme}")
                print(f"  Summary: {summary}")
                print(f"  Movie URL: {movie_url}")

                data = (movie_rank, name, score, num_of_votes, director, release_year, country, theme, summary, movie_url)
                cursor.execute(insert_query, data)
        connection.commit()
    except pymysql.Error as err:
        print(f"Error inserting data: {err}")

def main(i, connection):
    url = f'https://movie.douban.com/top250?start={i}&filter='
    html = get_one_page(url)
    if html:
        parse_one_page(html, connection)
    time.sleep(1)

if __name__ == '__main__':
    connection = connect_to_mysql()
    if connection:
        create_table(connection)
        for i in range(10):
            print(f"Processing page {i + 1}...")
            main(i * 25, connection)
        connection.close()
