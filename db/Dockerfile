FROM postgres

ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=db


COPY ./data /var/lib/postgresql/data

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "pg_isready", "-U", "user", "-d", "db" ]