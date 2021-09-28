# STrategy contract
from SSHStrategy import SSHStrategy

"""
Class to establish an SSH connection with a device. It applies the strategy pattern, to support various implementations or libraries. 
It also allows to keep the output of the entered commands in a buffer, which can also be cleared on demand.
"""
class SSHManager:
    def __init__(
        self,
        strategy: SSHStrategy
    ):
        self.buffer = ''
        self.strategy = strategy

    """
    Method to start the connection.
    """
    def connect(self):
        self.net_connect = self.strategy.connect()

    """
    Method to execute a command. It writes the result to the buffer.
    @param command: str 
        The command to execute
    """
    def exec_command(self, command: str):
        self.buffer += self.net_connect.send_command(command)

    """
    Method to print the output buffer
    """
    def print_buffer(self) -> str:
        print(self.buffer)

    """
    Method to clear the output buffer
    """
    def clear_buffer(self):
        self.buffer = ''
