# Fake News Detector

## Overview
This is a **Fake News Detector** that allows users to check if a news headline or snippet might be fake based on a predefined list of fake news phrases. Users can also view and add fake news phrases to improve detection.

## Features
- **Check News Authenticity**: Enter a news snippet to check if it matches known fake news phrases.
- **View Fake News Phrases**: Displays the list of stored fake news phrases.
- **Add New Fake News Phrases**: Users can contribute by adding suspicious phrases.
- **Persistence**: Saves and loads fake news phrases from a JSON file.

## How to Use
1. Run the Python script.
2. Choose an option from the menu:
   - `1` Check a news headline or snippet.
   - `2` View the stored fake news phrases.
   - `3` Add a new fake news phrase.
   - `4` Exit the program.
3. If checking news, the system will compare the input with stored phrases and return a similarity result.
4. If adding new phrases, the system updates the JSON file for future checks.

## Installation
Ensure you have Python installed (version 3.x recommended).

### Steps:
1. Copy the script into a Python file (e.g., `fake_news_detector.py`).
2. Open a terminal or command prompt and navigate to the script location.
3. Run the script using:
   ```sh
   python fake_news_detector.py
   ```

## Code Explanation
- `load_fake_news()`: Loads saved fake news phrases from `fake_news_phrases.json`.
- `save_fake_news(phrases)`: Saves new fake news phrases to the JSON file.
- `check_fake_news(input_text, fake_news_list)`: Checks if the input matches any stored fake news phrase with a similarity threshold.
- `main()`: Runs the interactive menu for users to check or manage fake news phrases.

## Example Output
```
Fake News Detector
1. Check a news headline/article snippet
2. View fake news phrases
3. Add a new fake news phrase
4. Exit
Choose an option: 1
Enter a news headline or article snippet: "Breaking: The world is ending tomorrow!"
This might be fake news!
```

## Future Enhancements
- **Integrate with real fact-checking APIs** for more accuracy.
- **Improve phrase-matching algorithms** for better detection.
- **GUI version** for an easier user experience.

## License
This project is open-source and free to use for learning and research purposes.

