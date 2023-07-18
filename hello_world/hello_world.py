from omni.services.core import main


def hello_world():
    return "Hello World!"


main.registry_endpoint("get", "/hello_world", hello_world)
