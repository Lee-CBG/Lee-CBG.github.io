from bs4 import BeautifulSoup
import os

# Constants
INPUT_HTML_FILE = 'output.html'
OUTPUT_MARKDOWN_FILE = '../pages/publications.md'
HEADER_MARKDOWN = """---
layout: page-fullwidth
title: "Selected Publications"
meta_title: ""
subheadline: ""
teaser: ""
permalink: "/publications/"
header:
    image_fullwidth: "genvis-dna-bg_optimized_v1a.png"
---

<div data-magellan-expedition="fixed">
  <ul class="sub-nav">
    <li data-magellan-arrival="2023"><a href="#2023">2023</a></li>
    <li data-magellan-arrival="2022"><a href="#2022">2022</a></li>
    <li data-magellan-arrival="2021"><a href="#2021">2021</a></li>
    <li data-magellan-arrival="2020"><a href="#2020">2020</a></li>
    <li data-magellan-arrival="2019"><a href="#2019">2019</a></li>
    <li data-magellan-arrival="2018"><a href="#2018">2018</a></li>
    <li data-magellan-arrival="2017"><a href="#2017">2017</a></li>
    <li data-magellan-arrival="2016"><a href="#2016">2016</a></li>
    <li data-magellan-arrival="2015"><a href="#2015">2015</a></li>
    <li data-magellan-arrival="All"><a href="#All">All</a></li>
  </ul>
</div>
"""

def parse_html_to_markdown(input_html, output_markdown):
    with open(input_html, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract publication years and details
    years = soup.find_all('h3', id=lambda x: x and x.startswith('y'))
    markdown_content = HEADER_MARKDOWN

    for year in years:
        year_text = year.get_text(strip=True)
        markdown_content += f"\n<h2 data-magellan-destination=\"{year_text}\">{year_text}</h2>\n<a name=\"{year_text}\"></a>\n\n"
        ul = year.find_next('ul')
        if ul:
            publications = ul.find_all('li')
            for pub in publications:
                title = pub.find('i').get_text(strip=True)
                authors = pub.contents[0].strip().rstrip(',')
                journal = pub.find('b') and pub.find('b').next_sibling.strip().strip(',')
                doi_link = pub.find('a', href=True) and pub.find('a', href=True)['href']
                markdown_content += f"{{% include publication authors=\"{authors}\" title=\"{title}\" journal=\"{journal}\" doi=\"{doi_link}\" %}}\n"
        else:
            print(f"Warning: No publications found for the year {year_text}")

    # Write to Markdown file
    with open(output_markdown, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print("Markdown file generated successfully at:", output_markdown)

if __name__ == "__main__":
    parse_html_to_markdown(INPUT_HTML_FILE, OUTPUT_MARKDOWN_FILE)
