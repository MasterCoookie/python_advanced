'''
There are two main functions in regex - search() and match().
Match tries to match the entire string while search() just looks for a
matching part.
'''
import re

def main():
    '''Main function'''
    line = "I think I understand regular expressions"

    match_result = re.match('think', line, re.M|re.I)
    if match_result:
        print("Match found:", match_result.group())
    else:
        print("No match was found")

    search_result = re.search('think', line, re.M|re.I)
    if search_result:
        print("Search found:", search_result.group())
    else:
        print("No search was found")

if __name__ == "__main__":
    main()
