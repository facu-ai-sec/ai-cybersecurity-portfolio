import requests
import csv
from datetime import datetime

URL = "https://jsonplaceholder.typicode.com/posts"
TIMEOUT = 5
USER_ID = 1
OUTPUT_FILE = "filtered_posts.csv"

def fetch_posts(url):
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def filter_posts(posts, user_id):
    return [post for post in posts if post.get("userId") == user_id]


def export_posts_to_csv(posts, filename):
    fieldnames = ["userId", "id", "title"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for post in posts:
            writer.writerow({
                "userId": post["userId"],
                "id": post["id"],
                "title": post["title"]
            })


def log_summary(posts, user_id):
    print("Execution summary")
    print("-----------------")
    print(f"Filtered user: {user_id}")
    print(f"Number of posts: {len(posts)}")
    print(f"Date and time: {datetime.now()}")


def main():
    try:
        posts = fetch_posts(URL)

        filtered_posts = filter_posts(posts, USER_ID)

        if not filtered_posts:
            print("No posts were found for the specified user.")
            return

        export_posts_to_csv(filtered_posts, OUTPUT_FILE)

        log_summary(filtered_posts, USER_ID)

        print(f"\nFile successfully generated: {OUTPUT_FILE}")

    except requests.exceptions.RequestException as e:
        print("Error while consuming the API:", e)


if __name__ == "__main__":
    main()
