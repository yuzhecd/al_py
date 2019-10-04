class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '[' + self.start + ", " + self.end + ']'

    def __repr__(self):
        return "[%s, %s]" % (self.start, self.end)

def merge_array(intervals):
    intervals.sort(key=lambda x: x.start)

    merge = []
    for interval in intervals:
        if not merge or merge[-1].end < interval.start:
            merge.append(interval)

        else:
            merge[-1].end = max(merge[-1].end, interval.end)

    return merge

if __name__ == '__main__':
    a = Interval(1, 3)
    b = Interval(2, 6)
    c = Interval(8, 10)
    d = Interval(15, 18)
    alist = [b, a, d, c]
    result = merge_array(alist)
    print(result, type(result[0]))
