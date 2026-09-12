
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
   
    def to_html(self):
        raise NotImplementedError
        
    def tag_to_html(self):
        if self.tag is None or self.tag == "":
            return ""
        else: 
            return self.tag
            
    def value_to_html(self):
        if self.value is None or self.value == "":
            return ""
        else:
            return self.value
            
    def children_to_html(self):
        if self.children is None or self.children == []:
            return None
        else:
            return self.children
        
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        result = ""
        for new_key,new_val in self.props.items():
            result += f' {new_key}="{new_val}"'
        return result 


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self)->str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self)->str:
        if self.tag is None:
            raise ValueError("No tag found")
        if self.children is None:
            raise ValueError("No children found")
        children_html  = ""
        for child in self.children:
            children_html += child.to_html()
        return (f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>")

