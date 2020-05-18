from parser import setup_parser
from actions import Actions

DEBUG=False


def main():
    if DEBUG:
        import pdb; pdb.set_trace()
    parser = setup_parser()
    opts = parser.parse_args()
    func = opts.argument[0]
    s = Actions()
    s.indirect(func, opts.value[0])

main()
