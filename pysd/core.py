import argparse
import sys

from pysd.helpers import DriverHelper, FileHelper


def save_wesbites(args: list[str]) -> None:
    parser = argparse.ArgumentParser(description="Loop over a list of websites and take screenshots.")
    parser.add_argument("-i", "--input_file", help="Input file with the list of websites.",  type=str, default="data/websites.txt")
    parser.add_argument("-o", "--output_dir", help="Output directory for the screenshots.", type=str, default="out/")
    parsed_args = parser.parse_args(args)

    websites = FileHelper.get_websites(parsed_args.input_file)
    driver_helper = DriverHelper()
    driver_helper.save_websites_screenshots(websites, parsed_args.output_dir)


if __name__ == "__main__":
    save_wesbites(sys.argv[1:]) #pragma: no cover