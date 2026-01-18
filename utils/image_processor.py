from PIL import Image
import io
import os
from typing import Tuple

class ImageProcessor:

    @staticmethod
    def validate_image(image_path: str) -> Tuple[bool, str]:
        try:
            image = Image.open(image_path)
            if image.format not in ['JPEG', 'JPG', 'PNG']:
                return False, "Image must be JPEG or PNG format"

            width, height = image.size
            if width < 200 or height < 200:
                return False, "Image resolution too low (minimum 200x200 pixels)"

            file_size = os.path.getsize(image_path)
            if file_size > 10 * 1024 * 1024:  # 10MB
                return False, "Image file too large (maximum 10MB)"

            return True, "Image valid"

        except Exception as e:
            return False, f"Invalid image file: {str(e)}"

    @staticmethod
    def preprocess_image(image_path: str, max_size: Tuple[int, int] = (1024, 1024)) -> str:
        
        img = Image.open(image_path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

        preprocessed_path = image_path.replace('.', '_processed.')
        img.save(preprocessed_path, quality=85, optimize=True)

        return preprocessed_path

    @staticmethod
    def get_image_metadata(image_path: str) -> dict:
    
        img = Image.open(image_path)
        return {
            "format": img.format,
            "size": img.size,
            "mode": img.mode,
            "file_size": os.path.getsize(image_path)
        }
