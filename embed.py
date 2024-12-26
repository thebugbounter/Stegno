from PIL import Image

def embed_message(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    # Convert the message to binary with a delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'  # Null byte as delimiter
    message_index = 0
    
    for i in range(img.width):
        for j in range(img.height):
            if message_index < len(binary_message):
                pixel = list(pixels[i, j])
                for k in range(3):  # RGB channels
                    if message_index < len(binary_message):
                        pixel[k] = (pixel[k] & 0xFE) | int(binary_message[message_index])
                        message_index += 1
                pixels[i, j] = tuple(pixel)
            if message_index >= len(binary_message):
                break
        if message_index >= len(binary_message):
            break
    
    img.save(output_path)
    print("Message embedded successfully.")

embed_message('image.jpg', 'Hello', 'output_image.png')
