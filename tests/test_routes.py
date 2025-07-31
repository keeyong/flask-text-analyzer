import json
from app import create_app

def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()

def test_health():
    rv = client().get('/health')
    assert rv.status_code == 200
    assert rv.get_json() == {'status': 'ok'}

def test_analyze_basic():
    payload = {'text': "Hello, hello! This is a test.", 'top': 2}
    rv = client().post('/analyze', data=json.dumps(payload), content_type='application/json')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['wordCount'] == 7
    assert len(data['topWords']) == 2

def test_analyze_validation():
    rv = client().post('/analyze', json={'text': 123})
    assert rv.status_code == 400
    rv = client().post('/analyze', json={'text': 'ok', 'top': -1})
    assert rv.status_code == 400
