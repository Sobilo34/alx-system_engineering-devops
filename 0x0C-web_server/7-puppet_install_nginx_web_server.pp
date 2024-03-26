# Configuring your server with Puppet                                                      # Nginx should be listening on port 80


# File: init.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Configure Nginx for redirection
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}
