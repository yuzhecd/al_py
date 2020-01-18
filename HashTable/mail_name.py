from collections import Counter
def name_count(str_list):
    result = Counter()
    for s in str_list:
        number, domain = s.split(' ')
        number = int(number)
        subdomain = domain.split('.')
        for i in range(len(subdomain)):
            result['.'.join(subdomain[i:])] += number
    print(result)

if __name__ == '__main__':
    s = ['9001 scholar.google.com']
    p = ['900 google.com', '50 yahoo.com', '1 intel.mail.com', '5 wiki.org']
    name_count(p)
