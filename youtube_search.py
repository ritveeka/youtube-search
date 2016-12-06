#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from sys import argv


#search is the search term
def youtube_search(search):
    print("showing search results for " + search)
    url_post = 'https://www.youtube.com/results'

    #url to get the links of search results
    url_get = 'https://www.youtube.com'

    #input for post request
    input = {'search_query':search}

    source = requests.post(url_post,input)
    html = source.text
    soup = BeautifulSoup(html,"lxml")

    #youtube stores links in 'ol' with class 'item-section'
    part = soup.find('ol',attrs = {'class':'item-section'})
    list = part.descendants

    #number of search results
    results_cnt = 0
    for item in list:
        if (item.name == 'a'):
            try:
                #some items are none so don't have 'class' key
                if(item['class'] == ['yt-uix-sessionlink', 'yt-uix-tile-link', 'yt-ui-ellipsis', 'yt-ui-ellipsis-2', 'spf-link', '']):
                    results_cnt += 1
                    print(str(results_cnt) + ")." + item.text + " - " + url_get + item.get('href') + "\n")
            except KeyError:
                print('key error')
    print("total results: " + str(results_cnt))

def main():
    if len(argv) < 2:
        print('please enter something to search ')
        search=input('> ')
        while len(search) == 0:
            print('please enter something to search ')
            search = input('> ')
    else:
        search = argv[1]

    youtube_search(search)

if __name__ == '__main__':
    main()