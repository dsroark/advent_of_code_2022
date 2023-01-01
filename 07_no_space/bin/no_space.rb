#!/usr/bin/env ruby
# frozen_string_literal: true

if ARGV.length != 1
  puts "Usage: #{File.basename(__FILE__)} FILE_PATH"
  exit
end

require 'pry'

##
# this class represents a filesystem
class Filesystem
  attr_reader :directories, :directories_stack

  def initialize()
    @directories_stack = []
    @directories = {}
  end

  def cd(dir)
    if dir == '/'
      path = '/'
    elsif @directories_stack.length == 1
      path = "/#{dir}"
    else
      path = "#{@directories_stack[1, @directories_stack.length()].join}/#{dir}"
    end

    if dir == '..'
      @directories_stack.pop
    else
      @directories_stack.append(path)
    end
  end

  def ls(name = nil, size = '')
    if size == 'dir' || name.nil?
        return nil
    else
      @directories_stack.each do |dir|
        key = dir.to_sym
        if !@directories.key?(key)
          @directories[key] = 0
        end
        @directories[key] += size.to_i
      end
    end
  end

  def search_dir_sizes(threshold, operator)
    matching_dirs = {}
    @directories.each do |dir, size|
      if size.public_send(operator, threshold)
        matching_dirs[dir] = size
      end
    end
    matching_dirs
  end
end

fs = Filesystem.new
cmd = ''

File.readlines(ARGV[0], chomp: true).each do |line|
  args = line.split.reverse
  if args.last == '$'
    args.pop
    cmd = args.pop
  end
  
  fs.send cmd.to_sym, *args
end

total=0
fs.search_dir_sizes(100000, :<=).each do |dir, size|
  total += size
end

puts total
