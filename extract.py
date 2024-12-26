from PIL import Image

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    binary_message = ''
    
    for i in range(img.width):
        for j in range(img.height):
            pixel = pixels[i, j]
            for k in range(3):  # RGB channels
                binary_message += str(pixel[k] & 1)
    
    # Split the binary message into 8-bit chunks
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':  # Null byte delimiter
            break
        message += chr(int(byte, 2))
    
    return message

print("Extracted message:", extract_message('output_image.png'))
