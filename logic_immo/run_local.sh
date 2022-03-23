docker rm logic_immo
docker run -d \
-e START_PAGE=95 \
-e END_PAGE=100 \
-e GOOGLE_APPLICATION_CREDENTIALS=service_account.json \
--name logic_immo -d logic_immo