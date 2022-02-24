FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
#ENV GOOGLE_APPLICATION_CREDENTIALS path_service_account

# Copy local code to the container image.
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python src/main.py --startpage $START_PAGE --endpage $END_PAGE