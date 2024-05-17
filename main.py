import moviepy.editor as mp

def extract_audio_from_video(video_file: str, output_audio_file: str):
    try:
        # Load the video file
        cvt_video = mp.VideoFileClip(video_file)

        # Extract the audio
        ext_audio = cvt_video.audio

        # Write the audio to a file
        ext_audio.write_audiofile(output_audio_file)

        print("Audio extracted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_file = "Snapchat-1637309829.mp4"  # Ensure the correct file extension is used
    audio_file = "audio_Extracted.mp3"
    extract_audio_from_video(video_file, audio_file)
