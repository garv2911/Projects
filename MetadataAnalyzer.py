import os
import exifread
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

def analyze_image_metadata(image_path):
    """Extract metadata from an image (JPEG, PNG)"""
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
        
        print("\n🔹 Image Metadata:")
        for tag, value in tags.items():
            print(f"{tag}: {value}")
        
        img = Image.open(image_path)
        print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")

    except Exception as e:
        print(f"Error reading image metadata: {e}")

def analyze_audio_metadata(audio_path):
    """Extract metadata from an audio file (MP3, MP4)"""
    try:
        if audio_path.lower().endswith(".mp3"):
            audio = MP3(audio_path)
        elif audio_path.lower().endswith(".mp4"):
            audio = MP4(audio_path)
        else:
            print("Unsupported audio format")
            return
        
        print("\n🔹 Audio Metadata:")
        for key, value in audio.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error reading audio metadata: {e}")

def analyze_file(file_path):
    """Detect file type and analyze metadata"""
    if not os.path.exists(file_path):
        print("File does not exist!")
        return
    
    extension = os.path.splitext(file_path)[-1].lower()
    
    if extension in [".jpg", ".jpeg", ".png"]:
        analyze_image_metadata(file_path)
    elif extension in [".mp3", ".mp4"]:
        analyze_audio_metadata(file_path)
    else:
        print("Unsupported file type")


