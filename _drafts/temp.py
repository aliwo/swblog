import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', type=str)

args = parser.parse_args()

print(args.kimchi)
