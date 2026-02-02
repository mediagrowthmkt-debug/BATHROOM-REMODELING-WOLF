#!/usr/bin/env python3
"""
Script to fix orientation of images 12 and 14
Image 12: turned left (needs rotation right)
Image 14: turned right (needs rotation left)
"""

from PIL import Image
import os

def fix_image_orientation(image_path, rotation_angle):
    """
    Fix image orientation by rotating it
    rotation_angle: -90 to rotate right (fix image turned left)
                    90 to rotate left (fix image turned right)
    """
    try:
        print(f"\nProcessing: {os.path.basename(image_path)}")
        
        if not os.path.exists(image_path):
            print(f"  ❌ File not found: {image_path}")
            return False
            
        # Open the image
        img = Image.open(image_path)
        original_size = os.path.getsize(image_path)
        
        print(f"  Original size: {img.size}")
        print(f"  Original file size: {original_size / 1024:.2f} KB")
        print(f"  Rotation: {rotation_angle} degrees")
        
        # Rotate the image
        img_rotated = img.rotate(rotation_angle, expand=True)
        
        print(f"  New size after rotation: {img_rotated.size}")
        
        # Save the rotated image (overwrite original)
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
    print("BATHROOM REMODELING - IMAGE ORIENTATION FIX (12 & 14)")
    print("=" * 70)
    
    # Base directory
    base_dir = "/Users/bruno/Documents/LPS/CLIENTES/WOLF/BATHROOM REMODELING"
    
    # Images to fix with their required rotation
    images_to_fix = [
        # Image 12 - turned left, needs to rotate right (-90)
        {
            "path": os.path.join(base_dir, "portifolio imagens/20241030_105005_001.webp"),
            "rotation": -90,
            "description": "Image 12 (turned left)"
        },
        # Image 14 - turned right, needs to rotate left (90)
        {
            "path": os.path.join(base_dir, "portifolio imagens/2.webp"),
            "rotation": 90,
            "description": "Image 14 (turned right)"
        },
    ]
    
    print(f"\nImages to fix: {len(images_to_fix)}")
    
    success_count = 0
    for img_info in images_to_fix:
        print(f"\n--- {img_info['description']} ---")
        if fix_image_orientation(img_info['path'], img_info['rotation']):
            success_count += 1
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: {success_count}/{len(images_to_fix)} images successfully fixed")
    print("=" * 70)

if __name__ == "__main__":
    main()
