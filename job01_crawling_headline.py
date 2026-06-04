from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()
for i in range(6):
    url = 'https://news.naver.com/section/10{}'.format(i)
    # 유니코드로 홈페이지 코드가 보임
    resp = requests.get(url)
    # 유니코드를 HTML으로 변환
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 클래스가 제목인 내용들만 가져옴
    title_tag = soup.select('.sa_text_strong')
    print(title_tag)
    titles = []
    for title in title_tag:
        titles.append(title.text)
    print(titles)
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)
print(df_titles.head())
df_titles.info()
# 수집한 뉴드 헤드라인들을 CSV파일로 저장
df_titles.to_csv('./data/naver_headline_news_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)