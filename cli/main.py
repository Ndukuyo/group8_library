  
# press play ;)

import sys
from pathlib import Path

# adding parent directory so we get access to the team work

sys.path.insert(0, str(Path(__file__).parent.parent))

from cli.parser import create_parser
from cli.commands import cmd_add, cmd_list, cmd_search, cmd_delete

def main():
    # enrty point, runs when you start the program 

    parser = create_parser()    #create parser with all commands

    args = parser.parse_args()      #parse command line arguments

     #find which command was used
    if args.command == "add":
        cmd_add(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "delete":
        cmd_delete(args)
    else:
        print(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
               