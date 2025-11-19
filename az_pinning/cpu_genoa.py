from .ccd_base import CCD
from .cpu_base import CPU


class GenoaX9V33X(CPU):
    def __init__(self):
        """
            2 nodes per socket
            6 CCD per node
            48 core each node
            8 core per CCD
            2 reserved cores in specific CCDs for a total of 16 reserved cores
        """
        super().__init__([
            CCD(8), CCD(8), CCD(8),  # Numa node 0
            CCD(8), CCD(6), CCD(6),
            CCD(8), CCD(8), CCD(8),  # Numa node 1
            CCD(8), CCD(6), CCD(6),
        ])
