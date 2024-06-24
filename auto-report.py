require 'rubygems'
require 'mechanize'
require 'colorize'
require 'optparse'
require 'highline/import'

options = {}

puts ''
puts "#{'Quantum'.red} :: #{'Automata'.blue} => http://34.212.135.46/"
puts ''
puts "Created By {\n #{'Cinder'.red} :: #{'Automata'.blue} => https://www.facebook.com/cinderautomata \nThanks For Reference: \n #{'Denny Darmawan'.green} => https://www.facebook.com/denny.darmawan.intra \n}"
puts "This Tool is for those who want to learn about the Mechanize library. #{'Author'.red} May Not #{'Warranty'.red}"
puts ''

class Facebook < Mechanize
  def initialize
    super
    self.user_agent_alias = 'Windows Mozilla'
    self.follow_meta_refresh = true
  end

  def login(email, pass)
    get 'https://www.facebook.com/'
    form_login = page.form_with(method: 'POST') do |form|
      form.email = email
      form.pass = pass
    end.submit
    pp form_login
  end

  def report_someone(ent)
    get "https://m.facebook.com/nfx/basic/question/?context_str={%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22breadcrumbs%22%3A[]%2C%22story_location%22%3A%22profile_someone_else%22%2C%22is_from_feed_tombstone%22%3Afalse%2C%22actions_taken%22%3A%22%22%2C%22is_rapid_reporting%22%3Afalse%2C%22reportable_ent_token%22%3A%22#{ent}%22%2C%22is_impostor%22%3A%22%22}&redirect_uri=%2Fprofile.php%3Fid%3D#{ent}"
    
    form1 = page.forms.first
    form1['a'] = 'b'
    form1.radiobutton_with(value: /account/).check
    form1.submit
    puts 'Report 1 Submitted'
    
    form2 = page.forms.first
    form2['a'] = 'b'
    form2.radiobutton_with(value: /fake/).check
    form2.submit
    puts 'Report 2 Submitted'
    
    form3 = page.forms.first
    form3['a'] = 'b'
    form3.radiobutton_with(value: /REPORT_CONTENT/).check
    form3.submit
    puts 'Review To Facebook'
  end
end

facebook = Facebook.new

parser = OptionParser.new do |opts|
  opts.banner = 'Usage: ruby autoreport-fb.rb [options]'
  
  opts.on('-l', '--login', 'Login Into Facebook') do |l|
    options[:login] = l
  end
  
  opts.on('-p', '--person', 'Report Account') do |p|
    options[:person] = p
  end
  
  opts.on('-h', '--help', 'Show Options') do
    puts opts
    puts ''
    puts 'Example: ruby autoreport-fb.rb --login --person "profile_id" #without quotes'
    puts ''
    exit
  end
end

parser.parse!

if options[:login]
  usr = ask("Enter your username: ") { |q| q.echo = true }
  pwd = ask("Enter your password: ") { |q| q.echo = "*" }
  facebook.login(usr, pwd)
end

if options[:person]
  facebook.report_someone(ARGV[2])
end

