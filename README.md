# Kubernetes examples

Tutorial of kubernetes basics with examples.

## Application
There is a simple Sanic (async python framework) based web application for the demo purposes.
It exposes 8000 port and serves 2 endpoints:

* `/` – return some information about the current request
* `/health/` – return 200 OK

This application docker image is public accessible [here](https://hub.docker.com/r/kaduev13/echoapp/).