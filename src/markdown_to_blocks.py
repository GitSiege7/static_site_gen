def markdown_to_blocks(markdown):
    blocks = list()
    
    split = markdown.split("\n\n")

    for block in split:
        if block == "":
            continue
        
        block = block.strip("\n")
        blocks.append(block)

    return blocks