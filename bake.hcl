group "default" {
    targets = [
        "API",
        # "db",
        "front"
    ]
}

target "API" {
    context = "./API"
    dockerfile = "Dockerfile"
    tags =[
        "vuln-app:0.0",
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