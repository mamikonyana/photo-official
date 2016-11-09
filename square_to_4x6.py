#!/usr/bin/env python3
"""
Convert a jpg photo of 1x1 crop ratio into a 4x6 inch photo
"""
from __future__ import print_function
import argparse
from PIL import Image


def parse_args(*argument_array):
  parser = argparse.ArgumentParser()
  parser.add_argument('in_photo')
  parser.add_argument('--dpi', type=int, default=240)
  parser.add_argument('-o', '--output',
                      help='Location to save the output photo')
  args = parser.parse_args(*argument_array)
  return args


def main(args):
  new_image = Image.new('RGB', (6 * args.dpi, 4 * args.dpi))
  input_image = Image.open(args.in_photo)
  resized_image = input_image.resize((2 * args.dpi, 2 * args.dpi))
  for horizontal in range(3):
    for vertrical in range(2):
       new_image.paste(resized_image,
                       (2 * horizontal * args.dpi, 2 * vertrical * args.dpi))
  new_image.save(args.output)


if __name__ == '__main__':
  args = parse_args()
  main(args)
