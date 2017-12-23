#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import httplib2
import os
import datetime

from apiclient import errors
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python.json')

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

def upload(self, file_name):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    time = datetime.now().strftime("%Y/%m/%d %H-%M-%S")
    file_name = time + fielname
    file_metadata = {'name': file_name}
    file_path = 'file/'+ file_name
    media = MediaFileUpload(file_path,
                             mimetype='image/pdf')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    request = farm.animals().insert(media_body=media, body={'name': 'Pig'})
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print ("Uploaded %d%%." % int(status.progress() * 100))
    print ("Upload Complete!")
    print ('File ID: %s' % file.get('id'))