import os
import re
import shutil
from datetime import datetime

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"E:\tests\test2\content\posts"  # Hugo
attachments_dir = r"E:\Obsidian Blog\MyBlog"  # Obsidian
static_images_dir = r"E:\tests\test2\static\images"  # Hugo

# Ensure the static images directory exists
os.makedirs(static_images_dir, exist_ok=True)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Check if the file has front matter, add if missing
        if not content.startswith("---"):
            title = os.path.splitext(filename)[0]
            today = datetime.now().strftime("%Y-%m-%d")
            front_matter = f"""---
title: {title}
date: {today}
draft: false
tags:
  - obsidian
---

"""
            content = front_matter + content
        
        # Step 2: Find all Obsidian image embeds ![[image.png]]
        obsidian_images = re.findall(r'!\[\[([^]]*\.(png|jpg|jpeg|gif|webp))\]\]', content)
        
        # Step 3: Replace Obsidian image embeds with markdown format
        for image_match in obsidian_images:
            image = image_match[0]  # Get the filename from the tuple
            # Use the filename as alt text, but clean it up
            alt_text = os.path.splitext(image)[0].replace("Pasted image ", "Image ")
            markdown_image = f"![{alt_text}](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
        
        # Step 5: Find and replace Obsidian wiki links [[page]]
        wiki_links = re.findall(r'\[\[([^]|]*?)(?:\|([^]]*))?\]\]', content)
        for link_match in wiki_links:
            link_target = link_match[0]
            link_text = link_match[1] if len(link_match) > 1 and link_match[1] else link_target
            # Convert to markdown link, using slug-style URLs
            slug = link_target.lower().replace(" ", "-")
            markdown_link = f"[{link_text}](/{slug})"
            # Handle both [[page]] and [[page|text]] formats
            if link_match[1]:
                content = content.replace(f"[[{link_target}|{link_text}]]", markdown_link)
            else:
                content = content.replace(f"[[{link_target}]]", markdown_link)
        
        # Step 6: Fix any double exclamation marks in image references
        content = re.sub(r'!\[!\[(.*?)\]\((.*?)\)\]', r'![\1](\2)', content)
        
        # Step 7: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")