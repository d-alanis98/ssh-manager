import os
from dotenv import load_dotenv
# SSH 
from SSHManager import SSHManager
from NemikoStrategy import NemikoStrategy

load_dotenv()


DEVICE_TYPE = os.getenv('DEVICE_TYPE')
HOST_ADDRESS = os.getenv('HOST_ADDRESS')
HOST_USERNAME = os.getenv('HOST_USERNAME')
HOST_PASSWORD = os.getenv('HOST_PASSWORD')
HOST_SSH_PORT = os.getenv('HOST_SSH_PORT')

test_host = { 
    'device_type': DEVICE_TYPE, 
    'host': HOST_ADDRESS, 
    'username': HOST_USERNAME, 
    'password': HOST_PASSWORD, 
    'port': HOST_SSH_PORT, 
}


def main():
    ssh_manager = SSHManager(
        NemikoStrategy(test_host)
    )
    # We start the connection and send commands
    ssh_manager.connect()
    ssh_manager.exec_command('ip -c -h a')
    # We print the buffer
    ssh_manager.print_buffer()
    # We clear the buffer
    ssh_manager.clear_buffer()
    # We execute another command
    ssh_manager.exec_command('python3 --version')
    ssh_manager.print_buffer()

if __name__ == '__main__':
    main()



