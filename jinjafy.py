from pathlib import Path
from bs4 import BeautifulSoup
import sys

from collections import defaultdict

ext = ['.css','.jpg','.png','icon']
BASE_DIR = Path(__file__).resolve().parent.parent

def css_m(i_css):
    t_css = ''
    ex_css = ''
    in_css = ''
    for styl in i_css:
        if styl['href']:
            lnk_styl = styl['href']
            for ex in ext:
                if str(lnk_styl).endswith(ex) :
                    f_s = '\\'
                    static = f"[# static '{styl['href']}' #]"
                    t_css += '\n'+str(styl).replace(styl['href'],static).replace('/',f_s)
                else:
                    pass
        
        ex_css += '\n'+str(styl)
    
    
    css = t_css 
    return css

def js_m(i_js):
    t_js = ''
    ex_js = ''
    in_js = ''
    for scrpt in i_js:
        if scrpt['src']:
            lnk_scrpt = scrpt['src']
            for ex in ext:
                if str(lnk_scrpt).endswith(ex) :
                    f_s = '\\'
                    static = f"[# static '{scrpt['src']}' #]"
                    t_js += '\n'+str(scrpt).replace(scrpt['src'],static).replace('/',f_s)
                else:
                    pass
        
        ex_js += '\n'+str(scrpt)
    
    
    js = t_js 
    return js



def Djangofy(file,path):
    
    #r_file = file[0]
    file = open(f'{file}','r').read()

    soup = BeautifulSoup(file,features='html.parser')

    head = soup.find('head')

    #_css = head.find_all('link')

    body = soup.find('body')
    
    #_js = soup.find_all('script')
    
    for ik in body.find_all('script'):
        static = f"[# static '{ik['src']}' #]"
        ik['src'] = static
        #print(f"changing js \n of :{ik['src']}") 
        
    for ik in head.find_all('link'):
        static = f"[# static '{ik['href']}' #]"
        ik['href'] = static
        #print(f"changing css \n of :{ik['href']}") 
    
    for ik in body.find_all('img'):
        static = f"[# static '{ik['src']}' #]"
        ik['src'] = static
        #print(f"changing img \n of :{ik['src']}") 

    
    #print(_js)
    

    idx = open(f'{BASE_DIR}/Djangofy/templates/index.txt').read()

    #print( f"{idx.replace(newline, '')}".format(**locals()))

    """ d = defaultdict(str)
    d['error6'] = "success"
    s = "i am an {0[error]} example string {0[error6]}" """
    #print(s.format(d))
    base_pth = f"'base.html'"


    wsum = defaultdict(str)

    wsum['meta'] = head
    wsum['ext_base'] = base_pth
    wsum['body'] = body

    html = idx.format(wsum)

    """ for a in head.find_all('link'):
        a['href'] = f"[# static '{styl['href']}' #]" """

    #print(html)
    #print(r_css)
    html = html.replace('[#','{%').replace('#]','%}')
    soup = BeautifulSoup(html,features="html.parser")
    html = soup.prettify()
    return html


""" file = Djangofy('/home/mr-13/Documents/py/Projects/Djangofy/html/css/about.html')

with open('file.html','w') as fl:
    fl.write(file) """
    
if __name__ == '__main__':
    """ if __name__ == "__main__":
    main(sys.argv[1:])
    input("\nPress Enter to continue...") """
    """ file = Djangofy('/home/mr-13/Documents/py/Projects/Djangofy/html/css/about.html') """
    file = Djangofy(sys.argv[1:])
    with open('file.html','w') as fl:
        fl.write(file)
    print(f"wrote file ....")