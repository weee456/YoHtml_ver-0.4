import yohtml


DOCTYPE = yohtml.DOCTYPE(type='html')
html = yohtml.html(lang='ko')
style = yohtml.style(Class='a', Inside='Background-color', Color='cornflowerblue')
body = yohtml.body()
text = yohtml.h1(size='h1', text='[Python] This is my Library')
List1 = yohtml.List(text='pip install yohtml')
List2 = yohtml.List(text='import yohtml')
btn = yohtml.btn(Class='a', text='Ok')
close = yohtml.close()

file = open('index.html', 'w', encoding='utf8')

f = file.write(DOCTYPE)
f = file.write(html)
f = file.write(style)
f = file.write(body)
f = file.write(text)
f = file.write(List1)
f = file.write(List2)
f = file.write(btn)
f = file.write(close)

file.close()