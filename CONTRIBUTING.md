# CONTRIBUTING 

# RUNNING THE FILE LOCALLY 

# VERSION ONE LOCALLY 

docker build -t rest-api-flask-python .

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" rest-api-flask-python

# VERSION TWO LOCALLY 

docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
