from PIL import Image
import os
import sys

def shrink_jpeg(input_dir, output_dir, compression_percent, quality):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Loop through all files in the input directory
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(('.jpg', '.jpeg')):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)

                # Open the image
                original_image = Image.open(input_path)

                # Calculate new dimensions based on compression percent
                width, height = original_image.size
                new_width = int(width * (compression_percent / 100))
                new_height = int(height * (compression_percent / 100))

                # Resize the image
                resized_image = original_image.resize((new_width, new_height), resample=Image.LANCZOS)

                # Save the resized and compressed image with specified quality
                resized_image.save(output_path, quality=quality)
                print(f"Processed: {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <input_directory> <output_directory> <compression_percent> <quality>")
        sys.exit(1)

    # Get command-line arguments
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    compression_percent = float(sys.argv[3])
    quality = int(sys.argv[4])

    # Call the function to shrink JPEG files in the input directory
    shrink_jpeg(input_directory, output_directory, compression_percent, quality)
