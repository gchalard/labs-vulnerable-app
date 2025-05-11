group "default" {
    targets = [
        "API",
        # "db",
        "front",
        "keycloak"
    ]
}

group "common" {
    labels = {
        "org.opencontainers.image.source" = "https://github.com/gchalard/labs-vulnerable-app"
    }
    targets = [
        "API",
        # "db",
        "front",
        "keycloak"
    ]
}

target "API" {
    inherits = ["common"]
    context = "./API"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-api:latest"
    ]
}

target "db" {
    inherits = ["common"]
    context = "./db"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-db:latest"
    ]
}

target "front" {
    inherits = ["common"]
    context = "./frontend"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-front:latest"
    ]
}

target "keycloak" {
    inherits = ["common"]
    context = "./idp"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-kc:latest"
    ]
}