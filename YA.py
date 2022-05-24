import requests
from pprint import pprint


class YaUploader:
    url = 'https://cloud-api.yandex.net:443' 

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }    

    def get_upload_link(self, path):
        url = f'{self.url}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href') 
        
    def upload(self, file_path, file_name):
        upload_link = self.get_upload_link(file_path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Ваш файл загружен!')
        
if __name__ == '__main__':
    token = ''
    print('Пример пути до файла: C:\\\\Users\\\\LocAdmin\\\\Pictures\\\\cosmos.jpg')
    my_file = f'{input("Введите путь до файла, согласно примеру: ")}'
    path_name = my_file.split('\\')[-1]
    uploader = YaUploader(token)
    uploader.upload(path_name, my_file)
    
      
