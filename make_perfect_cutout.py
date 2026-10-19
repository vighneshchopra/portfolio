from PIL import Image, ImageFilter
import numpy as np

def generate_perfect_cutout():
    print("Loading profile.png...")
    img = Image.open('profile.png').convert("RGBA")
    w, h = img.size
    arr = np.array(img, dtype=np.uint8)
    rgb = arr[:, :, :3]
    
    # 1. Studio background color sample from top corners
    corners = np.concatenate([
        rgb[0:30, 0:30].reshape(-1, 3),
        rgb[0:30, w-30:w].reshape(-1, 3)
    ])
    bg_color = np.median(corners, axis=0)
    print("Background studio color:", bg_color)
    
    # Distance from background color
    dist = np.linalg.norm(rgb.astype(np.float32) - bg_color, axis=2)
    # Brightness
    lum = rgb.astype(np.float32).mean(axis=2)
    
    # 2. Binary segmentation of person:
    # A pixel is definitively person if:
    # - It is dark (suit/tie/hair) -> lum < 185
    # - It has skin tone / saturation -> dist > 35 or (R > B + 15 and R > G)
    # - It is NOT the studio grey background
    is_person = (dist > 30) | (lum < 185) | (rgb[:, :, 0] > rgb[:, :, 2] + 12)
    
    # 3. Structural constraint: For every row y, the person has a left boundary and a right boundary.
    # Everything strictly between the outermost person pixels on that row is 100% person (shirt, tie, chest)!
    alpha = np.zeros((h, w), dtype=np.uint8)
    
    for y in range(h):
        row_person = np.where(is_person[y])[0]
        if len(row_person) > 0:
            left_bound = row_person[0]
            right_bound = row_person[-1]
            
            # Fill everything between left_bound and right_bound as 100% solid
            alpha[y, left_bound:right_bound+1] = 255
            
    # 4. Refine edges near hair (y < 450) where background might have small noise
    # Smooth alpha mask on boundaries
    alpha_img = Image.fromarray(alpha, mode='L')
    # Use slight Gaussian blur only to prevent hard pixel steps on hair & shoulders
    alpha_smooth = alpha_img.filter(ImageFilter.GaussianBlur(radius=1.2))
    
    # Apply alpha
    img.putalpha(alpha_smooth)
    img.save('profile_cutout.png', "PNG")
    print("Perfect crisp cutout generated!")

generate_perfect_cutout()
