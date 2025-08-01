import subprocess
import sys
import os

def run_script(script_name):
    """Run a Python script and handle any errors"""
    print(f"\n{'='*60}")
    print(f"Running {script_name}...")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, 
                              text=True, 
                              encoding='utf-8')
        
        if result.returncode == 0:
            print(f"✅ {script_name} completed successfully!")
            print("Output:")
            print(result.stdout)
        else:
            print(f"❌ {script_name} failed with error:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error running {script_name}: {str(e)}")
        return False
    
    return True

def main():
    """Run all prompt generation scripts in order"""
    print("🚀 Starting Image Analysis - Prompt Generation")
    print("This will process all images in the following order:")
    print("1. Carrybags")
    print("2. Footwear") 
    print("3. Jewellery")
    print("4. Watches")
    
    # List of scripts to run in order
    scripts = [
        "carrybag_prompt.py",
        "footwear_prompt.py", 
        "jewellery_prompt.py",
        "watches_prompt.py"
    ]
    
    successful_runs = 0
    total_scripts = len(scripts)
    
    for script in scripts:
        if os.path.exists(script):
            if run_script(script):
                successful_runs += 1
        else:
            print(f"❌ Script {script} not found!")
    
    print(f"\n{'='*60}")
    print("📊 FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"Successfully completed: {successful_runs}/{total_scripts} scripts")
    
    if successful_runs == total_scripts:
        print("🎉 All scripts completed successfully!")
        print("\nGenerated output files:")
        print("- carrybag_prompt_output.txt")
        print("- footwear_prompt_output.txt") 
        print("- jewellery_prompt_output.txt")
        print("- watches_prompt_output.txt")
    else:
        print("⚠️  Some scripts failed. Please check the errors above.")
    
    print(f"\n{'='*60}")

if __name__ == "__main__":
    main() 