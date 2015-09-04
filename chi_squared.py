from scipy import stats
import collections
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print "The chi value is", stats.chisquare(freq.values())[0], " and the p value is", stats.chisquare(freq.values())[1],"."