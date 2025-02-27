# base image
FROM python:3.13.1-alpine3.21

# working directory
WORKDIR /app

# content copy
COPY . ./

# install packages
RUN pip install -r requirements.txt

# environment setting

# debug

# run container
CMD ["fastapi", "run", "backend/main.py"]

