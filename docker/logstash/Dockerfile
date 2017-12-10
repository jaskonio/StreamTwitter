FROM docker.elastic.co/logstash/logstash-oss:6.0.1

RUN logstash-plugin install logstash-output-mongodb

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

ADD conf/ /usr/share/logstash/pipeline/
