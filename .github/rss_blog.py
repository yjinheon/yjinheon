import feedparser
import re
from pathlib import Path
from datetime import datetime
import pytz  # timezone 이슈
import xml.etree.ElementTree as ET

temp = feedparser.parse("https://yjinheon.netlify.app/rss.xml")


def update_readme(readme_base, rss_title):
    entries = temp["entries"][:5]
    posts = []

    # Parse the XML
    # Extract the date string
    # Convert the date string to a datetime object
    # Format the datetime object as YYYY-MM-DD

    for entry in entries:
        if entry["updated"]:
            parsed_date = datetime.striptime(
                entry["updated"], "%a, %d %b %Y %H:%M:%S %Z"
            )
        else:
            parsed_date = datetime.striptime(
                entry["published"], "%a, %d %b %Y %H:%M:%S %Z"
            )

        formatted_date = parsed_date.strftime("%Y-%m-%d")
        posts.append(
            f" - [{entry['title']}]({entry['links'][0]['href']}) ({formatted_date})"
        )

    posts_joined = "\n".join(posts)

    return (
        readme_base[: readme_base.find(rss_title)]
        + "## Recent Writings "
        + f"\n{posts_joined}"
    )


# print(fetch_writing())


rss_title = "## Recent Writings"
readme = Path("../README.md").read_text()
updated_readme = update_readme(readme, rss_title)
updated_time = f"\n Last Updated: {datetime.now(
    pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}"

with open("../README.md", "w") as f:
    f.write(updated_readme)
    f.write("\n")
    f.write(updated_time)
