from abc import ABCMeta, abstractmethod

"""
Contract for the SSH strategies, it specifies the methods that must be implemented, as well as the parameters that they receive.
"""
class SSHStrategy:
    __metaclass__ = ABCMeta
    # COnstructor, it receives a host options object.
    @abstractmethod
    def __init__(
        self, 
        options
    ): raise NotImplementedError
    # Connection entry point, any required methods by strategy musty be inovked here
    @abstractmethod
    def connect(self): raise NotImplementedError