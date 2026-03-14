import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props={
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(tag="a", value="This is text", props=props)
        self.assertEqual(
            f'HTMLNode(a, This is text, None,  href="https://www.google.com" target="_blank")',
            repr(node)
        )

    def test_props_to_html_no_props(self):
        node = HTMLNode(value="This is text")
        self.assertEqual(
            f'HTMLNode(None, This is text, None, )',
            repr(node)
        )

    def test_props_to_html2(self):
        props={
            "src": "https://www.google.com/bob.jpeg",
            "alt": "A happy Bob in the sun"
        }
        node = HTMLNode(tag="img", props=props)
        self.assertEqual(
            f'HTMLNode(img, None, None,  src="https://www.google.com/bob.jpeg" alt="A happy Bob in the sun")',
            repr(node)
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Text")
        self.assertEqual(node.to_html(), 'Text')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()


