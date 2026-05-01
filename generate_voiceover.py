from gtts import gTTS
from mutagen.mp3 import MP3
import os
import json

def generate_voiceover():
    sections = {
        "hook": "Stop losing money in trading!",
        "pain": "Tired of guessing and losing? Spending hours on chart analysis. Missing opportunities. Watching your profits disappear.",
        "solution": "CrowdWisdom Trading. AI-powered signals give you real-time insights. Save time. Maximize profits.",
        "cta": "Get started today at crowdwisdomtrading.com!"
    }
    
    public_dir = os.path.join("remotion", "public")
    durations = {}
    
    for name, text in sections.items():
        tts = gTTS(text=text, lang='en', slow=False)
        output_path = os.path.join(public_dir, f"{name}.mp3")
        tts.save(output_path)
        
        # Get audio duration in seconds and convert to frames (30 fps)
        audio = MP3(output_path)
        duration_sec = audio.info.length
        duration_frames = int(duration_sec * 30)
        durations[name] = duration_frames
        
        print(f"Generated: {output_path} (duration: {duration_sec:.2f}s = {duration_frames} frames)")
    
    # Save durations to JSON file in public directory
    durations_path = os.path.join(public_dir, "durations.json")
    with open(durations_path, "w") as f:
        json.dump(durations, f, indent=2)
    
    print(f"\nDurations saved to: {durations_path}")
    print("\nAll voiceovers generated successfully!")

if __name__ == "__main__":
    generate_voiceover()
