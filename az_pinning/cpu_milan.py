from .ccd_base import CCD
from .cpu_base import CPU


class Milan7V73X(CPU):
    def __init__(self):
        """
            2 nodes per socket
            4 CCD per node
            32 core each node
            8 core per CCD
            2 reserved cores in specific CCDs for a total of 8 reserved cores
        """
        super().__init__([
            CCD(8), CCD(8), CCD(8), CCD(6),  # Numa node 0
            CCD(8), CCD(8), CCD(8), CCD(6),  # Numa node 1
        ])
