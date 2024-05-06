def fragment_string(string, pieces = 3):
    fragments = []
    
    length = len(string)
    fragment_size = length // pieces

    for piece, i in enumerate(range(0, length, fragment_size)):

        if piece + 1 > pieces:
            fragments.append(fragments.pop(-1) + string[i:])
        else:
            fragments.append(string[i:i+fragment_size])
        
    return fragments

def main():
    print(fragment_string("hello world, yuval", 3))
    
if __name__ == "__main__":
    main()