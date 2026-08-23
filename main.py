import os
from google import genai
from PIL import Image

# আপনার API Key (সঠিকভাবে সেট করা হয়েছে)
API_KEY = "AQ.Ab8RN6Jn3_OhMizcwyq9NfUw5-73lKJm6to6vZegmGryGZYMFw"

# নতুন ক্লায়েন্ট তৈরি
client = genai.Client(api_key=API_KEY)

def analyze_chart(image_path, timeframe):
    try:
        # ছবি খুঁজে পাওয়া যাচ্ছে কিনা পরীক্ষা
        if not os.path.exists(image_path):
            print(f"[!] Error: '{image_path}' ফাইলটি পাওয়া যায়নি!")
            return

        image = Image.open(image_path)
        prompt = (
            f"Analyze this trading chart image for a {timeframe} trade setup. "
            f"Provide key technical analysis, support and resistance levels, "
            f"trend direction, and potential entry/exit signals."
        )
        
        print(f"\n[+] Analyzing {image_path} for {timeframe} trade setup...")
        print("[+] Processing with gemini-2.0-flash... Please wait.\n")

        # আপডেটেড API কলের মাধ্যমে অ্যানালাইসিস
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[image, prompt]
        )

        print("=== Analysis Result ===")
        print(response.text)

    except Exception as e:
        print(f"\n[!] An error occurred during analysis: {e}")

def main():
    image_filename = "chart.png"
    
    print("--- SELECT TIMEFRAME ---")
    print("[1] 5 Seconds (5S)")
    print("[2] 10 Seconds (10S)")
    print("[3] 15 Seconds (15S)")
    print("[4] 30 Seconds (30S)")
    print("[5] 1 Minute (1M)")
    print("[6] 2 Minutes (2M)")
    print("[7] 5 Minutes (5M)")
    print("[8] 15 Minutes (15M)")
    
    timeframe_map = {
        "1": "5 Seconds",
        "2": "10 Seconds",
        "3": "15 Seconds",
        "4": "30 Seconds",
        "5": "1 Minute",
        "6": "2 Minutes",
        "7": "5 Minutes",
        "8": "15 Minutes"
    }
    
    choice = input("\nSelect timeframe (1-8) [Default: 5 (1 Minute)]: ").strip()
    selected_tf = timeframe_map.get(choice, "1 Minute")
    
    analyze_chart(image_filename, selected_tf)

if __name__ == "__main__":
    main()
