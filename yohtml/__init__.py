import yohtml.HTPY

def DOCTYPE(type = str):
    if type == 'html':
        D = yohtml.HTPY.DOCTYPE(type='html')
        return D

def html(lang = str):
    if lang == 'en':
        h = yohtml.HTPY.html(lang='en')
        return h
    elif lang == 'ko':
        h2 = yohtml.HTPY.html(lang='ko')
        return h2
def style(Class=str, Inside=str, Color=str):
    if Class:
        if Inside == 'Background-color':
            s = yohtml.HTPY.style(Class2=Class, Inside2=Inside, Color2=Color)
            return s
            
def body():
    b = yohtml.HTPY.body()
    return b

def h1(size=str, text=str):
    hh = yohtml.HTPY.Text(size2=size, text2=text)
    return hh

def List(text=str):
    l = yohtml.HTPY.li(text2=text)
    return l
def btn(Class=str, text=str):
    if Class:
        B = yohtml.HTPY.Button(Class2=Class, text2=text)
        return B
    elif not Class:
        B2 = yohtml.HTPY.Button(text2=text)
        return B2

def close():
    close = yohtml.HTPY.all_close()
    return close

