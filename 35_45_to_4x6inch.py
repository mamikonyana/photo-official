#!/usr/bin/env python3
"""
Convert a jpg photo of 1x1 crop ratio into a 4x6 inch photo
"""
from __future__ import print_function
import argparse
from PIL import Image

INCH_IN_MM = 25.4


def parse_args(*argument_array):
  parser = argparse.ArgumentParser()
  parser.add_argument('in_photo')
  parser.add_argument('--dpi', type=int, default=240)
  parser.add_argument('--offset', type=int, default=10,
                      help='Margin from top and left for the left-top image')
  parser.add_argument('-o', '--output', required=True,
                      help='Location to save the output photo')
  args = parser.parse_args(*argument_array)
  return args


def main(args):
  new_image = Image.new('RGB', (6 * args.dpi, 4 * args.dpi))
  input_image = Image.open(args.in_photo)

  width = int(35 / INCH_IN_MM * args.dpi)
  height = int(45 / INCH_IN_MM * args.dpi)
  resized_image = input_image.resize((width, height))
  for horizontal in range(3):
    for vertrical in range(2):
       new_image.paste(resized_image,
                       (args.offset + 2 * horizontal * args.dpi,
                        args.offset + 2 * vertrical * args.dpi))
  new_image.save(args.output)


if __name__ == '__main__':
  args = parse_args()
  main(args)
