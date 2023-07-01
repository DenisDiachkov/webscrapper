FROM ubuntu:20.04
RUN apt-get -y update 
RUN apt-get install -y xvfb 
RUN apt-get install -y wget 
RUN apt-get install -y curl 
RUN apt-get install -y unzip 
RUN apt-get install -y libxi6 
RUN apt-get install -y libgconf-2-4 
RUN apt-get install -y libnss3 
RUN apt-get install -y gcc make 
RUN apt-get install gnupg -yq

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update && apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


RUN apt install python3-pip -y
RUN pip3 install selenium==4.9.1 bs4==0.0.1 
RUN pip3 install pyvirtualdisplay==3.0
RUN pip3 install flask==2.3.2


RUN rm -rf /var/lib/apt/lists/* 
RUN rm -rf /var/lib/apt/lists/*s

ENV PYTHONUNBUFFERED=1
