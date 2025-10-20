"""
Generate PWA Icons for QR Code Maker
Creates 192x192 and 512x512 PNG icons
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL not available, creating simple icons with basic shapes")

import os

def create_icon_simple(size, filename):
    """Create icon without PIL - using basic drawing"""
    # This creates a very basic bitmap manually
    # For production, use PIL or design tool
    
    # Create minimal PNG header and data
    # This is a workaround - icons should be generated with proper tools
    print(f"Creating placeholder {size}x{size} icon: {filename}")
    print("⚠️  Please use generate-icons.html in browser or design tool for better icons")
    
    # Create a simple colored square as placeholder
    # In real scenario, use PIL or Photoshop/Figma
    return False

def create_icon_with_pil(size, filename):
    """Create icon with PIL"""
    # Create image with gradient background
    img = Image.new('RGB', (size, size), color='#0078d4')
    draw = ImageDraw.Draw(img)
    
    # Draw gradient-like effect
    for y in range(size):
        color_val = int(0x00 + (0x10 * y / size))
        color = f'#{color_val:02x}78d4'
        draw.line([(0, y), (size, y)], fill=color, width=1)
    
    # Draw QR-like pattern
    block = size // 8
    
    # Top-left corner square
    draw.rectangle([block, block, block*3, block*3], fill='white')
    draw.rectangle([block*1.5, block*1.5, block*2.5, block*2.5], fill='#0078d4')
    
    # Top-right corner square
    draw.rectangle([block*5, block, block*7, block*3], fill='white')
    draw.rectangle([block*5.5, block*1.5, block*6.5, block*2.5], fill='#0078d4')
    
    # Bottom-left corner square
    draw.rectangle([block, block*5, block*3, block*7], fill='white')
    draw.rectangle([block*1.5, block*5.5, block*2.5, block*6.5], fill='#0078d4')
    
    # Center dot
    center = size // 2
    draw.ellipse([center-block//2, center-block//2, center+block//2, center+block//2], fill='white')
    
    # Save
    img.save(filename, 'PNG')
    print(f"✅ Created: {filename}")
    return True

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    if HAS_PIL:
        # Use PIL to create nice icons
        create_icon_with_pil(192, os.path.join(base_dir, 'icon-192.png'))
        create_icon_with_pil(512, os.path.join(base_dir, 'icon-512.png'))
        print("\n✅ Icons created successfully!")
        print("📝 Review icons and customize if needed")
    else:
        print("\n❌ PIL/Pillow not installed")
        print("\n📋 Options to create icons:")
        print("1. Install PIL: pip install Pillow")
        print("2. Open generate-icons.html in browser (automatic download)")
        print("3. Use online tool: https://realfavicongenerator.net/")
        print("4. Design manually in Photoshop/Figma/Canva")
        print("\n⚠️  App will work without icons, but PWA install may not show proper icon")
