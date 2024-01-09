# Pupppet code for modiffying headers
exec { 'update server':
  command  => 'sudo apt-get update',
  user     => 'root',
  provider => 'shell',
}

exec {'install nginx':
   owner => shell,
   command => 'sudo apt-get install nginx',
}

exec {'html':
   owner => shell,
   command => 'sudo echo "Hello World!" > /usr/share/nginx/html/index.html',
}

exec {'var':
   owner => shell,
   command => 'mkdir -p /var/www/html',
}

exec {'404':
   owner => shell,
   command => 'echo "Ceci n'est pas une page" > /var/www/html/custom_404.html',
}

file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}


service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
