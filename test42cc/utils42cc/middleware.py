from utils42cc.models import HttpRequestEntry


class HttpRequestStore(object):
    def process_request(self, request):
        """ Save each http request to db
        """
        path = request.path[:256]  # if we reciev very very long url
        method = request.method
        remote_addr = request.META['REMOTE_ADDR']
        entry = HttpRequestEntry(path=path, method=method,
            remote_addr=remote_addr)
        entry.save()
