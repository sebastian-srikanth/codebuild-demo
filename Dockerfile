# set base image (host OS)
FROM python:3.8

LABEL maintainer="Sebastian Srikanth Kumar <sebastin.kumar@factspan.com>"

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

COPY scripts .
COPY main.py .

ENTRYPOINT ["python", "/workspace/main.py", "sebastian"]
