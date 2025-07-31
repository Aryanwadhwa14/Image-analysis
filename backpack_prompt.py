import os
import base64
from pathlib import Path
import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini API
genai.configure(api_key="AIzaSyBVyU9U9fzjz3nspvBPKFn_dW21ZwwQ79Y")

def get_image_prompt_from_gemini(image_path):
    """Get detailed prompt from Gemini for a single image"""
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Create Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        prompt_text = """Describe this image in high detail to be able to re-generate a similar image with the same background and aesthetics with any other item. 
        Make the prompt more defining for the image, and ignore any texts or logo from it and also Do not describe the product company too. 
        Focus on:
        - Background setting and environment
        - Lighting and shadows
        - Color scheme and mood
        - Composition and framing
        - Textures and materials
        - Overall aesthetic style
        - Camera angle and perspective
        - Environmental details
        - Any props or accessories visible
        - The overall visual atmosphere
        
        Provide a detailed, descriptive prompt that could be used to recreate this exact scene with a different item."""
        
        # Generate content with image
        response = model.generate_content([prompt_text, image])
        
        # Return the text response
        return response.text
        
    except Exception as e:
        return f"Error processing image: {str(e)}"

def main():
    # Define the folders and their order
    folders = [
        ("handbags", "handbags"),
        ("Model-handbags", "handbags with models"), 
        ("backpacks", "backpacks"),
        ("Model-backpacks", "backpacks with models")
    ]
    
    # Collect all image paths in order
    image_paths = []
    for folder_name, folder_category in folders:
        folder_path = Path(folder_name)
        if folder_path.exists():
            # Get all PNG files in the folder
            png_files = sorted(folder_path.glob("*.png"))
            for png_file in png_files:
                image_paths.append({
                    'path': str(png_file),
                    'filename': png_file.name,
                    'folder': folder_category
                })
    
    print(f"Found {len(image_paths)} images to process")
    print("=" * 50)
    
    # Process each image
    results = []
    for i, img_info in enumerate(image_paths, 1):
        print(f"Processing image {i}/{len(image_paths)}: {img_info['filename']}")
        
        prompt = get_image_prompt_from_gemini(img_info['path'])
        
        # Debug: Print a sample of the prompt to verify it's readable
        print(f"Sample prompt (first 200 chars): {prompt[:200]}...")
        
        results.append({
            'Image_Number': i,
            'Folder_Category': img_info['folder'],
            'Filename': img_info['filename'],
            'Image_Path': img_info['path'],
            'Generated_Prompt': prompt
        })
        
        print(f"Completed: {img_info['filename']}")
        print("-" * 50)
    
    # Save results to TXT file
    txt_filename = "image_prompts_output.txt"
    
    with open(txt_filename, 'w', encoding='utf-8') as txtfile:
        for result in results:
            txtfile.write(f"PROMPT {result['Image_Number']}:\n")
            txtfile.write(result['Generated_Prompt'])
            txtfile.write("\n\n")
    
    print(f"\nResults saved to {txt_filename}")
    print(f"Successfully processed {len(results)} images")
    
    # Print summary
    print("\nSummary of processed images:")
    for result in results:
        print(f"{result['Image_Number']}. {result['Folder_Category']} - {result['Filename']}")

if __name__ == "__main__":
    main()
