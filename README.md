# purestories for whatsaap

This script processes an MOV video file using FFmpeg to convert it into an MP4 format with specific metadata and compression settings. It mimics the compression output of PureStatus for better compatibility and smaller file sizes while preserving essential video quality.

## Features

- Converts MOV video files to MP4 format.
- Adjusts metadata and compression settings to align with PureStatus output.
- Ensures compatibility with social media platforms and optimized file sizes.

## Prerequisites

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install FFmpeg. You can download it from [ffmpeg.org](https://ffmpeg.org/). Ensure the FFmpeg binary is added to your system's PATH.

## How to Use

1. Place your MOV video file in a known directory.
2. Update the `input_mov_file` and `output_mp4_file` variables in the script with the respective file paths.
3. Run the script using Python:

```bash
python script_name.py
```

## Script Explanation

```python
import subprocess

# Specify the input MOV file path
input_mov_file = "C:/path/to/your/input_file.mov"  # Replace with the actual path to your MOV file

# Specify the output MP4 file path
output_mp4_file = "C:/path/to/your/output_file.mp4"  # Replace with the desired path for the output MP4 file

# FFmpeg command for converting MOV to MP4 with specific compression settings
command = [
    "ffmpeg",
    "-i", input_mov_file,           # Input file
    "-c:v", "libx264",            # Video codec: H.264
    "-crf", "23",                 # Constant Rate Factor (adjusts quality/compression)
    "-preset", "medium",          # Compression speed preset
    "-c:a", "aac",                # Audio codec: AAC
    "-b:a", "128k",               # Audio bitrate
    "-pix_fmt", "yuv420p",        # Pixel format
    output_mp4_file                  # Output file
]

# Execute the FFmpeg command
try:
    subprocess.run(command, check=True)
    print("Conversion successful! Output file saved at:", output_mp4_file)
except subprocess.CalledProcessError as e:
    print("An error occurred during the conversion:", e)
```

### Detailed Steps

1. **Input and Output Paths**
   - `input_mov_file`: Path to the source MOV file.
   - `output_mp4_file`: Path where the converted MP4 file will be saved.

2. **FFmpeg Command**
   - `-i`: Specifies the input file.
   - `-c:v libx264`: Uses H.264 for video compression.
   - `-crf 23`: Sets the quality level (lower values mean better quality but larger file size).
   - `-preset medium`: Balances compression speed and efficiency.
   - `-c:a aac`: Compresses audio using AAC.
   - `-b:a 128k`: Sets the audio bitrate.
   - `-pix_fmt yuv420p`: Ensures compatibility with most players.

3. **Error Handling**
   - The `subprocess.run` function executes the FFmpeg command. If the command fails, an error message is printed.

## Example

If your MOV file is located at `C:/Videos/input.mov`, and you want the output file at `C:/Videos/output.mp4`, update the script as follows:

```python
input_mov_file = "C:/Videos/input.mov"
output_mp4_file = "C:/Videos/output.mp4"
```

Then, run the script. If successful, the converted file will be saved as `output.mp4`.

## Notes

- The script assumes FFmpeg is installed and available in the system's PATH. If not, provide the full path to the FFmpeg executable.
- Adjust the CRF value if needed. For better quality, use a lower value (e.g., 18). For smaller file sizes, use a higher value (e.g., 28).

---

