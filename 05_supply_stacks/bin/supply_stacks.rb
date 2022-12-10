#!/usr/bin/env ruby
# frozen_string_literal: true

# blatant copy from SO
def number_or_nil(string)
  Integer(string || '')
rescue ArgumentError
  nil
end

if ARGV.length != 1
  puts "Usage: #{File.basename(__FILE__)} FILE_PATH"
  exit
end

lines = File.readlines(ARGV[0], chomp: true)

raw_stacks = lines.take(lines.index("") - 1)
raw_instructions = lines.drop(lines.index("")+1)
require 'pry'

stacks_reversed = raw_stacks.map do |row|
  row.split('').drop(1).reject.with_index { |i, ix| ix % 4 != 0 }
end.transpose.map(&:reverse)

stacks = stacks_reversed.map do |r|
  r.reject { |p| p == ' ' }
end

instructions = raw_instructions.map do |i|
  i.split.select { |c| number_or_nil(c).is_a? Integer }
end

instructions.each do |i|
  num_crates = i[0].to_i
  from = i[1].to_i - 1
  to = i[2].to_i - 1

  num_crates.times do
    crate = stacks[from].pop
    stacks[to].append(crate)
  end
end

stacks.each do |stack|
  print stack.last
end
print "\n"
