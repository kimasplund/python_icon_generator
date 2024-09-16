"""
Icon Generator Script

This script generates square PNG icons of specified sizes, background colors,
and three rows of customizable text using a custom font. It's ideal for creating
custom icons for applications, websites, or projects.

Author: Kim Asplund
License: MIT
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont

# Variables
sizes_str = "24,48,128,256,512"  # Specify the sizes as a comma-separated string
sizes = [int(s.strip()) for s in sizes_str.split(",")]
background_color = "blue"  # Specify the background color

# Text row 1 settings (top row)
text_row_1 = "Python"
text_row_1_size = 0.2  # Relative to icon size
text_row_1_bold = "n"  # "y" for bold, "n" for regular
text_row_1_color = "green"
text_row_1_display = "y"  # "y" to display, "n" to hide
text_row_1_align = "center"  # "left", "center", or "right"

# Text row 2 settings (main centered row)
text_row_2 = "I.G."
text_row_2_size = 0.6  # Relative to icon size
text_row_2_bold = "y"  # "y" for bold, "n" for regular
text_row_2_color = "white"
text_row_2_display = "y"  # "y" to display, "n" to hide
text_row_2_align = "center"  # "left", "center", or "right"
main_row_vertical_adjustment = -75  # Adjust as needed
top_row_spacing = 0.1  # Spacing between top row and main row (as a fraction of image size)
bottom_row_spacing = 0.1  # Spacing between main row and bottom row (as a fraction of image size)

# Text row 3 settings (bottom row)
text_row_3 = "v.1"
text_row_3_size = 0.2  # Relative to icon size
text_row_3_bold = "n"  # "y" for bold, "n" for regular
text_row_3_color = "yellow"
text_row_3_display = "y"  # "y" to display, "n" to hide
text_row_3_align = "center"  # "left", "center", or "right"

filename_template = "icon{}.png"  # Filename template to include size
font_url = 'https://github.com/google/fonts/raw/main/ufl/ubuntu/Ubuntu-Regular.ttf'
font_url_bold = 'https://github.com/google/fonts/raw/main/ufl/ubuntu/Ubuntu-Bold.ttf'

def download_font(url):
    filename = os.path.basename(url)
    if not os.path.exists(filename):
        print(f'Downloading {filename}...')
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f'{filename} already downloaded.')
    return filename

def create_base_image(size=512):
    img = Image.new('RGB', (size, size), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    font1 = ImageFont.truetype(download_font(font_url_bold if text_row_1_bold == "y" else font_url), int(size * text_row_1_size))
    font2 = ImageFont.truetype(download_font(font_url_bold if text_row_2_bold == "y" else font_url), int(size * text_row_2_size))
    font3 = ImageFont.truetype(download_font(font_url_bold if text_row_3_bold == "y" else font_url), int(size * text_row_3_size))
    
    # Prepare text rows
    rows = []
    text_heights = []
    text_widths = []
    for i, (text, font, display, align) in enumerate([
        (text_row_1, font1, text_row_1_display, text_row_1_align),
        (text_row_2, font2, text_row_2_display, text_row_2_align),
        (text_row_3, font3, text_row_3_display, text_row_3_align)
    ]):
        if display == "y":
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_widths.append(text_width)
            text_heights.append(text_height)
            rows.append((text, font, text_width, text_height, align))
    
    # Find the main row index
    main_row_index = 1 if len(rows) > 1 else 0
    
    # Calculate total heights and spacings
    total_top_text_height = sum(text_heights[:main_row_index])
    total_bottom_text_height = sum(text_heights[main_row_index+1:])
    n_top_spacings = main_row_index
    n_bottom_spacings = len(rows) - main_row_index - 1
    total_top_spacing = n_top_spacings * size * top_row_spacing
    total_bottom_spacing = n_bottom_spacings * size * bottom_row_spacing
    total_height = (
        total_top_text_height + total_top_spacing +
        text_heights[main_row_index] +
        total_bottom_text_height + total_bottom_spacing
    )
    
    # Calculate starting y position
    y_start = (size - total_height) / 2
    y_positions = []
    y = y_start
    
    # Calculate y positions for each row
    for i in range(len(rows)):
        y_positions.append(y)
        y += text_heights[i]
        if i < main_row_index:
            y += size * top_row_spacing
        elif i == main_row_index:
            pass  # No spacing after main row yet
        else:
            y += size * bottom_row_spacing
    
    # Adjust main row position with vertical adjustment
    y_positions[main_row_index] += main_row_vertical_adjustment
    
    # Draw text
    for i, (text, font, text_width, text_height, align) in enumerate(rows):
        if align == "left":
            x = 0
        elif align == "right":
            x = size - text_width
        else:  # center
            x = (size - text_width) / 2
        
        y = y_positions[i]
        color = globals()[f"text_row_{i+1}_color"]
        draw.text((x, y), text, font=font, fill=color)
    
    return img

def create_image(size, filename):
    base_img = create_base_image(512)
    if size != 512:
        img = base_img.resize((size, size), Image.LANCZOS)
    else:
        img = base_img
    img.save(filename)

# Generate images for each size
for size in sizes:
    filename = filename_template.format(size)
    create_image(size, filename)
    print(f"Generated {filename}")
