#!/usr/bin/env python3

""" Calls the cythonized program """

#pylint: disable=E0401
from poor_perf_v15 import analyze


if __name__ == "__main__":
    analyze("./data/dataset.csv")
