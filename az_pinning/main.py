import argparse
from .sku_v3 import HB120v3
from .sku_v4 import HB176v4, HX
from .sku_v5 import HB368v5


SKU_MAP = {
    'HB120v3': HB120v3,
    'HB176v4': HB176v4,
    'HX': HX,
    'HB368v5': HB368v5,
}


def main():
    parser = argparse.ArgumentParser(
        description='Returns mpirun string for proper pinning'
    )

    parser.add_argument(
        '--sku',
        choices=list(SKU_MAP.keys()),
        help='SKU Name',
    )

    parser.add_argument(
        '--cpus',
        type=int,
        help='Number of CPUs for which pinning is desired',
    )

    parser.add_argument(
        '--mpi',
        choices=[
            'OMPI',
            'IMPI',
            'PMPI',
        ],
        help='MPI version',
    )

    args = parser.parse_args()

    print(SKU_MAP[args.sku](args.cpus).getMPIString(args.mpi))


if __name__ == "__main__":
    main()
