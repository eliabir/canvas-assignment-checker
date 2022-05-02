#!/usr/bin/env python3

import os

from dataclasses import dataclass
from canvasapi import Canvas
from datetime import datetime, timedelta
from dotenv import load_dotenv


def main():
    load_dotenv()

    API_URL = os.environ.get("CANVAS_API_URL")
    API_KEY = os.environ.get("CANVAS_API_KEY")

    canvas = Canvas(API_URL, API_KEY)

    events = canvas.get_upcoming_events()

    events_dict = {}

    for event in events:
        if event['type'] == 'assignment':
            if event['context_name'] not in events_dict:
                events_dict[f"{event['context_name']}"] = {}
            events_dict[f"{event['context_name']}"]['title'] = event['title']
            events_dict[f"{event['context_name']}"]['due_date'] = event['end_at']

    print(f"{'='*6} THIS WEEKS ASSIGNMENTS {'='*6}\n")
    for key, value in events_dict.items():
        title_split = key.split()
        due_date = datetime.strptime(value["due_date"], "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=2)
        print(f"=== {title_split[0]} {title_split[2]} ===")
        print(value['title'])
        print(f"Due: {datetime.strftime(due_date, '%A %H:%M %d/%m/%y')}\n")
        #print(f'Due: {parse_time(value["due_date"]).strftime("%A %H:%M %d/%m/%y")}\n')


if __name__ == "__main__":
    main()
