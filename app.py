from pyquery import PyQuery
from urllib import request
import json

# PUTTY
# response = request.urlopen('https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html')
#
# html = response.read()
# pq = PyQuery(html)
# tag_version = pq('title')
# date_version = pq('body > p:nth-child(3)')
# link_64 = pq('body > div:nth-child(7) > div:nth-child(5) > span.downloadftp')
# link_32 = pq('body > div:nth-child(7) > div:nth-child(4) > span.downloadftp')
# pattern_version = '(\d*\.)?\d+'
# pattern_date = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
#
# # print the text of the div
# print(tag_version.html())
# print(link_64.html())
# print(link_32.html())
# print(date_version.html())

#BackupandSync
# response = request.urlopen('http://www.filehippo.com/download_google_drive/tech/')
# html = response.read()
# pq = PyQuery(html)
# tag_version2 = pq('title')
# link = pq('#program-header > div.program-header-download-link-container > a.program-header-download-link.button-link.active.short.download-button')
#
# print(tag_version2.html())
# print(link.html('a').attr('href'))

with open('Existing_Versions.json') as file:
    data = json.load(file)
print(data.get("Firefox"))