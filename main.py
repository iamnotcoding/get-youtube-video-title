from indeed import extract_indeed_pages, extract_indeed_jobs

# function gets the max page number of indeed site


max_indeed_pages = extract_indeed_pages()  # while there is next page button
print(max_indeed_pages)
extract_indeed_jobs(max_indeed_pages)
