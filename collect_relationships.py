import json
import os,sys
import os.path as osp
import argparse
import bs4
import wget
import hashlib
import re

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--f_input')
    parser.add_argument('-o', '--f_output')
    args = parser.parse_args()
    
    with open(args.f_input, 'r') as input:
        f = json.load(input)
    
    cache_dir = f['cache_dir']
    target_pll = f['target_people']
    head, tail = os.path.split(cache_dir)
    file_path = osp.abspath(__file__)
    parent_dir = os.path.abspath('..')
    cache_abs_dir = parent_dir + '/' + cache_dir
    #print(cache_abs_dir)
    #print(osp.exists(cache_abs_dir))

    if not osp.exists(cache_abs_dir):
        if not osp.exists(parent_dir + '/' + head):
            os.mkdir(parent_dir + '/' + head)
            os.mkdir(parent_dir + '/' + head + '/' + tail)
            print('make data + wdw cache')
        else:
            os.mkdir(cache_abs_dir)
            print('make wdw cache')

    dict = {}
    for pll in target_pll:
        exs = []
        dict[pll] = []
        url = 'https://www.whosdatedwho.com/dating/' + pll
        hash = hashlib.sha1(url.encode("UTF-8")).hexdigest()
        if osp.exists(cache_abs_dir + '/' + hash):
            soup = bs4.BeautifulSoup(open(cache_abs_dir + '/' + hash, 'r'), 'html.parser')
        else:
            os.system('wget -O' + cache_abs_dir + '/' + hash + ' ' + url)
            print(cache_abs_dir + '/' + hash + ' ' + url)
            soup = bs4.BeautifulSoup(open(cache_abs_dir + '/' + hash, 'r'), 'html.parser')
        try:
            relationships = soup.find_all('a', href = re.compile('^/dating/.*$'))
            num_relationships = soup.find('a', href="#ff-dating-history")
            num_relationships = int(num_relationships.find('div', 'fact').string)
        except:
            print('This person do Not exist')
            continue

        for ex in relationships:
            name = ex.text
            name = name.replace('.', '')
            name = name.lower()
            name = name.replace(' ', '-')
            if name != pll and name not in exs and len(exs) != num_relationships:
                exs.append(name)

            dict[pll] = exs

        with open(args.f_output, 'w') as o:
            o.write(json.dumps(dict, indent = 4))

if __name__ == "__main__":
    main()