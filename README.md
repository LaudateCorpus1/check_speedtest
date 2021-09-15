## check_speedtest.py
A basic python script to run a speed test and output in an Icinga friendly format. Requires speedtest-cli to be installed, see https://github.com/sivel/speedtest-cli for installation process.

## Usage
    usage: check_speedtest.py [-h] [--version] [-s SERVER] dw dc uw uc
    
    Runs a speedtest and reports the result in an Icinga2 friendly format. Requires speedtest-cli installed.
    
    positional arguments:
      dw                    Download warning level (Mbps)
      dc                    Download critical level (Mbps)
      uw                    Upload warning level (Mbps)
      uc                    Upload critical level (Mbps)

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -s SERVER, --server SERVER
                            Server ID taken from the 'speedtest-cli --list' output