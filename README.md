# PyHtml
HTML 파싱  모듈 개발 (24/06/2023{FM 11:38} address : Korea) by : weee456

# ko-kr(사용법) | en-us(Instructions)

pip install PyHtml

===================================================================

from pyhtml import pyhtml

============================Lib import======================================

DOCTYPE = pyhtml.HTPY.DOCTYPE(type='html')

html = pyhtml.HTPY.html(lang='ko')

body = pyhtml.HTPY.body()

h1 = pyhtml.HTPY.Text(size='h1', text='hi')

close = pyhtml.HTPY.all_close()

file = open('html_test.html','w',encoding='UTF-8')

=============================Parsing========================================

f = file.write(DOCTYPE)

f = file.write(html)

f = file.write(body)

f = file.write(h1)

f = file.write(close)

file.close

==============================save============================================

# ko-kr(결과) en-us(result)



![자료](https://github.com/weee456/PyHtml/assets/133841941/32642a0b-b3fb-4388-834a-d440392bae04)




