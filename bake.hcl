group "default" {
    targets = [
        "API"
    ]
}

target "API" {
    context = "./API"
    dockerfile = "Dockerfile"
    tags =[
        "vuln-app:0.0"
    ]
}