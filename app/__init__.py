from .grpcAPI import Beetle
from .utils import Database

app = Beetle()
dbClient = Database()
dbClient.runClient()