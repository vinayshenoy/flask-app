import argparse

def add(args):
    print(args.num1+args.num2)

parse=argparse.ArgumentParser()
parse.add_argument("num1",type=int)
parse.add_argument("num2",type=int)
args=parse.parse_args()
add(args)