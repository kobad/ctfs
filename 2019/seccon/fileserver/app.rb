require 'erb'
require 'webrick'
require 'fileutils'
require 'securerandom'

include WEBrick::HTTPStatus

FileUtils.rm_rf('/tmp/flags')
FileUtils.mkdir_p('/tmp/flags')
FileUtils.cp('flag.txt', "/tmp/flags/#{SecureRandom.alphanumeric(32)}.txt")
# FileUtils.rm('flag.txt')

server = WEBrick::HTTPServer.new Port: 9292

def is_bad_path(path)
  bad_char = nil

  %w(* ? [ { \\).each do |char|
    if path.include? char
      bad_char = char
      break
    end
  end

  if bad_char.nil?
    false
  else
    # check if brackets are paired
    # 閉じられた{}, []があるとダメ
    puts "bad char"
    puts bad_char
    if bad_char == ?{
      puts path[path.index(bad_char)..].include? ?}
      path[path.index(bad_char)..].include? ?}
    elsif bad_char == ?[
      path[path.index(bad_char)..].include? ?]
    else
      true
    end
  end
end

server.mount_proc '/' do |req, res|
  raise BadRequest if is_bad_path(req.path)

  if req.path.end_with? '/'
    puts "--- end / ---"
    if req.path.include? '.'
      raise BadRequest
    end

    files = Dir.glob(".#{req.path}*")
    puts "---"
    puts files
    res['Content-Type'] = 'text/html'
    res.body = ERB.new(File.read('index.html.erb')).result(binding)
    next
  end

  matches = Dir.glob(req.path[1..])

  if matches.empty?
    raise NotFound
  end

  begin
    puts "--- read file ---"
    file = File.open(matches.first, 'rb')
    puts File.extname(req.path)[1..]
    res['Content-Type'] = server.config[:MimeTypes][File.extname(req.path)[1..]]
    res.body = file.read(1e6)
  rescue Errno::EISDIR => e
    res.set_redirect(MovedPermanently, req.path + '/')
  end
end

trap 'INT' do server.shutdown end

server.start
