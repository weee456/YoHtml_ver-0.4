def DOCTYPE(type = str):
    if type == 'html':
        DOC = '<!DOCTYPE html>'
        return DOC
    
def html(lang = str):
    if lang == 'en':
        tag_01 = '<html lang="en">'
        return tag_01
    elif lang == 'ko':
        tag_02 = '<html lang="ko">'
        return tag_02

def body():
    tag_01 = '<body>'
    return tag_01

def Text(size=str, text=str):
    if size == 'h1':
        tag_01 = '<h1>' + text + '</h1>'
        return tag_01
    elif size == 'h2':
        tag_02 = '<h2>' + text + '</h2>'
        return tag_02
    elif size == 'h3':
        tag_03 = '<h3>' + text + '</h3>'
        return tag_03
    elif size == 'h4':
        tag_04 = '<h4>' + text + '</h4>'
        return tag_04
    elif size == 'h5':
        tag_05 = '<h5>' + text + '</h5>'
        return tag_05
    elif size == 'h6': 
        tag_06 = '<h6>' + text + '</h6>'
        return tag_06

def all_close():
    close_tag_01 = '</body>'
    close_tag_02 = '</html>'
    return close_tag_01 + close_tag_02