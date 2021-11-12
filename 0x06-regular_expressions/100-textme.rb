#!/usr/bin/env ruby
#Simply matching School

puts ARGV[0].scan(/(?<=from:|to:|flags:).*?(?=\])/).join(',')
