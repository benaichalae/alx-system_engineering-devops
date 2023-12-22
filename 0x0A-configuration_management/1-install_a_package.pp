# Installs flask from pip3

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => true,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_flask'],
}

