import difflib
import json

FAKE_NEWS_FILE = "fake_news_phrases.json"


def load_fake_news():
    try:
        with open(FAKE_NEWS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_fake_news(phrases):
    with open(FAKE_NEWS_FILE, "w") as file:
        json.dump(phrases, file)


def check_fake_news(input_text, fake_news_list):
    for phrase in fake_news_list:
        similarity = difflib.SequenceMatcher(None, input_text.lower(), phrase.lower()).ratio()
        if similarity > 0.7:  # Adjust threshold as needed
            return True
    return False


def main():
    fake_news_list = load_fake_news()

    while True:
        print("\nFake News Detector")
        print("1. Check a news headline/article snippet")
        print("2. View fake news phrases")
        print("3. Add a new fake news phrase")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            news_input = input("Enter a news headline or article snippet: ")
            if check_fake_news(news_input, fake_news_list):
                print("This might be fake news!")
            else:
                print("This seems legitimate.")

        elif choice == "2":
            print("\nFake News Phrases:")
            for phrase in fake_news_list:
                print(f"- {phrase}")

        elif choice == "3":
            new_phrase = input("Enter a new fake news phrase: ")
            if new_phrase not in fake_news_list:
                fake_news_list.append(new_phrase)
                save_fake_news(fake_news_list)
                print("Phrase added successfully!")
            else:
                print("Phrase already exists.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()