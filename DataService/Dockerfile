FROM python:slim-trixie
#sørger for at den virtuelle mashine har python (den bruger Linux som operativsystem)
#Dockerfile bruges til at lave et docker image som et blueprint. Den kan vi bruge til at lave en docker container senere

WORKDIR /app
#kopieer mine filer over til arbejdsmappen på den virtuelle maskine
#sørger lige for at requirements.txt er i denne mappe 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
#kopiere ind i app-mappen på linux computeren 

CMD ["python", "app.py"] 

#terminal for at bygge image: docker build -t dataservice .
    #det virker kun hvis du har åbnet docker appen
#terminal for at køre container: docker run -p 5001:5000 dataservice
#-p 5001:5000 betyder at den skal mappe port 5001 på min computer til port 5000 på den virtuelle maskine

