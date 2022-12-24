from gevent import socket
from gevent.pool import Pool
from gevent.server import StreamServer

from collections import namedtuple
from io import BytesIO
from socket import error as socket_error

# Error handling
class CommandError(Exception): pass
class Disconnect(Exception): pass

Error = namedtuple('Error', ('message',))

