
# press play ;)

import sys
from pathlib import Path

current_file = Path(__file__)
project_root = current_file.parent.parent
sys.path.insert(0, str(project_root))

from cli.parser import create_parser
from cli.commands import cmd_add, cmd_list, cmd_search, cmd_delete
from cli.menu import run_menu

def main():
    if len(sys.argv) > 1:

        parser = create_parser()    

        args = parser.parse_args()    

    
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

    else:
        run_menu()


if __name__ == "__main__":
    main()
