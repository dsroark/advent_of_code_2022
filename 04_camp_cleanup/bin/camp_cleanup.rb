#!/usr/bin/env ruby
# frozen_string_literal: true

if ARGV.length != 1
  puts "Usage: #{File.basename(__FILE__)} FILE_PATH"
  exit
end
lines = File.readlines(ARGV[0])

sections = lines.map do |line|
  line.chomp.split(',').map do |assign|
    assign.split '-'
  end
end

number_of_overlaps = 0
any_overlaps = 0
sections.each do |section|
  a1 = section[0].map(&:to_i)
  a2 = section[1].map(&:to_i)

  if (a1.first >= a2.first && a1.last <= a2.last) || (a2.first >= a1.first && a2.last <= a1.last)
    number_of_overlaps += 1
  end
  if (a1.first <= a2.last) && (a2.first <= a1.last)
    any_overlaps += 1
  end
end

puts number_of_overlaps
puts any_overlaps
