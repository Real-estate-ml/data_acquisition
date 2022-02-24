docker rm logic_immo
docker rmi logic_immo
docker build -t logic_immo .
docker tag logic_immo eu.gcr.io/projet-immo-esme/logic_immo
docker push eu.gcr.io/projet-immo-esme/logic_immo