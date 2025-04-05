from os.path import expanduser
from sqlite3 import connect
from instaloader import ConnectionException, Instaloader, Post
from time import sleep
import re

# Define file path to save comments
output_file_path = r"Enter the path for out put"


# Use raw string to avoid escape character issues
path_to_firefox_cookies = r"Enter your path for \cookies.sqlite"
USERNAME = "Enter insta username"

# Initialize Instaloader
instaloader = Instaloader(max_connection_attempts=1)

try:
    # Connect to Firefox's cookies SQLite database
    with connect(expanduser(path_to_firefox_cookies)) as con:
        cursor = con.execute("SELECT name, value FROM moz_cookies WHERE host='.instagram.com'")
        
        # Update Instaloader session cookies
        for name, value in cursor.fetchall():
            instaloader.context._session.cookies.set(name, value)

    # Check if login is successful
    username = instaloader.test_login()
    if username != USERNAME:
        raise ConnectionException("Login test failed. Cookie might be invalid or username mismatch.")

    # Save session for later use
    instaloader.context.username = USERNAME
    instaloader.save_session_to_file()
    print(f"Session saved successfully for user: {USERNAME}")

except ConnectionException as e:
    print(f"Cookie import failed: {e}")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

# Load session
instagram = Instaloader()
try:
    instagram.load_session_from_file(USERNAME)
    print(f"Session loaded successfully for user: {USERNAME}")
except Exception as e:
    print(f"Failed to load session: {e}")

# Instagram Post Shortcode
SHORTCODE = 'Enter instagram shortcode'  # Replace with actual post shortcode

# Regex pattern to detect emojis
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # Emoticons
                           u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # Transport & map symbols
                           u"\U0001F700-\U0001F77F"  # Alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric shapes
                           u"\U0001F800-\U0001F8FF"  # Supplemental arrows
                           u"\U0001F900-\U0001F9FF"  # Supplemental symbols
                           u"\U0001FA00-\U0001FA6F"  # Extended pictographs
                           u"\U0001FA70-\U0001FAFF"
                           "]+", flags=re.UNICODE)

try:
    post = Post.from_shortcode(instagram.context, SHORTCODE)
    comment_count = 0
    max_comments = 1000
    0

    print("\nFetching comments...\n")
    
    with open(output_file_path, "w", encoding="utf-8") as file:
        for x in post.get_comments():
            if comment_count >= max_comments:
                break

            comment_text = x.text if x.text else ""
            
            # Skip comments containing emojis
            if emoji_pattern.search(comment_text):
                continue

            comment_line = f"[{comment_count + 1}] {x.owner.username}: {comment_text}\n"
            print(comment_line.strip())  # Print to console
            file.write(comment_line)  # Write to file

            comment_count += 1
            sleep(2)  # Add delay to avoid rate limits

    print(f"\n✅ Successfully fetched {comment_count} comments (without emojis).\n")
    print(f"Comments saved to: {output_file_path}")

except Exception as e:
    print(f"Failed to fetch post data: {e}")