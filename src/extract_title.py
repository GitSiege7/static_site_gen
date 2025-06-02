from markdown_to_blocks import markdown_to_blocks

def extract_title(md):
    blocks = markdown_to_blocks(md)

    for block in blocks:
        if block[0] == "#" and block[1] != "#":
            return block[1:].strip()
        
    raise Exception("No h1 header found")