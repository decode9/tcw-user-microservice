from .grpcAPI import Beetle
from .utils import Database
from .components import UserController


app = Beetle()
dbClient = Database()
dbClient.runClient()

app.services = [
    UserController(),
]
