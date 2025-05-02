import os
import subprocess

# Get the path to the images directory
current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, 'httpbin', 'templates', 'images')

# Open the PNG image
png_path = os.path.join(images_dir, 'pig_icon.png')
avif_path = os.path.join(images_dir, 'pig_icon.avif')

# Convert using avifenc command-line tool
try:
    subprocess.run(['avifenc', png_path, avif_path, '-y', '420', '-d', '8', '-s', '0'], check=True)
    print(f"Successfully converted {png_path} to {avif_path}")
except subprocess.CalledProcessError as e:
    print(f"Error converting image: {e}")
except FileNotFoundError:
    print("avifenc command-line tool not found. Please install it using: brew install libavif")

    