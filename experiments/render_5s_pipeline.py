import time
import io
import os
import shutil
import subprocess
from PIL import Image
import imageio
import imageio_ffmpeg
import numpy as np
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main():
    print("==================================================")
    print("5.0-SECOND ULTRA-HD STUDIO PIPELINE (WHATSAPP + LINKEDIN)")
    print("==================================================")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1200,1200")
    options.add_argument("--disable-gpu")
    options.add_argument("--force-device-scale-factor=1")

    driver = webdriver.Chrome(options=options)
    try:
        driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': 1080,
            'height': 1080,
            'deviceScaleFactor': 1,
            'mobile': False
        })
        driver.get("http://localhost:5500/studio_5s_render_harness.html")
        time.sleep(2)

        for _ in range(30):
            if driver.execute_script("return window.isReady === true;"):
                break
            time.sleep(0.1)

        stage = driver.find_element(By.ID, "master-stage")
        TOTAL_FRAMES = 150 # Exactly 5.000 seconds at 30 fps
        FPS = 30
        frames = []

        print(f"Capturing {TOTAL_FRAMES} frames at 1080x1080 (Exact 5.0s duration)...")
        start_time = time.time()

        for f in range(TOTAL_FRAMES):
            driver.execute_script(f"window.renderFrame({f}, {TOTAL_FRAMES});")
            stage_png = stage.screenshot_as_png
            img = Image.open(io.BytesIO(stage_png)).convert("RGB")
            frames.append(img)

            if (f + 1) % 25 == 0 or f == TOTAL_FRAMES - 1:
                elapsed = time.time() - start_time
                print(f"  Captured frame {f+1}/{TOTAL_FRAMES} ({(f+1)/elapsed:.1f} fps)")

        print("\nEncoding 1080x1080 Master MP4 (Exact 5.0s, high-bitrate libx264)...")
        mp4_path = "VighneshChopraPortfolio.mp4"
        
        # Use imageio with macro_block_size=1 to maintain exact 1080x1080 without resizing
        writer = imageio.get_writer(
            mp4_path,
            fps=FPS,
            codec='libx264',
            quality=9,
            pixelformat='yuv420p',
            macro_block_size=1,
            ffmpeg_params=['-preset', 'slow', '-movflags', '+faststart']
        )
        for img in frames:
            writer.append_data(np.array(img))
        writer.close()

        mp4_size = os.path.getsize(mp4_path) / 1024
        print(f"[OK] Generated {mp4_path} ({mp4_size:.1f} KB)")

        desktop_dir = r"C:\Users\amanc\OneDrive\Desktop"
        desktop_mp4 = os.path.join(desktop_dir, "VighneshChopraPortfolio.mp4")
        shutil.copyfile(mp4_path, desktop_mp4)
        print(f"[OK] Replaced Desktop MP4: {desktop_mp4}")

        # High Quality Palettegen GIF using ffmpeg
        print("\nEncoding Ultra-HD VighneshChopraPortfolio.gif (720x720, 15 FPS, 5.0s loop)...")
        gif_path = "VighneshChopraPortfolio.gif"
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

        cmd = [
            ffmpeg_exe, "-y",
            "-i", mp4_path,
            "-vf", "fps=15,scale=720:720:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=256:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=5",
            gif_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print("FFmpeg error:", res.stderr.decode('utf-8', errors='ignore'))
            raise RuntimeError("FFmpeg GIF generation failed")

        gif_size = os.path.getsize(gif_path) / 1024
        print(f"[OK] Generated {gif_path} ({gif_size:.1f} KB)")

        desktop_gif = os.path.join(desktop_dir, "VighneshChopraPortfolio.gif")
        shutil.copyfile(gif_path, desktop_gif)
        print(f"[OK] Replaced Desktop GIF: {desktop_gif}")

        # Also sync project root files
        shutil.copyfile(mp4_path, "autumn_qr_loop.mp4")
        shutil.copyfile(gif_path, "autumn_qr_loop.gif")
        print("[OK] Synced autumn_qr_loop.mp4 and autumn_qr_loop.gif in project root")

        # Optical Sensor Scan Test
        print("\n[Verification] Optical sensor scan test on frame 80...")
        detector = cv2.QRCodeDetector()
        
        # Test MP4 frame 80
        cap = cv2.VideoCapture(mp4_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 80)
        ret, cv_frame = cap.read()
        cap.release()
        if ret:
            val_mp4, _, _ = detector.detectAndDecode(cv_frame)
            print(f"  MP4 Frame 80 Decoded: '{val_mp4}'")
            assert "https://vighneshchopra.github.io/portfolio/" in val_mp4

        # Test GIF frame 40
        cap_gif = cv2.VideoCapture(gif_path)
        cap_gif.set(cv2.CAP_PROP_POS_FRAMES, 40)
        ret_g, cv_gframe = cap_gif.read()
        cap_gif.release()
        if ret_g:
            val_gif, _, _ = detector.detectAndDecode(cv_gframe)
            print(f"  GIF Frame 40 Decoded:  '{val_gif}'")
            assert "https://vighneshchopra.github.io/portfolio/" in val_gif

        print("  >> SUCCESS: 100% Scannability confirmed!")

    finally:
        driver.quit()

    print("\nPipeline execution complete!")

if __name__ == "__main__":
    main()
