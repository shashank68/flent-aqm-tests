(TOTAL_LATENCY, LATENCY_UNIT) = (80, "ms")  # Total Round trip latency

# Client to router Bandwidth will be 10 * Bottleneck bandwidth
(BOTTLENECK_BANDWIDTH, BW_UNIT) = (80, "mbit")

AQM = "fq_pie"  # set at router egress interface
QDELAY_TARGET = "5ms"
ECN = True

TOTAL_NODES_PER_SIDE = 1  # Number of clients

DEBUG_LOGS = True
FLENT_TEST_NAME = "tcp_nup"  # e.g rrul, tcp_nup, cubic_reno, tcp_1up
TCP_CONG_CONTROL = "cubic"

TEST_DURATION = 20
STEP_SIZE = 0.05  # Resolution in seconds
UPLOAD_STREAMS = 1

OFFLOADS = True  # GSO, GRO
OFFLOAD_TYPES = ["gso", "gro", "tso"]


def arg_parser_def(parser):
    parser.add_argument("--rtt", type=int, help="RTT of flows(ms)")
    parser.add_argument(
        "--bottleneck_bw", type=int, help="bottleneck bandwidth (mbit)"
    )
    parser.add_argument("--qdisc", type=str, help="AQM (qdisc) algorithm")
    parser.add_argument("--ecn", type=str, help="ecn flag (Yes / No)")
    parser.add_argument(
        "--no_offloads", type=str, help="Turn off GSO, GRO offloads (Yes / No)"
    )
    parser.add_argument(
        "--number_of_tcp_flows",
        type=int,
        help="Number of flows (tcp_nup flent test)",
    )
    parser.add_argument(
        "--qdelay_target", type=int, help="Queue delay target (For AQM)"
    )