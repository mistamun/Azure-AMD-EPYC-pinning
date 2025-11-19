from .cpu_GA9V64H import GA9V64H
from .sku_base import SKU


class HB368v5(SKU):
    def __init__(self, cpuCores=None):
        super().__init__([
            GA9V64H(), GA9V64H(),
            GA9V64H(), GA9V64H(),
            ])
        if cpuCores is not None:
            self.subscribe(cpuCores)
