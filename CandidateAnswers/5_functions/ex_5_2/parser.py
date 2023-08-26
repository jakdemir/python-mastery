#parser.py

def parse_line(line: str):    
    result = line.split('=')

    if len(result) == 2:
        (key, value) = result
        return (key, value)
    else:
        return None

def parser_test():
    (key, value) = parse_line('email=korstsststs@gmail.com')
    print(f'Key is : {key}')
    print(f'Value is : {value}')

    result = parse_line('spam')
    print(result)


# if __name__ == '__main__':
    #parser_test()