import bottle

@bottle.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    bottle.run()