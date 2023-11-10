import unittest
import numpy as np

from dtcc_model import Raster


class TestCreateRaster(unittest.TestCase):
    def test_create_empty(self):
        raster = Raster()
        self.assertEqual(raster.crs, "")
        self.assertEqual(raster.bounds.tuple, (0, 0, 0, 0))
        self.assertEqual(raster.georef.to_gdal(), (0, 1, 0, 0, 0, 1))


class TestCopyRaster(unittest.TestCase):
    def test_copy(self):
        raster = Raster()
        raster.data = np.ones((10, 10), dtype=np.uint8)
        raster.crs = "EPSG:3857"

        copy_raster = raster.copy()

        self.assertEqual(copy_raster.data.tolist(), raster.data.tolist())
        self.assertEqual(copy_raster.crs, raster.crs)

    def test_copy_nodata(self):
        raster = Raster()
        raster.data = np.ones((10, 10), dtype=np.uint8)
        raster.crs = "EPSG:3857"

        copy_raster = raster.copy(no_data=True)

        self.assertEqual(copy_raster.data.shape, ())
        self.assertEqual(copy_raster.crs, raster.crs)


if __name__ == "__main__":
    unittest.main()
