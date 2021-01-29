from html.parser import HTMLParser
def read_int(): return int(input())
def read_int_words(): return map(int,input().split())
def pa(a):
    for ai in a:
        (k,v) = ai
        print("->",k.strip(),">",str(v).strip())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag.strip())
        pa(attrs)
    def handle_endtag(self, tag): print("End   :",tag.strip())
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag.strip())
        pa(attrs)
n = int(input())
parser = MyHTMLParser()
for i in range(n): parser.feed(input())
