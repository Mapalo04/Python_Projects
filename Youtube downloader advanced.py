from pytube import YouTube
from pytube.cli import on_progress
import os
from datetime import datetime
from tqdm import tqdm

def custom_progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    
    # Update tqdm progress bar if you prefer that over the CLI progress
    # Or use print statements for simple progress
    print(f"\r📥 Downloading: {percentage:.1f}% complete", end='', flush=True)


def download_with_progress():
    try:
        # Get YouTube URL from user
        link = input("Enter the YouTube URL: ").strip()
        
        if not link:
            print("❌ No URL provided. Exiting.")
            return
        
        print("🔍 Connecting to YouTube...")
        
        # Create YouTube object with progress callback
        video = YouTube(link, on_progress_callback=on_progress)
        
        # Display video information
        print(f"\n📹 Video Title: {video.title}")
        print(f"👤 Channel: {video.author}")
        print(f"⏱️ Duration: {video.length} seconds")
        print(f"📊 Views: {video.views:,}")
        
        # Get available streams and let user choose
        print("\n📋 Available resolutions:")
        streams = video.streams.filter(progressive=True, file_extension='mp4')
        
        for i, stream in enumerate(streams):
            print(f"{i+1}. {stream.resolution} ({stream.mime_type}) - {stream.filesize_mb:.1f}MB")
        
        # Let user choose resolution or use lowest as default
        choice = input("\nEnter choice number (or press Enter for lowest resolution): ").strip()
        
        if choice and choice.isdigit():
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(streams):
                stream = streams[choice_idx]
            else:
                print("❌ Invalid choice. Using lowest resolution.")
                stream = video.streams.get_lowest_resolution()
        else:
            stream = video.streams.get_lowest_resolution()
            print(f"✅ Selected: {stream.resolution}")
        
        # Create downloads directory if it doesn't exist
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)
        
        print(f"\n⬇️ Downloading: {video.title}")
        print(f"📁 Saving to: {download_dir}/")
        print("⏳ Download progress:")
        
        # Start download with timestamp
        start_time = datetime.now()
        file_path = stream.download(output_path=download_dir)
        
        # Calculate download time
        end_time = datetime.now()
        download_time = (end_time - start_time).total_seconds()
        
        # Get file size
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
        
        print(f"\n✅ Download completed!")
        print(f"📊 File size: {file_size:.2f} MB")
        print(f"⏱️ Download time: {download_time:.2f} seconds")
        print(f"📁 Saved as: {os.path.basename(file_path)}")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Please check the URL and try again.")

if __name__ == "__main__":
    print("🎵 YouTube Video Downloader")
    print("=" * 30)
    
    while True:
        download_with_progress()
        
        # Ask if user wants to download another video
        another = input("\nDo you want to download another video? (y/n): ").lower()
        if another not in ['y', 'yes']:
            print("👋 Goodbye!")
            break
        print("\n" + "=" * 30)