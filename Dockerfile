FROM python:3.7.2
WORKDIR /jdx
RUN apt-get update
# Required for postgres
RUN apt-get install -y libpq-dev python-dev
# Required for textract
RUN apt-get install -y curl python-dev libxml2-dev libxslt1-dev \
antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 \
libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev zlib1g-dev
# Required for textract
RUN curl https://raw.githubusercontent.com/OriHoch/textract/fake-pocketsphinx-for-swig-dependency/provision/fake-pocketsphinx.sh | bash -
RUN pip install pipenv
ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pipenv install --system
ADD jdxapi jdxapi
ADD run.sh run.sh
RUN chmod a+x run.sh
ADD .env-docker-development .env-docker-development
ENTRYPOINT [ "/jdx/run.sh" ]
