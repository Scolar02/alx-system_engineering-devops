# Must use 'exec' and 'pkill'

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
