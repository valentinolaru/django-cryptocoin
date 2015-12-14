import bitcoinrpc

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse


def bitcoinrpc_connect(service_url):
    service_url = service_url
    url = urlparse.urlparse(service_url)
    hostname = url.hostname
    if url.port is None:
        port = 80
    else:
        port = url.port
    (user, password) = (url.username, url.password)
    try:
        user = user.encode('utf8')
    except AttributeError:
        pass
    try:
        passwd = password.encode('utf8')
    except AttributeError:
        pass

    use_https = False
    if url.scheme == 'https':
        use_https = True

    return bitcoinrpc.connect_to_remote(user, password, hostname, port, use_https)
