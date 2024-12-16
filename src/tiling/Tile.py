import numpy
from plyfile import PlyData, PlyElement

class Tile:
    """A tile of a point cloud"""

    def __init__(self, points:numpy.ndarray, x:float, y:float, z:float, x_size:float, y_size:float, z_size:float) -> None:
        """Constructor

        Args:
            points (numpy.ndarray): The points of this tile
            x (float): The tile's center x coordinate
            y (float): The tile's center y coordinate
            z (float): The tile's center z coordinate
            x_size (float): The size of the x-axis of the tile
            y_size (float): The size of the y-axis of the tile
            z_size (float): The size of the z-axis of the tile
        """
        self.points = points
        self.x = x
        self.y = y
        self.z = z
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size

    def save(self, path:str) -> None:
        """Saves this tile as a PLY file.

        Args:
            path (str): The path where to save the tile with the extension
        """
        element = PlyElement.describe(self.points, "vertex")
            
        PlyData([element]).write(path)
