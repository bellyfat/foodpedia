FROM google/python

RUN apt-get update && apt-get install -y \
  libffi-dev\
  libxml2-dev\
  libxslt1-dev\
  python-dev

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/local/src/foodpedia-parser-v2/
RUN mkdir -p /upload
RUN touch /upload/dump.ttl
VOLUME /upload

ADD . /usr/local/src/foodpedia-parser-v2/
ENTRYPOINT [ "sh", "./start.sh" ]
CMD [ "Foodstuffs" ]
#CMD [ "Frozen-meat-natural-convenience-foods" ]
