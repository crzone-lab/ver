import zlib, struct, glob, collections

def flood_fill_nukki(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    pos = 8
    width = height = bit_depth = color_type = 0
    idat_data = bytearray()
    
    while pos < len(data):
        length, chunk_type = struct.unpack('>I4s', data[pos:pos+8])
        chunk_body = data[pos+8:pos+8+length]
        if chunk_type == b'IHDR':
            width, height, bit_depth, color_type = struct.unpack('>IIBB', chunk_body[:10])
        elif chunk_type == b'IDAT':
            idat_data.extend(chunk_body)
        elif chunk_type == b'IEND':
            break
        pos += 12 + length

    if color_type != 6:
        print(f'Skipping {filepath}: not RGBA')
        return

    raw = zlib.decompress(idat_data)
    stride = width * 4 + 1
    
    # Extract raw 2D RGBA array
    pixels = []
    for r in range(height):
        row_bytes = bytearray(raw[r * stride + 1 : (r + 1) * stride])
        row_pixels = []
        for c in range(width):
            idx = c * 4
            row_pixels.append([row_bytes[idx], row_bytes[idx+1], row_bytes[idx+2], row_bytes[idx+3]])
        pixels.append(row_pixels)

    # High-Precision BFS Flood Fill from 4 Outer Corners
    visited = set()
    queue = collections.deque()

    # Seed 4 corners and entire outer border perimeter
    for c in range(width):
        queue.append((0, c))
        queue.append((height - 1, c))
    for r in range(height):
        queue.append((r, 0))
        queue.append((r, width - 1))

    def is_white_paper(r, c):
        p = pixels[r][c]
        # Check if pixel is white / light background paper (R>200, G>200, B>200)
        return p[0] > 200 and p[1] > 200 and p[2] > 200

    nukki_count = 0
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if is_white_paper(r, c):
            pixels[r][c][3] = 0 # Make outer paper 100% transparent!
            nukki_count += 1

            # Check 4 neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in visited:
                    if is_white_paper(nr, nc):
                        queue.append((nr, nc))

    # Re-pack raw PNG bytes
    new_raw = bytearray()
    for r in range(height):
        new_raw.append(raw[r * stride]) # preserve filter byte
        for c in range(width):
            p = pixels[r][c]
            new_raw.extend(p)

    new_idat = zlib.compress(new_raw)
    header = data[:8]
    ihdr_chunk = data[8:33]
    idat_len = len(new_idat)
    idat_header = struct.pack('>I4s', idat_len, b'IDAT')
    idat_crc = struct.pack('>I', zlib.crc32(b'IDAT' + new_idat) & 0xffffffff)
    iend_chunk = struct.pack('>I4s', 0, b'IEND') + struct.pack('>I', zlib.crc32(b'IEND') & 0xffffffff)
    
    with open(filepath, 'wb') as f:
        f.write(header + ihdr_chunk + idat_header + new_idat + idat_crc + iend_chunk)
    
    print(f'100% Precision Flood-Fill Nukki Completed on {filepath}: {nukki_count} outer paper pixels made transparent!')

# ONLY PROCESS THE 4 RABBIT FILES INSTRUCTED BY USER!
rabbit_files = ['deco_sprites/01.png', 'deco_sprites/02.png', 'deco_sprites/03.png', 'deco_sprites/04.png']
for rf in rabbit_files:
    flood_fill_nukki(rf)
