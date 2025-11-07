FROM python:3.12-slim
#sørger for at den virtuelle mashine har python (den bruger Linux som operativsystem)
#Dockerfile bruges til at lave et docker image som et blueprint. Den kan vi bruge til at lave en docker container senere

WORKDIR /app
#kopieer mine filer over til arbejdsmappen på den virtuelle maskine

# Installer nødvendige systempakker
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0"]



