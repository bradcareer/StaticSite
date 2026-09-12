import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props =  {"href": "https://www.google.com"})

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
    def test_props_to_html_multi(self):
        node = HTMLNode(props =  {
        "href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"') 
        
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(
            node.props_to_html(), "")  
            
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "whatever a tags do", props =  {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">whatever a tags do</a>')
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "No tag here!")
        self.assertEqual(node.to_html(), "No tag here!")
        
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )            
    def test_to_html_with_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()


        
if __name__ == "__main__":
    unittest.main()
  