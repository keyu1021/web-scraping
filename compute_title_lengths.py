import json
import os,sys
import argparse

def main():
    with open(sys.argv[1],'r') as sample:
        lines = sample.readlines()
        total_len = 0
        for line in lines:
            content = json.loads(line)
            title = content['data']['title']
            total_len += len(title)

        avg_len = total_len / 1000
        print(avg_len)

    return avg_len

if __name__ == "__main__":
    main()