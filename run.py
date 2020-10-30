import argparse
import sys
import json

from src.data.etl import complete

def main():

    with open('config/params.json') as fh:
        data_cfg = json.load(fh)

    if targets:
        assert len(targets) >= 2, "Make sure to provide a feature and edge filepath! Features filepath first followed by edge filepath."

        features_fp = targets[0]
        edges_fp = targets[1]

        data_cfg['fp_features'] = features_fp
        data_cfg['fp_edges'] = edges_fp

    complete(**data_cfg)


if __name__ == '__main__':
    targets = sys.argv[1:]
    main()


# python run.py data/raw/twitch/ENGB/musae_ENGB_features.json data/raw/twitch/ENGB/musae_ENGB_edges.csv

#make sure to change to snap instead of cora
