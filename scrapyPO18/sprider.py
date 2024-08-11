# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time


def getContent(page):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'www.po18.tw',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Cookie': cookies
        }
    global content_url
    if page > 1:
        content_url = content_url + '?page=' + str(page)
    response = session.get(content_url, headers=headers)
    print('page %d %s processing...' % (page, content_url))
    soup = BeautifulSoup(response.text, 'lxml')
    chapter_list = soup.find_all(name='a', attrs={'class': 'btn_L_blue'})
    chapter_order_list = soup.find_all(name='div', attrs={'class': 'l_counter'})

    global start
    for i in range(start, len(chapter_list)):
        chapter_url = 'https://www.po18.tw' + chapter_list[i].get('href')
        chapter_order = chapter_order_list[i].get_text()
        print('%d %s processing...' % (i, chapter_url))
        time.sleep(0.5)
        getChapter(chapter_url, chapter_order, 10)

    global chapter_page_sum
    if (chapter_page_sum - page) > 0:
        page += 1
        getContent(page)


def getChapter(chapter_url, chapter_order, time):
    try:
        text_url = chapter_url.replace("articles", "articlescontent")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1',
            'Host': 'www.po18.tw',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Cookie': cookies,
            'Referer': chapter_url
        }
        response = session.get(text_url, headers=headers, timeout=10)
        chapter = response.text.replace("&nbsp;&nbsp;", '')
        soup = BeautifulSoup(chapter, 'lxml')
        chapter_title = soup.find('h1').get_text()
        if len(soup.find_all('p')) < 10:
            print('Unknown error, reloading... %d' % (11 - time))
            time = time - 1
            getChapter(chapter_url, chapter_order, time)
        if time == 1:
            print('Failed, pass.')
            pass
        else:
            print('%s processing...' % (chapter_title))
            txt.write('第' + chapter_order + '章 ' + chapter_title + '\n')
            text = soup.find_all(name='p')
            for row in text:
                txt.write(row.get_text())
            txt.write('\n')
            txt.write('\n')
            txt.write('\n')
            print('%s done.' % chapter_title)
    except requests.exceptions.ConnectionError:
        print('ConnectionError, reloading...')
        getChapter(chapter_url, chapter_order, time)
    except requests.exceptions.ReadTimeout or RuntimeError:
        print('ReadTimeout or RuntimeError, reloading...')
        getChapter(chapter_url, chapter_order, time)


book_number = 'YOUR TARGET BOOK'
content_url = 'https://www.po18.tw/books/' + book_number + '/articles'
chapter_page_sum = 1
cookies = 'YOUR COOKIE'
start = 0
session = requests.session()
txt = open('YOUR PATH' + book_number + '.txt', 'a')
getContent(1)
txt.close()
