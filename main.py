from indeed import extract_indeed_pages, extract_indeed_jobs

# function gets the max page number of indeed site
last_indeed_pages = extract_indeed_pages()

print(last_indeed_pages)
extract_indeed_jobs(last_indeed_pages)
