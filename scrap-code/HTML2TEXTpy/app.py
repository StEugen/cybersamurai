from bs4 import BeautifulSoup
import mechanize
import re


def cleanhtml(html):
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()


url = input()
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
html = br.open(url).read().decode('utf-8')
cleanhtml = cleanhtml(html)
soup = BeautifulSoup(html)
final_text = soup.get_text()
print(final_text)
