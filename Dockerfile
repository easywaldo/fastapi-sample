 # 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]

ENV MONGODB_SAMPLE_URL mongodb://easywaldo:rlekflqk1Py@cluster0-shard-00-00.figii.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-wyadnv-shard-0&authSource=admin&retryWrites=true&w=majority