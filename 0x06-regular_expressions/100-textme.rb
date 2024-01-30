#!/usr/bin/env ruby
# This script should print: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
