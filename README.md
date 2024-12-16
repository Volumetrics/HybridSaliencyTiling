# Hybrid Saliency Based Tiling

Software that implements the method Hybrid Saliency Based Tiling from [1].

## Installation

1. Install the lastest version of [Python 3.11](https://www.python.org/downloads/) and `pip`
2. Install the required Python packages :
    
    `pip install plyfile`
    
    `pip install numpy`

## Usage

Run the command `python src/makeTiles.py -h` to see details concerning usage.

Example usage :

`python src/makeTiles.py data/ 3 out/ 2`

This will take the frames in the `data` directory, split them in groups of `3`, cut each frame in `2` tiles in each direction and save them in the `out` directory.

## References

[1] J. Li, C. Zhang, Z. Liu, R. Hong, and H. Hu, “Optimal Volumetric Video Streaming With Hybrid Saliency Based Tiling,” IEEE Transactions on Multimedia, vol. 25, pp. 2939–2953, 2023. [Online]. Available : https://ieeexplore.ieee.org/document/9720162/
