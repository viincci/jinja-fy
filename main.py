
import sys
from tqdm import tqdm
import json
import shutil
import os
from pathlib import Path
from jinjafy import Djangofy


def Make(lpth):
        lpth = lpth[0]
        dirs = os.walk(lpth)
        d_lpth = {}
        com = ('.html','.css','.map','.js','.woff','.woff2','.txt','.jpg','.png','.php')

        for i in dirs:
            for k in i:
                if type(k) != list:
                    key = k
                if type(k) == list:
                    for m in k:
                        if m != None and str(m).endswith(com):
                            val = k
                            
            d_lpth[key] = val
        return lpth, d_lpth
    
    
def Finnal( d_lpth,lpth):
    BASE_DIR = Path(__file__).resolve().parent.parent
    wrk_dir = BASE_DIR

    #os.system(f'cd {BASE_DIR}/Djangofy/templates/finals')
    print(f'changing directory \nfrom :{os.getcwd()} \nto :{BASE_DIR}/Djangofy/templates/finals')
    os.chdir(f'{BASE_DIR}/Djangofy/templates/finals')
    try:
        os.mkdir(f'{BASE_DIR}/Djangofy/templates/finals/{lpth}')
    except:
        pass
        #os.rmdir(f'{BASE_DIR}/Djangofy/templates/finals/{lpth}')
    fu = open(f'{BASE_DIR}/Djangofy/templates/base.txt','r').read()

    for _ in tqdm(d_lpth.keys(),'Django-fying-files~'):
        for i , k in d_lpth.items():
                try:
                    if i != lpth:
                        os.mkdir(i)
                    for m in k:
                        src = f'{BASE_DIR}/Djangofy/{i}/{m}'
                        dst = f'{i}/{m}'
                        if str(m).endswith('.html'):
                            #print(m, src,'\n', dst)
                            file =  Djangofy(f'{src}',f'{lpth}')
                            fl = open(f'{dst}','w') 
                            fl.write(file)
                            
                            #print(f'{src}')
                        else: 
                            #print(src,dst)
                            shutil.copy(src,dst)
                except:
                    pass
        os.chdir(f'{BASE_DIR}/Djangofy/templates/finals/{lpth}')
        base = open('base.html','w')
        base.write(fu)
        js = open('path_walk.json','w')
        js.write(json.dumps(d_lpth))    


#pth2 = 'PhotoFolio'
def Main_Djangfy(pth):      
    path, dir_path = Make(pth)
    Finnal(dir_path,path)
    
    


""" file =  Djangofy('about.html')
with open('file.html','w') as fl:
    fl.write(file) """



if __name__ == '__main__':
    pth = 'PhotoFolio'
    #BASE_DIR = Path(__file__).resolve().parent
    """ path, dir_path = Make(pth)
    for _key, _value in dir_path.items():
        print(_key,_value) """
    
    Main_Djangfy(sys.argv[1:])
        
    
    

