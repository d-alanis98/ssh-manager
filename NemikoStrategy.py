from netmiko import ConnectHandler
from SSHStrategy import SSHStrategy

"""
SSH strategy, implementing nemiko library for multi-vendor support.
It receives an options list with the following shape:

host = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'user',
    'password': 'password',
    'port' : 22, # optional, defaults to 22
    'secret': 'cisco', # optional, defaults to ''
}
"""
class NemikoStrategy(SSHStrategy):
    def __init__(self, options):
        self.options = options
    
    """
    Connect method specific for the nemiko library.
    """
    def connect(self):
        return ConnectHandler(
            **self.options
        )