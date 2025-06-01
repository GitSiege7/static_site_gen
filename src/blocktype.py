from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(block):
    match (block[0]):
        case "#":
            return BlockType.HEADING
        case "`":
            return BlockType.CODE
        case ">":
            return BlockType.QUOTE
        case "-":
            return BlockType.ULIST
        case "1":
            return BlockType.OLIST
        case _:
            return BlockType.PARAGRAPH