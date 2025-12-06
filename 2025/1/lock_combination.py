def read_file():
    file_path = "input.txt"
    current = 50
    ans = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                rotation = line.strip()
                direction = rotation[0]
                turns = int(rotation[1:])
                print(f"turns is {turns}, direction is {direction}")
                if direction == 'L':
                    cycles = turns // 100
                    print(f"cycles is {cycles}")
                    ans += cycles
                    remainder = turns % 100
                    print(f"remainder is {remainder}")
                    if 0 < current <= remainder:
                        ans += 1
                    current = (current - remainder) % 100
                    print(f"current is {current}")
                    print(f"ans is {ans}")
                else:
                    current += turns
                    cycles = current // 100
                    print(f"cycles is {cycles}")
                    remainder = current % 100
                    print(f"remainder is {remainder}")
                    ans += cycles
                    print(f"ans is {ans}")
                    current = remainder

            print(f"ans is {ans}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    read_file()
