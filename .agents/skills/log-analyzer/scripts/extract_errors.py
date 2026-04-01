import sys

def process_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '[ERROR]' in line:
                    print(line.rstrip('\n'))
    except FileNotFoundError:
        print(f"Error: Log file not found at {file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing log file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python extract_errors.py <log_file_path>")
        sys.exit(1)
        
    process_log(sys.argv[1])
