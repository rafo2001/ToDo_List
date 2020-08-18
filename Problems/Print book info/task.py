def print_book_info(title, author=None, year=None):
    #  Write your code here
    output = f'"{title}"'
    if not (author is None and year is None):
        output += " was written"
    if author is not None:
        output += " by " + author
    if year is not None:
        output += " in " + year
    print(output)
