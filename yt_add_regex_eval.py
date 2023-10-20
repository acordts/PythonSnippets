import re
URLS_FILE = "./yt_add_urls.txt"
MISS_URLS = "./missed_urls.txt"
URLS_REGEX = re.compile(r'r+\d+[\w\-\.]+\.googlevideo(\.com)?')

def get_urls():
    with open(URLS_FILE, 'r') as stream:
        return stream.readlines()

def get_matches(urls):
    matches = []
    miss_matches = []
    for url in urls: 
        if URLS_REGEX.match(url):
            matches.append(url)
        else:
            miss_matches.append(url)

    write_miss_matches(miss_matches)
    return matches

def write_miss_matches(miss_matches):
    with open(MISS_URLS, 'w') as stream:
        stream.writelines(miss_matches)
    print(f"missed matches count: {len(miss_matches)}")

def get_matches_count(urls):
    return len(get_matches(urls))

def main():
    urls = get_urls()
    matches = get_matches_count(urls)
    print(f"regex fit all urls: {len(urls) == matches}")

if __name__ == "__main__":
    main()
