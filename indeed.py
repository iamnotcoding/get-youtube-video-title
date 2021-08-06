import requests
from bs4 import BeautifulSoup

LIMIT = 5
"""
 !!LIMIT may not work properly!! please just use the default value : 5
 """
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    """
    get the max page number of site indeed
    """
    page, count_page = 0, 0
    max_page = 0
    page = 0  # page starts from 0

    while True:
        is_last_page = True
        result = requests.get(
            f"{URL}&start={page*10}")

        soup = BeautifulSoup(result.text, "html.parser")

        pagination = soup.find("div", {"class": "pagination"})
        
        links = pagination.find_all('a')
        pages = []

        for link in links:
            # append every page number
            if link['aria-label'] == "Previous":
                continue
            if link['aria-label'] == "Next":
                is_last_page = False
                break

            pages.append(int(link.find("span").string))
            count_page += 1
            print(pages)

        if is_last_page == True:
            break

        page += 1

    max_page = pages[-1]  # pages[-1] = the last page number
    return max_page  # return max page number


def extract_indeed_jobs(last_page):
    f = open("result.txt", "w")

    for page in range(last_page):
        print(f"page : {page}")
        # print(f"{URL}&start={page*LIMIT}")
        result = requests.get(f"{URL}&start={page*10}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})
        # print(results)

        for result in results:
            result = result.find("h2", {"class": "jobTitle"})
            span = result.find("span", {"class": ""})

            print(span.string)
            f.write(span.string + "\n")
