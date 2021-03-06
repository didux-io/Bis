FROM alpine:3.8

# Setup python3 (add numpy here too, else opencv install issues)
RUN apk add --no-cache python3 python3-dev gcc musl-dev postgresql-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install other requirements
RUN pip3 install --upgrade pip

# Copy python requirements file and install libs
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -U -r /tmp/requirements.txt

# Add app
RUN mkdir /app
COPY . /app
WORKDIR /app

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "server.py" ]