import httplib2

GOQR_API = 'http://api.qrserver.com/v1/create-qr-code/?data=%s&size=250x250'

def create_qrcode(url):
    client = httplib2.Http()
    client.request(GOQR_API % url)
