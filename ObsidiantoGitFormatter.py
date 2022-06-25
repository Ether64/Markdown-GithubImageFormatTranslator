import re
from urllib.parse import quote_plus

CDN = 'https://cdn.ethereal.bond/file/github-images/'


# def link_subber(match: re.Match):
#     image = match.group(1)
#     quoted_image = quote_plus(image)
#     return F"![]({cdn}{quoted_image})"


def convert_links(markdown_str) -> str:
    # subbed = re.sub(r'\!\[\[(.*)\]\]', link_subber, contents)
    subbed = re.sub(
        r'\!\[\[(.*)\]\]', lambda match: F"![]({CDN+quote_plus(match.group(1))})", markdown_str)
    return subbed


def main():
    markdown_file = input(
        'Enter the markdown file you would like to convert to Github\'s image formatting: ')
    with open(markdown_file, 'r') as f:
        contents = f.read()

    new_markdown = convert_links(contents)

    with open(markdown_file.replace('.md', '.gh.md'), 'w') as f:
        f.write(new_markdown)


if __name__ == '__main__':
    main()

#![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)  .... Example Github Image Formatting
