from .ccd_base import CCD
from .cpu_base import CPU


class GA9V64H(CPU):
    def __init__(self):
        """
            4 nodes per socket
            3 CCD per node
            24 core each node
            8 core per CCD
            1 reserved core in specific CCDs for a total of 16 reserved cores
        """
        super().__init__([
            CCD(8), CCD(8), CCD(7),  # Numa node 0
            CCD(8), CCD(8), CCD(7),  # Numa node 1
            CCD(8), CCD(8), CCD(7),  # Numa node 2
            CCD(8), CCD(8), CCD(7),  # Numa node 3
        ])
