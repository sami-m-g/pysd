import os
import tempfile
import unittest

import numpy as np

from pysd.core import save_wesbites
from pysd.helpers import FileHelper


class CoreTest(unittest.TestCase):
    def test_save_wesbites(self) -> None:
        websites = ["https://google.com", "https://yahoo.com"]
        temp_file_path = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        np.savetxt(temp_file_path, websites, newline="\n", fmt="%s")
        output_dir = "out"
        args = ["-i", temp_file_path, "-o", output_dir]
        save_wesbites(args)

        for website in websites:
            file_path = FileHelper.get_file_path(output_dir, website)
            self.assertTrue(os.path.exists(file_path))


if __name__ == '__main__':
    unittest.main()