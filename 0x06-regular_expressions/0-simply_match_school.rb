#!/usr/bin/env ruby

input_string = ARGV[0]

pattern = /School/

matches = input_string.scan(pattern).join

if matches.length > 0
  puts matches
else
  puts ""
end
