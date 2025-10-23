from enum import Enum

class TextType(Enum):
    plain_text = "plain"
    bold_text = "**bold**"
    italic_text = "_italic_"
    code_text = "''code''"
    link_text = "[anchor text](url)"
    image = "![alt text](url)"
    

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, TextNode):
        if self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
