from website import create_app
import argparse

msg = "Enable debug mode in your Flask application"
parser = argparse.ArgumentParser(description=msg)

parser.add_argument(
    '-d',
    '--debug',
    action='store_true',
    help='Enable debug mode')
parser.add_argument(
    '-H',
    '--host',
    default='0.0.0.0',
    help='Host to bind to')
parser.add_argument(
    '-p',
    '--port',
    type=int,
    default=5000,
    help='Port to bind to')

parser.parse_args()
args = parser.parse_args()

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port)


