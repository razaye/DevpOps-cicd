from app import app

def test_home():
   client = app.test_client()
   response = client.get('/')
   assert response.status_code == 200

def test_addition():
   client =app.test_client()
   response =client.get('/addition/2/3')
   assert response.data == b'10'
