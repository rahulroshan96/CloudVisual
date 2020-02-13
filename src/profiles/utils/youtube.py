import os
from googleapiclient.discovery import build

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret2.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl', 'https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    api_key = str(os.environ['GOOGLEAPI'])
    return build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)


def get_videos_by_query(query):
    service = get_authenticated_service()
    req = service.search().list(q=query, part='snippet', type='video', maxResults=50)
    result = req.execute()
    items = result['items']
    results = []
    for i in items:
        results.append('https://www.youtube.com/watch?v=%s' % i['id']['videoId'])
    return results


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()
    print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
          (results['items'][0]['id'],
           results['items'][0]['snippet']['title'],
           results['items'][0]['statistics']['viewCount']))


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    # channels_list_by_username(service,
    #     part='snippet,contentDetails,statistics',
    #     forUsername='GoogleDevelopers')
    get_videos_by_query(service, 'avengers')
