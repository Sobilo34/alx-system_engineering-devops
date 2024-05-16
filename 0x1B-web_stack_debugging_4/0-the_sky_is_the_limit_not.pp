# Increase the maximum number of connections an Nginx server can handle
# Increases the maximum number of connections from the default value of 15 to 4096

exec { 'ngix-conf':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx to apply the configuration changes
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
