gcloud compute instances create-with-container logic-immo-acq \
--zone europe-west1-b \
--container-image eu.gcr.io/projet-immo-esme/logic_immo:latest \
--container-env=\
START_PAGE=1,\
END_PAGE=2,\
GOOGLE_APPLICATION_CREDENTIALS=service_account.json
#--container-restart-policy=on-failure