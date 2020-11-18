import api

def test_webapp_index():
    assert api.index() == 'Hi!'
