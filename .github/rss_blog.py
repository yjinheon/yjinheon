import feedparser
import re
from pathlib import Path
from datetime import datetime
import pytz # timezone 이슈

temp = feedparser.parse('https://yjinheon.github.io/rss2.xml')

def update_readme(readme_base,rss_title):
    entries = feedparser.parse('https://yjinheon.github.io/rss2.xml')['entries'][:5]
    posts = []

    for entry in entries:
        posts.append(f" - [{entry['title']}]({entry['link']})")
    posts_joined = '\n'.join(posts)

    return readme_base[:readme_base.find(rss_title)] +"## Recent Writings "+ f"\n{posts_joined}"


#print(fetch_writing())



rss_title = "## Recent Writings"
readme = Path('../README.md').read_text()
updated_readme = update_readme(readme,rss_title)
updated_time = f"\n Last Updated: {datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}"

with open('../README.md','w') as f:
    f.write(updated_readme)
    f.write("\n")
    f.write(updated_time)
    
