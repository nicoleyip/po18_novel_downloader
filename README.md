# PO18-Novel-txt-downloader

## First Of All

本项目fork自 [PO18-Novel-Txt-Downloader](https://github.com/Theseuship/PO18-Novel-Txt-Downloader) ，并在其基础上略做修改，因目前po18登录需进行验证码校验，原有登录逻辑无法实现目标，故请求头中需携带用户cookie以进行身份校验。

将 https://www.po18.tw 网站上的小说下载为 txt 文档。

大陆地区无法访问此网站，须使用代理。

只能取得免费 / 已购章节内容。收费章节请先手动购买。

开发环境：Python 3.12

## import

BeautifulSoup

requests

lxml

## How to use

1. 先找到要下载的书籍 ID（网址`/books/` 后面那串数字），赋值给 `book_number` 。

2. 找到章回列表总页数，赋值给 `chapter_page_sum`。

3. 如何获取cookie：以Chrome为例，网页登录po18后，右键选择检查 或 按F12 打开开发者工具，选择Network一栏，刷新页面，找到一个网络请求，在Headers一栏，找到Request Headers里面的Cookie，复制出来赋值给`cookies`（此信息存在本地，只会发送给 po18 的服务器登录用）。

4. 更改 `txt = open('路径' + book_number + '.txt', 'a')`，随便找个文件夹路径，替换掉中文字符。

5. 下载后，可使用Calibre制作epub等格式的电子书，并添加目录，相关设置请自行Google。

6. 此脚本默认下载一节间隔0.5s，为避免网站屏蔽，请适度使用此脚本。




