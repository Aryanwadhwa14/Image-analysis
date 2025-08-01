# Image Analysis - Prompt Generation

The project uses Google's Gemini API to generate detailed prompts for images across different product categories. The prompts are designed to describe the background, aesthetics, and visual elements of images so they can be recreated with different items while maintaining the same visual style. Made it more easier to use.

## Project Structure

```
Image-analysis/
├── carrybags/
│   ├── carrybag/           # Carrybag images only
│   └── Model-carrybag/     # Carrybag images with models
├── footwear/
│   ├── casual-shoes/       # Casual shoes only
│   ├── formal-shoes/       # Formal shoes only
│   ├── Model-casual-shoes/ # Models with casual shoes
│   ├── Model-formal-shoes/ # Models with formal shoes
│   └── Model-sports-shoes/ # Models with sports shoes
├── jewellery/
│   ├── jewel-images/       # Jewellery images only
│   └── Model-jewellery/    # Jewellery images with models
├── Watches/
│   ├── watch/              # Watch images only
│   └── model-watch/        # Watch images with models
├── backpacks/              # Backpack images (existing)
├── handbags/               # Handbag images (existing)
├── carrybag_prompt.py      # Script for carrybag prompt generation
├── footwear_prompt.py      # Script for footwear prompt generation
├── jewellery_prompt.py     # Script for jewellery prompt generation
├── watches_prompt.py       # Script for watches prompt generation
├── run_all_prompts.py      # Master script to run all scripts
├── backpack_prompt.py      # Existing script for backpacks
└── requirements.txt        # Python dependencies
```

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Setup:**
   - The scripts are already configured with a Gemini API key
   - If you need to use your own API key, replace the key in each script file

## Usage

### Option 1: Run All Scripts at Once
```bash
python run_all_prompts.py
```
This will process all images in the correct order:
1. Carrybags
2. Footwear
3. Jewellery
4. Watches

### Option 2: Run Individual Scripts
```bash
# Process carrybag images only
python carrybag_prompt.py

# Process footwear images only
python footwear_prompt.py

# Process jewellery images only
python jewellery_prompt.py

# Process watch images only
python watches_prompt.py
```

## Output Files

Each script generates a separate output file:

- `carrybag_prompt_output.txt` - Prompts for carrybag images
- `footwear_prompt_output.txt` - Prompts for footwear images
- `jewellery_prompt_output.txt` - Prompts for jewellery images
- `watches_prompt_output.txt` - Prompts for watch images

## Output Format

Each output file contains prompts in the following format:

```
PROMPT 1:
Image: carrybag1.png
Category: carrybag only
[Generated detailed prompt describing the image's background, aesthetics, lighting, etc.]

PROMPT 2:
Image: carrybag2.png
Category: carrybag only
[Generated detailed prompt...]

...
```

## Prompt Description

The generated prompts focus on:
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

The prompts are designed to ignore any text or logos in the images and focus purely on the visual elements that can be recreated with different items.

## Processing Order

The scripts process images in the following chronological order:

### Carrybags
1. carrybag/ (carrybag only)
2. Model-carrybag/ (carrybag with model)

### Footwear
1. casual-shoes/ (casual shoes only)
2. formal-shoes/ (formal shoes only)
3. Model-casual-shoes/ (model with casual shoes)
4. Model-formal-shoes/ (model with formal shoes)
5. Model-sports-shoes/ (model with sports shoes)

### Jewellery
1. jewel-images/ (jewellery only)
2. Model-jewellery/ (model with jewellery)

### Watches
1. watch/ (watches only)
2. model-watch/ (model with watches)

## Error Handling

- Each script includes error handling for missing folders or files
- Progress is displayed for each image being processed
- Sample prompts are shown during processing for verification
- Detailed error messages are provided if any issues occur

## Requirements

- Python 3.7+
- google-generativeai>=0.3.0
- Pillow>=9.0.0
- pathlib (usually included with Python)

## Notes

- All images should be in PNG format
- The scripts automatically sort images alphabetically within each folder
- Processing time depends on the number of images and API response time
- Each script can be run independently or together using the master script
