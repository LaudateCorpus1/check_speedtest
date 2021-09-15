#!/usr/bin/python
import argparse
import speedtest


def grab_args() -> object:
    parser = argparse.ArgumentParser(
        description="Runs a speedtest and reports the result in an Icinga2 friendly format.\n" \
                    "Requires speedtest-cli installed.")

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('dw', type=float, help="Download warning level (Mbps)")
    parser.add_argument('dc', type=float, help="Download critical level (Mbps)")
    parser.add_argument('uw', type=float, help="Upload warning level (Mbps)")
    parser.add_argument('uc', type=float, help="Upload critical level (Mbps)")
    parser.add_argument('-s', '--server', type=int, help="Server ID taken from the 'speedtest-cli --list' output")

    return parser.parse_args()


def process_result(results, args):

    #compare
    state = "OK"
    down = results.download
    up = results.upload

    #convert Mbps->bps
    dw = args.dw*1024*1024
    dc = args.dc*1024*1024
    uw = args.uw*1024*1024
    uc = args.uc*1024*1024

    if down < dc or up < uc:
        state = "CRITICAL"
    elif down <dw or up < uw:
        state = "WARNING"

    down = down/1024/1024
    up = up/1024/1024

    out = "{state} - Download = {down:.2f} Mbit/s Upload = {up:.2f} Mbit/s|'download'={down:.2f};{dw:.2f};{dc:.2f} " \
        "'upload'={up:.2f};{uw:.2f};{uc:.2f}".format(state=state, down=down, up=up, dw=args.dw, dc=args.dc, uw=args.uw, uc=args.uc)

    return out


if __name__ == '__main__':
    args = grab_args()

    s = speedtest.Speedtest()

    if args.server is not None:
        s.get_servers([args.server])
    else:
        s.get_best_server()

    s.download()
    s.upload()

    output = process_result(s.results, args)

    print(output)