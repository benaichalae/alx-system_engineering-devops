# install flask from pip3

class { 'python3': }

package { 'python3-pip':
  ensure => present,
  require => Class['python3'],
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
