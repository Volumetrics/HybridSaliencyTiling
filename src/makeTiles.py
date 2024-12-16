import argparse
import os
from pathlib import Path
from plyfile import PlyData
from timeit import default_timer as timer
from tiling.uniformSize import UniformSize

# Arguments
parser = argparse.ArgumentParser(description="Applies the Hybrid Saliency Tiling technique to a point cloud.")

parser.add_argument("frames", help="The directory where the point cloud frames to tile are located. Only PLY files (.ply) are supported (ASCII or binary).")
parser.add_argument("num_frames", type=int, help="The number of frames per Group of Frames.")
parser.add_argument("directory", help="The directory where to save the tiles. The directory must exist as this script won't create it. The tiles are saved in a binary little endian PLY format.")
parser.add_argument("num_tiles", type=int, help="The number of tiles in each axis.")

args = parser.parse_args()

start = timer()

# Get the frames files
paths = Path(args.frames).rglob("*.ply")

# Make the group of frames and tile the content
gofs = []
c = 0

for path in paths:
    # Load the point cloud
    cloud = PlyData.read(path)

    # Cut the fined-grained tiles in uniform size
    tiler = UniformSize(cloud, args.num_tiles, args.num_tiles, args.num_tiles)
    tiles = tiler.make_tiles()

    # Make the group of frames
    if (c % args.num_frames == 0):
        gofs.append([tiles])
    else:
        gofs[len(gofs) - 1].append(tiles)

    c += 1

# Process the fined grained tiles (not implemented)
# ...

# Save the tiles
i = 0

for gof in gofs:
    for frame in gof:
        j = 0
        for tile in frame:
            file_path = os.path.join(args.directory, f"frame_{i}_tile_{j}.ply")
            
            tile.save(file_path)

            j += 1
    
        i += 1

end = timer()
print("Time elapsed:", end - start)
