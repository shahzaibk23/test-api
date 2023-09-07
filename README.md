# Test API

API made in Flask for testing purpose.

### Install Flask
```bash
pip install flask
```

### Run the App
```bash
python app.py
```
### API Calll using Postman or Curl

Simply send a POST request to `http://127.0.0.1:5000/api/response`

```bash
curl -X POST http://127.0.0.1:5000/api/response

# output
#{
#  "status": "failed"
#}

curl -X POST http://127.0.0.1:5000/api/response

# output
#{
#  "status": "success"
#}
```