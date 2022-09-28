# BOJ 17141 연구소
# 220926

import collections
import copy
from pprint import pprint

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]