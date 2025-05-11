group "default" {
    targets = [
        "API",
        # "db",
        "front",
        "keycloak"
    ]
    labels = {
        "org.opencontainers.image.source" = "https://github.com/gchalard/labs-vulnerable-app"
    }
}
target "API" {
    inherits = ["default"]
    context = "./API"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-api:latest"
    ]
}

target "db" {
    inherits = ["default"]
    context = "./db"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-db:latest"
    ]
}

target "front" {
    inherits = ["default"]
    context = "./frontend"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-front:latest"
    ]
}

target "keycloak" {
    inherits = ["default"]
    context = "./idp"
    dockerfile = "Dockerfile"
    tags =[
        "ghcr.io/gchalard/vulnerable-app-kc:latest"
    ]
}