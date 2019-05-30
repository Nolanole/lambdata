FROM debian
  
# Comments are like this
# So logging works w/Docker
ENV PYTHONUNBUFFERED=1

# You can RUN things, mostly to install dependencies
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-Nolanole && \
  python3 -c "import lambdata_Nolanole"