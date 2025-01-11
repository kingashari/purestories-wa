import subprocess
import os

def convert_to_purestatus_format(input_file, output_file):
    """
    Convert a video file to PureStatus-like format (MP4 with H.264, reduced bitrate and resolution).

    Parameters:
    - input_file (str): Path to the input MOV file.
    - output_file (str): Path to save the converted MP4 file.
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return

        # FFmpeg command to convert video
        command = [
            "ffmpeg",
            "-i", input_file,               # Input file
            "-vf", "scale=1080:1920",       # Resize to 1080x1920 (portrait)
            "-r", "29.97",                 # Set frame rate to 29.97 FPS
            "-b:v", "4M",                  # Set video bitrate to 4 Mbps
            "-c:v", "libx264",             # Use H.264 codec for video
            "-preset", "fast",             # Use fast preset for encoding
            "-c:a", "aac",                 # Use AAC codec for audio
            "-b:a", "128k",                # Set audio bitrate to 128 kbps
            "-strict", "experimental",     # Allow experimental features if needed
            output_file                      # Output file
        ]

        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion successful! Saved as '{output_file}'.")

    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
    except Exception as e:
        print("Unexpected error:", e)

# Example usage
if __name__ == "__main__":
    input_mov_file = r"C:\Users\kingashari\Pictures\tes\3.MOV"   # Replace with the path to your input MOV file
    output_mp4_file = "output3.1.mp4"  # Replace with the desired output MP4 file name

    convert_to_purestatus_format(input_mov_file, output_mp4_file)
