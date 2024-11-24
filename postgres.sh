docker run -p 5432:5432 --name test-postgres \
-e POSTGRES_PASSWORD=postgres \
-e TZ=Asia/Seoul \
-v /Users/dwlee/Documents/quant_api/temp:/var/lib/postgresql/data \
-d postgres:latest
