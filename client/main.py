import argparse
import sys
from pathlib import Path
from .client import OratorClient 
from .models import ClientConfig  

def main():
    parser = argparse.ArgumentParser(description='Orator Text-to-Speech Client')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('text', nargs='?', help='Text to convert to speech')
    group.add_argument('-s', '--source', help='Text file to convert to speech')
    
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-p', '--parameter', nargs=2, action='append', 
                       metavar=('NAME', 'VALUE'), help='Set parameter NAME to VALUE')
    parser.add_argument('--server', default='http://localhost:8000',
                       help='Server URL (default: http://localhost:8000)')
    
    args = parser.parse_args()
    
    try:
        config = ClientConfig(server_url=args.server)
        client = OratorClient(config)
        
        if args.parameter:
            for name, value in args.parameter:
                client.set_parameter(name, value)
        
        if args.source:
            if not Path(args.source).exists():
                print(f"Error: File {args.source} does not exist", file=sys.stderr)
                sys.exit(1)
            client.text_file_to_speech(args.source, args.output)
        else:
            client.text_to_speech(args.text, args.output)
    
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()