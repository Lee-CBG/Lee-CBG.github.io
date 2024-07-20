import json
import argparse
import os

#TO-DO!
#Implement the social media links in _data/socialmedia.yml 

data_file = 'team_data.json'

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_member():
    member = {
        "name": input("Enter member's name: "),
        "full_name": input("Enter member's full name: "),
        "bio": input("Enter member's bio: "),
        "image": input("Enter path to member's image: "),
        "role": input("Enter member's role: ")
    }
    data = load_data()
    data.append(member)
    save_data(data)
    print("Member added successfully!")

def remove_member():
    name = input("Enter the name of the member to remove: ")
    data = load_data()
    data = [member for member in data if member['name'] != name]
    save_data(data)
    print("Member removed successfully!")

def generate_markdown():
    print("Current working directory:", os.getcwd())
    data = load_data()
    directory = "../pages"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    markdown_file_path = os.path.join(directory, 'team.md')
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write("---\nlayout: page-fullwidth\ntitle: \"Team\"\nmeta_title: \"\"\nsubheadline: \"\"\nteaser: \"\"\npermalink: \"/team/\"\nheader:\n    image_fullwidth: \"genvis-dna-bg_optimized_v1a.png\"\n---\n")
        file.write("<div data-magellan-expedition=\"fixed\">\n  <ul class=\"sub-nav\">\n")

        # Assuming roles are predefined sections
        roles = set(member['role'] for member in data)
        for role in roles:
            file.write(f"    <li data-magellan-arrival=\"{role.replace(' ', '_')}\"><a href=\"#{role.replace(' ', '_')}\">{role}</a></li>\n")
        file.write("  </ul>\n</div>\n")

        for role in roles:
            file.write(f"<h2 data-magellan-destination=\"{role.replace(' ', '_')}\">{role}</h2>\n")
            file.write(f"<a name=\"{role.replace(' ', '_')}\"></a>\n")
            for member in [m for m in data if m['role'] == role]:
                file.write(f"{{% include team_member member_name=\"{member['name']}\" full_name=\"{member['full_name']}\" bio='{member['bio']}' image=\"{member['image']}\" role=\"{member['role']}\" %}}\n")

    print("Markdown file generated successfully!", markdown_file_path)

def main():
    while True:
        print("Manage Team Information")
        print("1. Add a new team member")
        print("2. Remove a team member")
        print("3. Generate markdown file")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_member()
            print("Don't forget to generate Markdown!")
        elif choice == '2':
            remove_member()
            print("Don't forget to generate Markdown!")
        elif choice == '3':
            generate_markdown()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
