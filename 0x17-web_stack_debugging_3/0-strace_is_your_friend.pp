# 0-strace_is_your_friend.pp

$file_to_edit = '/var/www/html/wp-settings.php'

# Define an exec resource to replace the line in the file
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep -q 'phpp' ${file_to_edit}", # Only execute if the line exists
}
