from server import app, common

if __name__ == '__main__':
    common.serve(host=app.config['HOST'], port=app.config['PORT'])
