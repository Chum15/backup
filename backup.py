import requests
import os
import json
from tqdm import tqdm



class VK():

    url_base ='https://api.vk.com/method'

    def __init__(self, user_id, version='5.131'):

        self.token = access_token
        self.id = user_id
        self.version = version 
        self.params = {'access_token': self.token, 'v': self.version}
 
    def get_photos(self):
        params = self.params
        params.update({'owner_id':self.id, 'album_id':'profile', 'extended':'extended=1', 'count':6})
        response = requests.get(f'{self.url_base}/photos.get', params=params)
        response = response.json()['response']['items']
      
        return response


    def file(self):
        photo_phile = self.get_photos()
       
        photos = {}
        info_file = [{}]

        if not os.path.isdir('photo_info'):
            os.mkdir('photo_info')

        for items in tqdm(photo_phile):
            
            data_file = items['date']
            name_file = items['likes']['count']
            size = items['sizes'][-1]['type']
            size_url = items['sizes'][-1]['url']
            info_file[0]['file_name'] = f'{name_file}.json'
            info_file[0]['size'] = size
            
            if os.path.exists('photo_info/'f'{name_file}.json'):
        
                with open('photo_info/'f'{name_file}.{data_file}.json', 'w', encoding='utf-8') as f:
                    json.dump(info_file, f)
                
                name_file =f'{name_file}.{data_file}'

            elif not os.path.exists('photo_info/'f'{name_file}.json'):
                with open('photo_info/'f'{name_file}.json', 'w', encoding='utf-8') as f:
                    json.dump(info_file, f)

                name_file = name_file

            photos[name_file] = size_url

        return photos
                          


class YD():
   
    url ='https://cloud-api.yandex.net/v1/disk/resources'
 
    def __init__(self, headers):

        self.headers = headers 
        self.params = {
            'path':'Photo_VK'
        }
      

    def folder(self):

        params = self.params
        response = requests.put(self.url,
                            headers=headers,
                            params=params)
        if response == 409:
              
            return response


    def load_photo(self):

        load_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        photos = vk.file()

        for photo, url in tqdm(photos.items()):
            url = requests.get(url).content
            response = requests.get(load_url,
                                    params={'path':f'Photo_VK/{photo}'},
                                    headers=headers)
            
            url_upload = response.json()['href']

            requests.put(url_upload, files={'file': url})



headers = {}
headers['Authorization'] = input('Введите ключ авторизации Яндекс Диска: Authorization:' )              
access_token = input('Введите актуальный токен VK:')
user_id = int(input('Введите user_id VK:'))


vk = VK(user_id)
yd = YD(headers)
yd.folder()
yd.load_photo()