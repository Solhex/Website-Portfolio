from website import create_app
import argparse

msg = "Personal portfolio website using flask."
parser = argparse.ArgumentParser(description=msg)

parser.add_argument(
    '-d',
    '--debug',
    action='store_true',
    help='enable debug mode'
)
parser.add_argument(
    '-H',
    '--host',
    type=str,
    default='127.0.0.1',
    help='host to bind to (default: 127.0.0.1)'
)
parser.add_argument(
    '-p',
    '--port',
    type=int,
    default=5000,
    help='port to bind to (default: 5000)'
)

parser.parse_args()
args = parser.parse_args()

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port
    )
