FROM Kuma-Stream/aeon:latest
WORKDIR /usr/src/app
COPY . .
CMD ["bash", "start.sh"]
