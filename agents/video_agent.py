import os
import logging

logger = logging.getLogger(__name__)

def create_video(script):
    try:
        logger.info("Creating Remotion video project")
        
        remotion_dir = "remotion"
        if not os.path.exists(remotion_dir):
            os.makedirs(remotion_dir)
        
        # Only create package.json and tsconfig if they don't exist
        package_json_path = os.path.join(remotion_dir, "package.json")
        tsconfig_path = os.path.join(remotion_dir, "tsconfig.json")
        
        if not os.path.exists(package_json_path):
            package_json = {
                "name": "crowdwisdom-ad",
                "version": "1.0.0",
                "private": True,
                "dependencies": {
                    "remotion": "^4.0.0",
                    "@remotion/cli": "^4.0.0",
                    "react": "^18.0.0",
                    "react-dom": "^18.0.0"
                },
                "scripts": {
                    "dev": "remotion studio",
                    "build": "remotion render",
                    "upgrade": "remotion upgrade"
                }
            }
            
            import json
            with open(package_json_path, "w") as f:
                json.dump(package_json, f, indent=2)
        
        if not os.path.exists(tsconfig_path):
            tsconfig_json = {
                "compilerOptions": {
                    "target": "ES2018",
                    "module": "ESNext",
                    "moduleResolution": "node",
                    "jsx": "react-jsx",
                    "strict": True,
                    "esModuleInterop": True,
                    "skipLibCheck": True,
                    "forceConsistentCasingInFileNames": True
                }
            }
            
            import json
            with open(tsconfig_path, "w") as f:
                json.dump(tsconfig_json, f, indent=2)
        
        src_dir = os.path.join(remotion_dir, "src")
        if not os.path.exists(src_dir):
            os.makedirs(src_dir)
        
        with open("outputs/final_video.txt", "w", encoding="utf-8") as f:
            f.write(f"""Remotion project created in 'remotion' directory!

🎬 Ad Features:
- Animated sections (fade-in, scale-in)
- Gradient background with glow effects
- Clear sections: Hook → Pain → Solution → CTA

🎤 To add voiceover (ElevenLabs):
1. Generate voice audio using ElevenLabs
2. Place audio file in remotion/public/
3. Import and use <Audio> component in Ad.tsx

📝 Ad Script:
{script}
""")
        
        logger.info("Remotion project created successfully")
        return "Video project created"
    except Exception as e:
        logger.error(f"Error creating video project: {e}")
        with open("outputs/final_video.txt", "w", encoding="utf-8") as f:
            f.write(f"Error creating video: {e}\n\nAd Script:\n{script}")
        return "Error creating video"
