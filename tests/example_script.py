from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter

def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="No description.",
        epilog="No epilog.",
    )
    parser.add_argument(
        "-a",
        "--argument_1",
    )
    parser.add_argument(
        "-b",
        "--argument_2",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print("This is an example script.")