#!/usr/bin/env python3
"""
Script to fix orientation of specific bathroom portfolio images
Images 10, 12, and 13 are rotated incorrectly (turned left)
"""

from PIL import Image
import os

def fix_image_orientation(image_path, rotation_angle=90):
    """
    Fix image orientation by rotating it
    rotation_angle: 90 to rotate right (counterclockwise visual rotation fix)
                   -90 to rotate left
    """
    try:
        print(f"\nProcessing: {image_path}")
        
        if not os.path.exists(image_path):
            print(f"  ❌ File not found: {image_path}")
            return False
            
        # Open the image
        img = Image.open(image_path)
        original_size = os.path.getsize(image_path)
        
        print(f"  Original size: {img.size}")
        print(f"  Original file size: {original_size / 1024:.2f} KB")
        
        # Rotate the image (90 degrees clockwise = -90 in PIL, or use ROTATE_270)
        # Since images are turned to the left, we need to rotate right (270 degrees or -90)
        img_rotated = img.rotate(-90, expand=True)
        
        print(f"  New size after rotation: {img_rotated.size}")
        
        # Save the rotated image (overwrite original)
        # Preserve quality and optimize
        if image_path.lower().endswith('.webp'):
            img_rotated.save(image_path, 'WEBP', quality=85, method=6)
        elif image_path.lower().endswith(('.jpg', '.jpeg')):
            img_rotated.save(image_path, 'JPEG', quality=85, optimize=True)
        else:
            img_rotated.save(image_path, quality=85, optimize=True)
        
        new_size = os.path.getsize(image_path)
        print(f"  New file size: {new_size / 1024:.2f} KB")
        print(f"  ✅ Successfully rotated and saved!")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error processing {image_path}: {str(e)}")
        return False

def main():
    print("=" * 70)
    print("BATHROOM REMODELING - IMAGE ORIENTATION FIX")
    print("=" * 70)
    print("\nFixing images that are rotated to the left...")
    
    # Base directory
    base_dir = "/Users/bruno/Documents/LPS/CLIENTES/WOLF/BATHROOM REMODELING"
    
    # Images to fix (10, 12, 13 from portfolio)
    images_to_fix = [
        # Image 10
        os.path.join(base_dir, "3 - Bathroom Portfolio - Finished Projects/portfolio-master-bathroom.webp"),
        # Image 12
        os.path.join(base_dir, "portifolio imagens/20241030_105005_001.webp"),
        # Image 13
        os.path.join(base_dir, "portifolio imagens/IMG-20240913-WA0063.webp"),
    ]
    
    print(f"\nImages to fix: {len(images_to_fix)}")
    
    success_count = 0
    for image_path in images_to_fix:
        if fix_image_orientation(image_path):
            success_count += 1
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: {success_count}/{len(images_to_fix)} images successfully fixed")
    print("=" * 70)

if __name__ == "__main__":
    main()
