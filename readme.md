### app 실행절차

- 리포지토리 최상위 디렉터리 위치로 이동 cd /fastapi
- export MONGODB_SAMPLE_URL="mongodb://easywaldo:rlekflqk1Py@cluster0-shard-00-00.figii.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-wyadnv-shard-0&authSource=admin&retryWrites=true&w=majority"
- uvicorn main:app --reload --host=127.0.0.1 --port=9000

