FROM python:3.8
# https://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/
#FROM hypriot/rpi-python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 80/tcp
#EXPOSE 80/udp
#EXPOSE 443/tcp
#EXPOSE 443/udp
COPY . .
CMD ["python", "main.py"]