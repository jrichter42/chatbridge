FROM python:3.8
WORKDIR /app
COPY docker_requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 80/tcp
#EXPOSE 80/udp
#EXPOSE 443/tcp
#EXPOSE 443/udp
COPY . .
CMD ["python", "main.py"]