import pyfiglet

def print_ascii_title(title):
    # Genera el arte ASCII
    ascii_art = pyfiglet.figlet_format(title)
    
    # Rodea el texto con un marco decorativo
    print("*" * (len(ascii_art.splitlines()[0]) + 4))
    for line in ascii_art.splitlines():
        print(f"* {line} *")
    print("*" * (len(ascii_art.splitlines()[0]) + 4))

# Uso del título
print_ascii_title("Siete y medio\n Diego, Yeray y Marc")
