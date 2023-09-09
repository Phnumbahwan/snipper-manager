#!/usr/bin/env python

import argparse, keyboard

parser = argparse.ArgumentParser(description="Text Snippet Manager")

parser.add_argument("--add", metavar="SNIPPET_NAME", type=str, nargs="?", help="Add a new snippet")
parser.add_argument("--list", action="store_true", help="List all snippets")
parser.add_argument("--remove", metavar="SNIPPET_NAME", type=str, nargs="?", help="Remove a specific snippet")
parser.add_argument("--remove-all", action="store_true", help="Remove all snippets")
snippets = {}

args = parser.parse_args()

hotkey_actions = {}

if args.add:
    snippet_name = args.add.strip()
    
    print(f"Enter the hotkey for '{snippet_name}': ")
    hotkey = ''
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'enter':
                break
            print(event.name)
            hotkey += '+' + event.name if hotkey else event.name

    hotkey_actions[hotkey] = snippet_name

    print(f"Snippet '{snippet_name}' with hotkey '{hotkey}' added successfully.")

if args.remove:
    snippet_name = args.remove
    if snippet_name in snippets:
        del snippets[snippet_name]
        print(f"Snippet '{snippet_name}' removed successfully.")
    else:
        print(f"Snippet '{snippet_name}' not found.")

if args.remove_all:
    snippets.clear()
    print("All snippets removed.")

if args.list:
    print("List of snippets:")
    for hotkey in hotkey_actions:
        print(hotkey)

def execute_action(hotkey):
    if hotkey in hotkey_actions:
        action = hotkey_actions[hotkey]
        print(f"Executing action: '{action}'")
        keyboard.write(action)

for hotkey in hotkey_actions.keys():
    keyboard.add_hotkey(hotkey, execute_action, args=(hotkey,))

keyboard.wait('esc')