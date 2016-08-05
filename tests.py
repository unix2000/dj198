def application(env,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return [b"hello django--uwsgi"]

# uwsgi --http :9090 --wsgi-file tests.py
#//加载不到静态文件css js
# python35 manage.py collectstatic
# uwsgi --http :8000 --module dj198.wsgi 