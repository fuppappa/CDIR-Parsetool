import Evtx.Evtx as evtx
import Evtx.Views as e_views


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Dump a binary EVTX file into XML.")
    parser.add_argument("evtx", type=str,
                        help="Path to the Windows EVTX event log file")
    args = parser.parse_args()

    with evtx.Evtx(args.evtx) as log:
        record_buf = e_views.XML_HEADER
        record_buf += "<Events>"
        for record in log.records():
            r = record.xml()
            record_buf += record.xml()
        record_buf += "<Events>"


if __name__ == "__main__":
    main()
