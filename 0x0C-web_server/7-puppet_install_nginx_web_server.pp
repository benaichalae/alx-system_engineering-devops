# Install Nginx web server with Puppet

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

file {'/var/www/html/index.html':
        content => 'Hello World!'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $content,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}

service {'nginx':
        ensure => running,
        require => Package['nginx']
}
