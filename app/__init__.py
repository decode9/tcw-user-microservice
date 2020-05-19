from .grpcAPI import Beetle
from .components import UserController


app = Beetle()

app.services = [
    UserController(),
]
