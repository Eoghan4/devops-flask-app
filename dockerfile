FROM python:3.15.0a1-trixie
RUN apt-get install -y git
RUN git clone https://github.com/Eoghan4/devops-flask-app/
WORKDIR /devops-flask-app
RUN chmod 777 my_script.sh
EXPOSE 5000
CMD ["./my_script.sh"]
