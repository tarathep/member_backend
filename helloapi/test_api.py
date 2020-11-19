import helloapi.api

def test_webapp_index():
    assert helloapi.index() == 'Hi!'

