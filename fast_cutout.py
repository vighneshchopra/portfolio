from PIL import Image, ImageFilter
import numpy as np
from collections import deque

def create_cutout(input_path, output_path):
    print("Opening image...")
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    arr = np.array(img, dtype=np.float32)
    rgb = arr[:, :, :3]
    
    # Calculate background mask using flood-fill from borders
    # Corner samples
    corners = [
        rgb[0:15, 0:15],
        rgb[0:15, w-15:w],
        rgb[15:50, 0:15],
        rgb[15:50, w-15:w]
    ]
    bg_sample = np.mean(np.concatenate([c.reshape(-1, 3) for c in corners]), axis=0)
    print("Background studio color estimate:", bg_sample)
    
    # Distance to studio background color
    dist = np.linalg.norm(rgb - bg_sample, axis=2)
    # Background threshold
    is_bg_candidate = (dist < 42) & (rgb[:, :, 0] > 195) & (rgb[:, :, 1] > 195) & (rgb[:, :, 2] > 195)
    
    # Flood-fill BFS from all edges so we never accidentally touch white shirt collar inside!
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()
    
    # Top and side borders
    for x in range(w):
        if is_bg_candidate[0, x]:
            queue.append((0, x))
            visited[0, x] = True
    for y in range(h):
        if is_bg_candidate[y, 0]:
            queue.append((y, 0))
            visited[y, 0] = True
        if is_bg_candidate[y, w-1]:
            queue.append((y, w-1))
            visited[y, w-1] = True
            
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny, nx] and is_bg_candidate[ny, nx]:
                    visited[ny, nx] = True
                    queue.append((ny, nx))
                    
    # Visited is confirmed outer background
    alpha = np.ones((h, w), dtype=np.uint8) * 255
    alpha[visited] = 0
    
    # Soft feathering on edges
    alpha_img = Image.fromarray(alpha, mode='L')
    # Slight blur for smooth hair and jacket edges
    alpha_blurred = alpha_img.filter(ImageFilter.GaussianBlur(radius=1.8))
    
    # Apply alpha
    img.putalpha(alpha_blurred)
    img.save(output_path, "PNG")
    print(f"Saved refined cutout to {output_path}")

create_cutout('profile.png', 'profile_cutout.png')
