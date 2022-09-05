import requests
import os
import shutil
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
from tqdm import tqdm







def get_r(link):
    r = requests.get(link)
    return r.content


def get_l(html):
    soup = BeautifulSoup(html,features='html')
    _links = soup.find_all(name='a',attrs={'class':'download'})
    links = []
    for i in _links:
        links.append(i['href'])
    return links


def delink(link):
    html = get_r(link)
    links  = get_l(html)
    link2 = []
    for lk in links:
        lnk = lk.replace('#','')
        name = str(lk).removeprefix('https://bootstrapmade.com/').removesuffix('/#download')
        html2 = get_r(lnk)
        soup = BeautifulSoup(html2,features='html')
        _lnks = soup.find_all(name='a')
        for ket in _lnks:
            if str(ket['href']).endswith('.zip'):
                link2.append(ket['href'])
        """ 
        
        """
    return link2


def download_file(link):
    # make an HTTP request within a context manager
    with requests.get(link, stream=True) as r:
        
        # check header to get content length, in bytes
        total_length = int(r.headers.get("Content-Length"))
        print(f"Downloading {os.path.basename(r.url)}....")
        # implement progress bar via tqdm
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
        
            # save the output to a file
            with open(f"{os.path.basename(r.url)}", 'wb')as output:
                shutil.copyfileobj(raw, output)


if __name__ == '__main__':
    init_link = 'https://bootstrapmade.com/bootstrap-5-templates/'
    
    lst = delink(init_link)
    
    for _ in range(1):
        for lk in lst:
            download_file(lk)
    
        
        
        



