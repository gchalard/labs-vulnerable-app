group "default" {
    targets = [
        "API",
        "db",
        "front",
        "keycloak"
    ]
}

target "API" {
    context = "./API"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-api:latest"
    ]
}

target "db" {
    context = "./db"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-db:latest"
    ]
}

target "front" {
    context = "./frontend"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-front:latest"
    ]
}

target "keycloak" {
    context = "./idp"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-kc:latest"
    ]
}