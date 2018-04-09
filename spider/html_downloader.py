import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is not None:

            try:

                request = urllib.request.urlopen(url, timeout=10)

                if request.getcode() == 200:

                    return request.read()

                else:

                    return None

            except Exception as e:

                print(str(e))

        else:

            return None