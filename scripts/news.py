import json
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.realpath(__file__))

data_file = os.path.join(script_dir, 'news_data.json')

def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_news():
    news = {
        "title": input("Enter news title: "),
        "teaser": input("Enter news teaser: "),
        "image_fullwidth": "genvis-dna-bg_optimized_v1a.png",
        "content": input("Enter news content: ")
    }
    data = load_data()
    data.append(news)
    save_data(data)
    print("News added successfully!")

def remove_news():
    title = input("Enter the title of the news to remove: ")
    data = load_data()
    filtered_data = [news for news in data if news['title'] != title]

    if len(data) == len(filtered_data):
        print("No news found with that title.")
        return
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_title = title.replace(' ', '-').lower().replace('/', '-').replace('\\', '-')
    filename = f"{date_str}-{safe_title}.md"
    directory = "_posts"
    markdown_file_path = os.path.join(directory, filename)

    try:
        os.remove(markdown_file_path)
        print(f"Removed markdown file: {markdown_file_path}")
    except OSError as e:
        print(f"Error removing markdown file: {e.strerror}")

    save_data(filtered_data)
    print("News removed successfully!")

def generate_markdown():
    data = load_data()
    directory = "_posts"
    if not os.path.exists(directory):
        os.makedirs(directory)

    #print('here')
    
    for news in data:
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{date_str}-{news['title'].replace(' ', '-').lower()}.md"
        markdown_file_path = os.path.join(directory, filename)
        with open(markdown_file_path, 'w', encoding='utf-8') as file:
            file.write("---\n")
            file.write(f"layout: page\n")
            file.write(f"title: \"{news['title']}\"\n")
            file.write(f"teaser: \"{news['teaser']}\"\n")
            file.write(f"header:\n    image_fullwidth: \"{news['image_fullwidth']}\"\n")
            file.write("breadcrumb: true\n")
            file.write("---\n\n")
            file.write(news['content'] + "\n")
        print(f"Markdown file generated successfully for news: {news['title']} at {markdown_file_path}")

def main():
    while True:
        print("Manage News Posts")
        print("1. Add a new news post")
        print("2. Remove a news post")
        print("3. Generate markdown files")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_news()
        elif choice == '2':
            remove_news()
        elif choice == '3':
            generate_markdown()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
