def parse_settings(config_lines):
    settings={}
    for line in config_lines:
        try:
            parts=line.split(":")
            if len(parts) !=2:
                raise IndexError
            
            
            value=int(parts[1])
            if not (0 <= value <= 100 ): 
                  raise ValueError("Out of range")
            settings[parts[0]]=value
        except IndexError:
            print(f"Format error in: {line}")
        except ValueError as e :
            print(f"Invalid value in: {line} ({e})")
    return settings
configs = [
    "volume:80",          # Valid
    "brightness:120",     # Invalid Range
    "difficulty:hard",    # Invalid Type
    "mute",               # Invalid Format (no colon)
    "contrast:50"         # Valid
]
settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")
            
