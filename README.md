# Icon Generator Script

A Python script to generate square PNG icons of specified sizes, background colors, and three rows of customizable text using a custom font. Ideal for creating custom icons for applications, websites, or projects.

| 24x24 | 48x48 | 128x128 | 256x256 | 512x512 |
|-------|-------|---------|---------|---------|
| ![Icon 24x24](icon24.png) | ![Icon 48x48](icon48.png) | ![Icon 128x128](icon128.png) | ![Icon 256x256](icon256.png) | ![Icon 512x512](icon512.png) |

## Features

- **Custom Sizes**: Generate icons of any square dimensions.
- **Background Colors**: Choose any background color using color names or hex codes.
- **Three Text Rows**: Add up to three separate lines of text to your icons.
- **Customizable Text Properties**: 
  - Set different sizes for each text row.
  - Choose between bold and regular font styles for each row.
  - Set different colors for each text row.
  - Show or hide each text row independently.
  - Align each text row (left, center, or right).
- **Adjustable Row Spacing**: Control the vertical space between text rows, with separate control for top and bottom spacing.
- **Vertical Adjustment**: Fine-tune the vertical position of the main text row.
- **Font Flexibility**: Uses the Ubuntu font (regular and bold) by default but can be customized.
- **Automatic Font Download**: Downloads the specified fonts if they're not already present.
- **Easy Customization**: Variables at the top of the script make customization straightforward.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
  - [Sizes](#sizes)
  - [Background Color](#background-color)
  - [Text Customization](#text-customization)
  - [Row Spacing and Vertical Adjustment](#row-spacing-and-vertical-adjustment)
  - [Output Filename Template](#output-filename-template)
  - [Font URLs](#font-urls)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Python 3.x**
- **Pip** (Python package manager)
- **Internet Connection** (for downloading the fonts)

---

## Installation

1. **Clone the Repository or Download the Script**

   ```bash
   git clone https://github.com/kimasplund/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Required Python Packages**

   ```bash
   pip install Pillow requests
   ```

---

## Usage

Run the script using the following command:

```bash
python icon_generator.py
```

This will generate PNG images based on the settings specified in the script.

---

## Customization

You can customize the script by modifying the variables at the top of the `icon_generator.py` file:

```python
# Variables
sizes_str = "24,48,128,256,512"  # Specify the sizes as a comma-separated string
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

# Text row 3 settings (bottom row)
text_row_3 = "v.1"
text_row_3_size = 0.2  # Relative to icon size
text_row_3_bold = "n"  # "y" for bold, "n" for regular
text_row_3_color = "yellow"
text_row_3_display = "y"  # "y" to display, "n" to hide
text_row_3_align = "center"  # "left", "center", or "right"

# Row spacing
top_row_spacing = 0.1  # Spacing between top row and main row (as a fraction of image size)
bottom_row_spacing = 0.1  # Spacing between main row and bottom row (as a fraction of image size)

filename_template = "icon{}.png"  # Filename template to include size
```

### Sizes

Specify the icon sizes by editing the `sizes_str` variable. Enter sizes as a comma-separated string.

```python
sizes_str = "24,48,128,256,512"
```

### Background Color

Set the background color by changing the `background_color` variable. You can use color names or hex codes.

```python
background_color = "blue"
```

### Text Customization

For each text row (1, 2, and 3), you can customize:

- **Text Content**: Set the text for each row using `text_row_1`, `text_row_2`, and `text_row_3`.
- **Text Size**: Set the size relative to the icon size using `text_row_1_size`, `text_row_2_size`, and `text_row_3_size`.
- **Bold Style**: Choose bold ("y") or regular ("n") using `text_row_1_bold`, `text_row_2_bold`, and `text_row_3_bold`.
- **Text Color**: Set the color using `text_row_1_color`, `text_row_2_color`, and `text_row_3_color`.
- **Display**: Choose to show ("y") or hide ("n") each row using `text_row_1_display`, `text_row_2_display`, and `text_row_3_display`.
- **Alignment**: Set text alignment to "left", "center", or "right" using `text_row_1_align`, `text_row_2_align`, and `text_row_3_align`.

### Row Spacing and Vertical Adjustment

Adjust the vertical space between text rows by modifying the `top_row_spacing` and `bottom_row_spacing` variables. These values are relative to the icon size.

```python
top_row_spacing = 0.1  # 10% of the icon size between top and main row
bottom_row_spacing = 0.1  # 10% of the icon size between main and bottom row
```

Fine-tune the vertical position of the main text row (row 2) using the `main_row_vertical_adjustment` variable:

```python
main_row_vertical_adjustment = -75  # Adjust as needed (negative values move up, positive move down)
```

### Output Filename Template

Customize the output filenames using the `filename_template` variable. The `{}` placeholder will be replaced with the size.

```python
filename_template = "icon{}.png"
```

### Font URLs

The script uses the Ubuntu font (regular and bold) by default. You can change the fonts by modifying the `font_url` and `font_url_bold` variables in the script.

---

## Examples

### Example 1: Generate Icons with Default Settings

Running the script without any modifications will generate icons of sizes 24x24, 48x48, 128x128, 256x256, and 512x512 pixels with a blue background and three rows of text.

```bash
python icon_generator.py
```

Here are the generated icons with default settings:

| 24x24 | 48x48 | 128x128 | 256x256 | 512x512 |
|-------|-------|---------|---------|---------|
| ![Icon 24x24](icon24.png) | ![Icon 48x48](icon48.png) | ![Icon 128x128](icon128.png) | ![Icon 256x256](icon256.png) | ![Icon 512x512](icon512.png) |

### Example 2: Customize Text, Colors, Alignment, and Spacing

Modify the variables in the script:

```python
background_color = "#FF5733"
text_row_1 = "MY"
text_row_1_color = "white"
text_row_1_align = "left"
text_row_2 = "APP"
text_row_2_color = "black"
text_row_2_align = "center"
text_row_3 = "3.0"
text_row_3_color = "yellow"
text_row_3_align = "right"
text_row_3_display = "y"  # Show the third row
top_row_spacing = 0.15  # Adjust spacing between top and main row
bottom_row_spacing = 0.2  # Adjust spacing between main and bottom row
main_row_vertical_adjustment = -50  # Move the main row up slightly
```

Run the script:

```bash
python icon_generator.py
```

This will generate a new set of icons with the customized settings. The appearance will differ from the default icons shown above.

---

## Troubleshooting

### Font Download Issues

If the script fails to download the fonts:

- **Check Internet Connection**: Ensure you have an active internet connection.
- **Verify Font URLs**: Make sure the `font_url` and `font_url_bold` are correct and accessible.
- **Firewall Restrictions**: Check if your firewall or antivirus software is blocking the download.

### Missing Modules Error

If you get an error like `ModuleNotFoundError: No module named 'PIL'`:

- **Install Missing Packages**:

  ```bash
  pip install Pillow requests
  ```

### Text Positioning Issues

- **Adjust Text Size**: If the text doesn't fit well, adjust the `text_row_X_size` values.
- **Modify Row Spacing**: If the rows are too close or far apart, adjust the `top_row_spacing` and `bottom_row_spacing` values.
- **Fine-tune Vertical Position**: Use `main_row_vertical_adjustment` to move the main text row up or down.
- **Check Text Length**: Ensure the text for each row isn't too long for the icon size.
- **Verify Alignment**: Make sure the `text_row_X_align` values are set correctly ("left", "center", or "right").

### Color Not Applied Correctly

- **Ensure Valid Color Names or Hex Codes**: Verify that all color variables are set to valid color names or hex codes.

### Text Not Displaying

- **Check Display Settings**: Ensure that `text_row_X_display` is set to "y" for rows you want to display.

---
## Keywords

Python icon generator
Custom square icons
Open-source icon script
Python script for custom icons
Create icons for applications

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, please contact Kim Asplund at [kim@asplund.kim](mailto:kim@asplund.kim).

More about me on my website: [https://asplund.kim](https://asplund.kim)

GitHub Profile: [https://github.com/kimasplund](https://github.com/kimasplund)
