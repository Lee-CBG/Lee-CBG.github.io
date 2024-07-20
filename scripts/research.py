import json
import os
#TO-DO!
#The markdown header has to be updated real time to add title on top.

script_dir = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_dir, 'research_data.json')
markdown_file_path = os.path.join(script_dir, '..', 'pages', 'research.md')

# Default header for markdown file
markdown_header = """---
layout: page-fullwidth
title: "Research"
meta_title: ""
subheadline: ""
teaser: ""
permalink: "/research/"
header:
    image_fullwidth: "genvis-dna-bg_optimized_v1a.png"
---

<div data-magellan-expedition="fixed">
  <ul class="sub-nav">
    <li data-magellan-arrival="Overview"><a href="#Overview">Overview</a></li>
  </ul>
</div>

<h2 data-magellan-destination="Overview">Overview</h2>
<a name="Overview"></a>

The research conducted by this laboratory spans a wide range of topics in genomics, molecular biology, and computational biology, showcasing a multidisciplinary approach to understanding fundamental biological processes. The team has made significant contributions to the field of immunology, particularly in the realm of T-cell receptor (TCR) and epitope interactions. Pioneering work includes the development of advanced computational models such as ATM-TCR, a multi-head self-attention model for predicting TCR-epitope binding affinities, and PiTE, a TCR-epitope binding affinity prediction pipeline utilizing a Transformer-based Sequence Encoder. These computational tools provide valuable insights into the dynamics of immune responses and have potential applications in vaccine development and personalized medicine.

Moreover, the research team delves into the intricacies of DNA replication and transcription processes, shedding light on the factors influencing mutation rates and transcript errors in bacterial pathogens like Salmonella enterica subsp. enterica and Escherichia coli. Their work not only uncovers the complexities of mutagenesis but also challenges existing paradigms, as seen in studies on DNA replication-transcription conflicts and the symmetrical wave pattern of base-pair substitution rates across the E. coli chromosome. Beyond the laboratory bench, the team engages with broader societal issues, addressing privacy and ethical considerations in wastewater monitoring. Their commitment to understanding and advancing both the theoretical and practical aspects of genomics and molecular biology positions this research group at the forefront of innovative scientific inquiry.
"""

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_research():
    section = {
        "id": input("Enter section ID: "),
        "title": input("Enter section title: "),
        "description": input("Enter section description: "),
        "team": input("Enter team members: "),
        "image": input("Enter image path: "),
        "citation": input("Enter citation URL: ")
    }
    content_format = """{{% include project
      title="{title}"
      description="{description}"
      team="{team}"
      image="{image}"
      citation="{citation}"
    %}}"""
    section['content'] = content_format.format(**section)
    data = load_data()
    data.append(section)
    save_data(data)
    print("Research section added successfully!")

def remove_research():
    section_id = input("Enter section ID to remove: ")
    data = load_data()
    data = [section for section in data if section['id'] != section_id]
    save_data(data)
    print("Research section removed successfully!")

def generate_markdown():
    data = load_data()
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_header)
        for section in data:
            file.write(f"<h2 data-magellan-destination=\"{section['id']}\">{section['title']}</h2>\n")
            file.write(f"<a name=\"{section['id']}\"></a>\n")
            file.write(f"{section['content']}\n\n")
    print(f"Markdown file generated successfully at {markdown_file_path}")

def main():
    while True:
        print("\nManage Research Sections")
        print("1. Add a new research section")
        print("2. Remove a research section")
        print("3. Generate markdown file")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_research()
        elif choice == '2':
            remove_research()
        elif choice == '3':
            generate_markdown()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
