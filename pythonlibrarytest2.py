from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(image_path):
    """Reads and returns EXIF data from an image file."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        exif = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            exif[tag] = value
        return exif
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def detect_ai_image(image_path):
    """Analyzes image EXIF data to guess if it is AI-generated."""
    exif = get_exif_data(image_path)

    if exif is None:
        # This message is now more contextual based on get_exif_data's output
        print("Could not retrieve EXIF data.")
    else:
        print("EXIF metadata found:")
        for key, val in exif.items():
            # To avoid printing very long byte strings (like MakerNote)
            if isinstance(val, bytes) and len(val) > 100:
                print(f"{key}: <Large data not shown>")
            else:
                print(f"{key}: {val}")

    # Simple heuristic: AI images often have no camera info or have specific software tags
    if exif is None:
        print(
            "\nAnalysis: No EXIF data found. The image might be AI-generated, scrubbed, or saved in a way that strips metadata.")
    elif 'Make' not in exif and 'Model' not in exif:
        # Checking for software tags that might indicate AI generation
        software = exif.get('Software', '').lower()
        if 'photoshop' in software or 'gimp' in software or 'midjourney' in software:
            print(
                f"\nAnalysis: Image edited or created with '{exif.get('Software')}'. This could be an AI-generated image.")
        else:
            print(
                "\nAnalysis: No camera make or model info found. This could indicate an AI-generated or heavily edited image.")
    else:
        print(
            f"\nAnalysis: Camera info detected (Make: {exif.get('Make')}, Model: {exif.get('Model')}). It is less likely to be purely AI-generated.")


# Usage
# Corrected the filename to include the '.jpg' extension as seen in the file explorer.
detect_ai_image('download.jpg')
