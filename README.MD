# Stegno

Stegno is a Python-based steganography project that allows users to embed hidden text into an image and later extract the hidden text from the modified image.

## Features
- **Embed Text into an Image**: Use `embed.py` to select an image and hide text within it.
- **Extract Hidden Text**: Use `extract.py` to retrieve the hidden text from the image.

## Prerequisites
- Python 3.x
- [PyCharm](https://www.jetbrains.com/pycharm/) (recommended IDE for development)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/thebugbounter/Stegno.git
   ```
2. Open the project in PyCharm.
3. Install any required dependencies. You can use `pip` to install libraries if necessary:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Embedding Text
1. Run `embed.py`:
   ```bash
   python embed.py
   ```
2. Select an image and specify the text you want to hide.

### Extracting Text
1. Run `extract.py`:
   ```bash
   python extract.py
   ```
2. Select the image from which you want to extract the hidden text.

## Notes
- Ensure that the image file format supports steganography operations.
- Keep a backup of the original image for comparison purposes.

## Contributing
Feel free to fork the repository, make enhancements, and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
