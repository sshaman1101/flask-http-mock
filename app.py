from flask import Flask, Response, request
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=('GET', 'POST'))
@app.route('/<path:path>', methods=('GET', 'POST'))
def catch_all(path):
    print('Path: %s' % path)
    if request.method == 'POST':
        print('BODY: %s' % request.data)
        content_type = request.headers.get('Content-Type')

        if content_type == 'application/xml':
            return Response('<status>OK</status>', content_type='application/xml')
        elif content_type == 'application/json':
            return Response('{"status": "OK"}', content_type='application/json')

    return Response('OK', content_type='text/plain')


if __name__ == '__main__':
    app.run(port=8099)
