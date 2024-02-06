FROM minio/minio:latest


# Set the access and secret keys for Minio (replace with your own keys)
ENV MINIO_ROOT_USER=test
ENV MINIO_ROOT_PASSWORD=test_pwd
ENV MINIO_ADDRESS=:9000
ENV MINIO_CONSOLE_ADDRESS=:9001

# Expose the port on which Minio will run
EXPOSE 9000
EXPOSE 9001

VOLUME ["/data"]

CMD ["minio","server", "/data", "--console-address", ":9001", "--address" , ":9000"]
