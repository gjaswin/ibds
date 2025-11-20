from mrjob.job import MRJob
import csv

class RatingsBreakdown(MRJob):

    def mapper(self, _, line):
        if line.startswith("userId"): # skip header
            return
        # parse CSV
        userId, movieId, rating, timestamp = line.split(',')
        yield rating, 1

    def reducer(self, rating, counts):
        yield rating, sum(counts)

if __name__ == '__main__':
    RatingsBreakdown.run()
