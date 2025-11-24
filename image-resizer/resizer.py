import os
from PIL import Image

def resize_image(input_path, output_path, width, height):
    try:
        img = Image.open(input_path)
        resized = img.resize((width, height))
        resized.save(output_path)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("\n" + "="*50)
    print("🖼️  IMAGE RESIZER TOOL 🖼️")
    print("="*50 + "\n")
    
    # Create output folder
    if not os.path.exists('output'):
        os.makedirs('output')
        print("📁 Created output folder\n")
    
    # Check input folder
    if not os.path.exists('input'):
        print("⚠️  Input folder not found!")
        print("👉 Please create an 'input' folder and add your images\n")
        return
    
    # Get image files
    files = os.listdir('input')
    images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    
    if not images:
        print("😕 No images found in input folder\n")
        return
    
    print(f"✨ Found {len(images)} images:")
    for img in images:
        print(f"   📷 {img}")
    
    # Get dimensions
    print()
    try:
        width = int(input("🔢 Enter width (px): "))
        height = int(input("🔢 Enter height (px): "))
    except:
        print("⚠️  Invalid input, using default 800x600")
        width, height = 800, 600
    
    print(f"\n🚀 Resizing to {width}x{height}...\n")
    
    success = 0
    for img_file in images:
        input_path = os.path.join('input', img_file)
        output_path = os.path.join('output', img_file)
        
        print(f"⚙️  {img_file}... ", end="")
        
        if resize_image(input_path, output_path, width, height):
            print("✅ Done")
            success += 1
        else:
            print("❌ Failed")
    
    print(f"\n{'='*50}")
    print(f"🎉 Success! Resized {success}/{len(images)} images")
    print(f"📂 Check the 'output' folder for your images")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()