from hello import app 
import time
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World!'
    assert response.status_code == 200
    print("1")
    print("2")
    print("4")

