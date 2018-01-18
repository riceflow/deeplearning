import sys
import codecs
import pandas as pd
import matplotlib.pyplot as plt

shops = pd.read_csv('shops.txt', delimiter='\t')
reviews = pd.read_csv('reviews.txt', delimiter='\t')

print(reviews)
