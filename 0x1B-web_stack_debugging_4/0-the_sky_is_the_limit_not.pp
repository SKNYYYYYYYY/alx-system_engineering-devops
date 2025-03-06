# Increase the ULIMIT for Nginx
file_line { 'nginx_ulimit':
  ensure => present,
  path   => '/etc/default/nginx',
  line   => 'ULIMIT="-n 4096"',
  match  => '^ULIMIT="-n \d+"',
  notify => Service['nginx'],
}

# Manage Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}