# Pomodoro CLI

A simple Pomodoro timer with session tracking and stats.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pomodoro-cli.git
   cd pomodoro-cli
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.json` file to set your preferred Pomodoro session lengths:

```json
{
    "work_length": 25,
    "short_break": 5,
    "long_break": 15
}
```

## Usage

Run the timer with:
```bash
python timer.py
```
You may need to specify the task name and duration as arguments.