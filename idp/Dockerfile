FROM quay.io/keycloak/keycloak:latest

ENV KEYCLOAK_ADMIN=admin
ENV KEYCLOAK_ADMIN_PASSWORD=admin
ENV KC_DB=postgres
ENV KC_DB_URL=jdbc:postgresql://postgres:5432/db
ENV KC_DB_USERNAME=user
ENV KC_DB_PASSWORD=password
ENV KC_HTTP_ENABLED=true
ENV KC_HOSTNAME_STRICT=false
ENV KEYCLOAK_IMPORT=/opt/keycloak/data/import/realm.json

COPY realm.json /opt/keycloak/data/import/realm.json