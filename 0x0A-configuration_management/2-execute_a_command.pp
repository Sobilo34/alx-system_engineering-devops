# A DSL that execute a command to kill process killmenow

exec { 'pkill -f killmenow':
  path  => 'usr/bin/:/usr/local/bin/:/bin/'
}