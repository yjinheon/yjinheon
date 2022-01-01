import feedparser
import re
from pathlib import Path

temp = feedparser.parse('https://yjinheon.github.io/rss2.xml')

def update_readme(readme_base):
    entries = feedparser.parse('https://yjinheon.github.io/rss2.xml')['entries'][:5]
    posts = []

    for entry in entries:
        posts.append(f" - [{entry['title']}]({entry['link']})")
    posts_joined = '\n'.join(posts)

    return readme_base[:readme_base.find(rss_title)] + f"\n{posts_joined}"


#print(fetch_writing())


rss_title = "## My Recent Posts"
readme = Path('../README.md').read_text()
updated_readme = update_readme(readme)

with open('../README.md') as f:
    f.write()
