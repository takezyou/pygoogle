#!/usr/bin/env python
#coding: utf-8
from __future__ import print_function
import httplib2
import os

from apiclient import errors
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'pygoogle'

class Uploader:
    def __init__(self):
        self.credentials = self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=self.http)

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def upload(self):
        folder_id = '1EU4ZzMywK9sIUjvs4GQQej12x5Ph-8Cn'
        media_body = MediaFileUpload('test.jpg', mimetype='image/jpeg', resumable=True)
        file_name = 'test.jpg'
        body = {
                'name': os.path.split(file_name)[-1],
                'mimeType': 'image/jpeg',
                'parents': [folder_id],
            }
        self.service.files().create(body=body, media_body=media_body).execute
        print('Upload sucssesful:' + file_name)

if __name__ == '__main__':
    uploader = Uploader()
    uploader.upload()   
