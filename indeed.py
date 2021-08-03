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
    result = requests.get(
        URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))  # append every page number

    max_page = pages[-1]  # pages[-1] = the last page number

    return max_page  # return max page number


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    # print(f"{URL}&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "job_seen_beacon"})
    # print(results)

    for result in results:
        result = result.find("h2", {"class": "jobTitle"})
        span = result.span

        print(span.text)
