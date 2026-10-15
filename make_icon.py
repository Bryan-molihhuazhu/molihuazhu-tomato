from PIL import Image, ImageDraw
import math

S = 256
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# 番茄主体（带一点高光的红色圆，略扁）
cx, cy = S // 2, int(S * 0.56)
rx, ry = int(S * 0.40), int(S * 0.36)
# 底色阴影
d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(200, 40, 30, 255))
# 主体渐变感：叠一层更亮
d.ellipse([cx - rx + 6, cy - ry + 6, cx + rx - 6, cy + ry - 6], fill=(232, 70, 52, 255))
# 高光
hl = Image.new("RGBA", (S, S), (0, 0, 0, 0))
hd = ImageDraw.Draw(hl)
hd.ellipse([cx - int(rx * 0.55), cy - int(ry * 0.7), cx - int(rx * 0.05), cy - int(ry * 0.1)],
           fill=(255, 255, 255, 120))
img = Image.alpha_composite(img, hl)

# 绿色蒂叶（顶部五角星状）
leaf = ImageDraw.Draw(img)
gx, gy = cx, int(cy - ry + 4)
leaf_colors = [(76, 175, 80, 255), (60, 150, 64, 255)]
for i, ang in enumerate(range(0, 360, 72)):
    a = math.radians(ang - 90)
    x2 = gx + math.cos(a) * (rx * 0.42)
    y2 = gy + math.sin(a) * (ry * 0.42)
    x3 = gx + math.cos(a + math.radians(36)) * (rx * 0.18)
    y3 = gy + math.sin(a + math.radians(36)) * (ry * 0.18)
    x4 = gx + math.cos(a - math.radians(36)) * (rx * 0.18)
    y4 = gy + math.sin(a - math.radians(36)) * (ry * 0.18)
    leaf.polygon([(gx, gy), (x2, y2), (x3, y3), (x4, y4)],
                 fill=leaf_colors[i % 2])
# 小梗
leaf.rectangle([gx - 5, gy - int(ry * 0.5), gx + 5, gy + 6], fill=(56, 120, 50, 255))

# 生成多尺寸 .ico
sizes = [16, 24, 32, 48, 64, 128, 256]
frames = []
for sz in sizes:
    frames.append(img.resize((sz, sz), Image.LANCZOS))
out = r"C:\Users\Bryan\Desktop\番茄钟\tomato.ico"
img.save(out, sizes=[(s, s) for s in sizes])
print("saved", out)
print("ico frames:", [f.size for f in frames])
