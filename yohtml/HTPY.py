
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

def li(text2=str):
        tag_02 = '<li>' + text2 + '</li>'
        return tag_02




def style(Class2=str, Inside2=str, Color2=str):
    if Class2 == 'a':
        if Inside2 == 'Background-color':
            Inside2.__init__()
            Inside2 = '{Background-color:'+ Color2 +';}'
            tag_2 = '<style> .'+ Class2 + Inside2 +'</style>' 
            return tag_2
        else:
            tag_2 = '<style>.a {Background-color:'+ Color2 +';} </style>'
            return tag_2



def Button(Class2=str, text2=str):
    if not Class2:
        tag_01 = '<Button>' + text2 + '</Button>'
        return tag_01
    elif Class2:
        tag_02 = '<Button class="'+ Class2 +'">'+ text2 +'</Button>'
        return tag_02
                    
def body():
    tag_01 = '<body>'
    return tag_01

def Text(size2=str, text2=str):
    if size2 == 'h1':
        tag_01 = '<h1>' + text2 + '</h1>'
        return tag_01
    elif size2 == 'h2':
        tag_02 = '<h2>' + text2 + '</h2>'
        return tag_02
    elif size2 == 'h3':
        tag_03 = '<h3>' + text2 + '</h3>'
        return tag_03
    elif size2 == 'h4':
        tag_04 = '<h4>' + text2 + '</h4>'
        return tag_04
    elif size2 == 'h5':
        tag_05 = '<h5>' + text2 + '</h5>'
        return tag_05
    elif size2 == 'h6': 
        tag_06 = '<h6>' + text2 + '</h6>'
        return tag_06

def all_close():
    close_tag_01 = '</body>'
    close_tag_02 = '</html>'
    return close_tag_01 + close_tag_02