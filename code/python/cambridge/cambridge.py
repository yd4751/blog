import os
import requests
from bs4 import BeautifulSoup
#
default_headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
#
class CWord:
    '''
    word:sunny
    desc:阳光明媚的，阳光充足的
    type:adjective
    ogg:[uk url,us url]
    areas:[uk,us]
    pronus:[/ˈsʌn.i/,/ˈsʌn.i/]
    example:
        We're having the party in the garden, so I'm praying it'll be sunny.
        我们要在花园里举行聚会，所以我正祈祷那天会阳光明媚。
    '''
    def __init__(self,word):
        self.word = word
        self.desc = ''
        self.type = ''
        self.examples = {}
        self.areas = [] #uk/us
        self.pronus = []
        self.audio_urls = []
    #
    def AddExample(self,example,translation):
        self.examples[example] = translation
    #
    def AddAudio(self,area,pronunciation,url):
        self.areas.append(area)
        self.pronus.append(pronunciation)
        self.audio_urls.append(url)
    #
    def Save(self):
        try:
            save_str = '{0}|{1}|{2}'.format(self.word,self.type,self.desc)

            for i in range(len(self.areas)):
                word = self.word
                area = self.areas[i]
                url = self.audio_urls[i]
                #
                save_str += '|{0}|{1}'.format(area,self.pronus[i])
                #
                response = requests.get(url,headers=default_headers)
                with open('ogg/{0}_{1}.ogg'.format(area,word), 'wb') as f:
                    f.write(response.content)
            #
            for k,v in self.examples.items():
                save_str += '|{0}|{1}'.format(k,v)
            #
            with open('word.txt', 'a', encoding='utf-8') as f:
                f.write(save_str)
                f.write('\n')

        except Exception as e:
            print(e)
#
class CDictionary:
    def __init__(self,domain):
        self.domain = domain
        self.words = []
        #初始化目录
        if not os.path.exists('ogg'):
            os.mkdir('ogg')
    #
    def Serach(self,word:list):
        for w in word:
            ret = self.search(w)
            if ret is not None:
                self.words.append(ret)
    #
    def Save(self):
        for w in self.words:
            w.Save()
    #
    def search(self,w)->CWord:
        url = '{0}/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/{1}'.format(self.domain,w)
        word = self.handle_requet(url)
        return word

    def handle_requet(self,url)->CWord:
        #
        try:
            response = requests.get(url,headers=default_headers)
            if response.status_code != 200:
                return None
            #
            soup = BeautifulSoup(response.text, 'lxml')
            word =self.handle_content1(soup.select_one('div.pos-header.dpos-h'))
            self.handle_content2(soup.select_one('div.def-block.ddef_block'),word)
            return word
        except Exception as e:
            print(e)
            return None
    
    #注音+音频
    def handle_content1(self,soup)->CWord:
        if soup is None:
            return None
        #
        title = soup.select_one('span.hw.dhw')
        #print(title.text)
        word  = CWord(title.text)
        #adj,n,vi
        type = soup.select_one('span.pos.dpos')
        word.type = type.text
        #uk
        uk_audio =soup.select_one('span.uk.dpron-i source[type="audio/ogg"]')
        uk_audio = self.domain + uk_audio.attrs['src']
        uk_pronuc = soup.select_one('span.uk.dpron-i > span.pron.dpron > span')
        word.AddAudio('uk','/{}/'.format(uk_pronuc.text),uk_audio)
        #us
        us_audio =soup.select_one('span.us.dpron-i source[type="audio/ogg"]')
        us_audio = self.domain + us_audio.attrs['src']
        us_pronuc = soup.select_one('span.us.dpron-i > span.pron.dpron > span')
        word.AddAudio('us','/{}/'.format(us_pronuc.text),us_audio)
        return word

    #例句
    def handle_content2(self,soup,word:CWord):
        if soup is None or word is None:
            return 
        #
        result = soup.select('span.trans.dtrans.dtrans-se.break-cj span.dtrans')
        description = ''
        for d in result:
            description += d.text + ','
        word.desc = description
        #
        result = soup.select_one('div.examp.dexamp')
        eg = result.select_one('span.eg.deg')
        trans = result.select_one('span.trans.dtrans')
        word.AddExample(eg.text,trans.text)