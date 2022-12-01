#!/usr/bin/env ruby
# frozen_string_literal: true

if ARGV.length != 1
  puts "Usage: 01_stars.rb FILE_PATH"
  exit
end

elves = []
count = 0

lines = File.readlines(ARGV[0])

lines.each_with_index do |value, line|
  count += value.to_i
  if value.chomp.empty? || line + 1 == lines.length
    elves.append(count)
    count = 0
  end
end.max

puts "Winner: elf #{elves.index(elves.max) + 1} with #{elves.max} calories"

puts "The top three elves are carrying #{elves.max(3).sum} calories"
