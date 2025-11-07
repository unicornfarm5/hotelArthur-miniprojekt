FROM python:3.12-slim
#sørger for at den virtuelle mashine har python (den bruger Linux som operativsystem)
#Dockerfile bruges til at lave et docker image som et blueprint. Den kan vi bruge til at lave en docker container senere

WORKDIR /app
#kopieer mine filer over til arbejdsmappen på den virtuelle maskine
#sørger lige for at requirements.txt er i denne mappe 

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
#kopiere ind i app-mappen på linux computeren 

CMD ["python", "main.py"] 
