import unittest

class Element:
    # represetning an XML Node
    def __init__(self, tag: str = "", value: str = "", attributes: dict[str, str] | None = None, children: list["Element"] | None = None):
        self.tag = tag
        self.value = value
        self.attributes : dict[str, str] = (
                attributes if attributes is not None else {}
        )
        self.children: list["Element"] = (
             children if children is not None else []
        )
        # List of Element type instances

def _encode_single_attribute(
        attributes: dict[str, str], mapping: dict[str, int | str], tokens: list[str]
        ) -> None:
        
        # Helper Encodes single attribute, and the trailing 0 for this attribute
        for key, value in attributes.items():
            tokens.append(str(mapping[key]))
            tokens.append(str(value))
        tokens.append("0")

def _encode_single_element(
        node: Element, mapping: dict[str, str], tokens: list[str]
        ) -> None:
        # helper recursively encodes an XML element node
        
        # 1. Encode TAG
        tokens.append(str(mapping[node.tag]))
        # 2. Encode ATTRIBUTES
        _encode_single_attribute(node.attributes, mapping, tokens)
        # 3. Encode VALUE / CHILDREN
        if node.value:
            tokens.append(str(node.value))
        else:
            for child in node.children:
                _encode_single_element(child, mapping, tokens)

        tokens.append("0")

def encode_xml(root: Element, mapping: dict[str, str]) -> str:
        # Recursive
        # LOOK IT UP: Pre-order XML Serialization

        # Time: O(N), N - number of nodes/attributes
        # space: O(N)
        tokens: list[str] = []
        _encode_single_element(root, mapping, tokens)
        return " ".join(tokens)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestXMLEncoding(unittest.TestCase):

    def test_01_single_element_no_attributes(self):
        """Single element without attributes or children."""
        tag_map = {"root": 1}
        root = Element("root")
        self.assertEqual(encode_xml(root, tag_map), " ".join(["1", "0", "0"]))

    def test_02_element_with_attributes_and_value(self):
        """Element containing attributes and text value."""
        tag_map = {"family": 1, "lastName": 2}
        root = Element("family", attributes={"lastName": "McDowell"}, value="Care")
        self.assertEqual(
            encode_xml(root, tag_map),
            " ".join(["1", "2", "McDowell", "0", "Care", "0"]),
        )

    def test_03_nested_child_elements(self):
        """Encodes nested XML hierarchy correctly."""
        tag_map = {"family": 1, "person": 2, "firstName": 3}
        child = Element("person", attributes={"firstName": "Gayle"}, value="Some Value")
        root = Element("family", children=[child])
        self.assertEqual(
            encode_xml(root, tag_map),
            " ".join(["1", "0", "2", "3", "Gayle", "0", "Some Value", "0", "0"]),
        )

    def test_04_multiple_attributes(self):
        """Encodes element with multiple attributes."""
        tag_map = {"person": 1, "id": 2, "state": 3}
        root = Element("person", attributes={"id": "10", "state": "CA"})
        self.assertEqual(
            encode_xml(root, tag_map),
            " ".join(["1", "2", "10", "3", "CA", "0", "0"])
        )


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.12 - XML Encoding\n{'='*75}")

    passed, failed, errors = 0, 0, 0

    for test in suite:
        test_name = test._testMethodName
        doc = (test._testMethodDoc or "").strip()
        desc = f"{test_name} -> {doc}" if doc else test_name

        result = unittest.TestResult()
        test.run(result)

        if result.wasSuccessful():
            print(f"  ✅ [PASS] {desc}")
            passed += 1
        elif result.failures:
            fail_msg = result.failures[0][1].strip().split("\n")[-1]
            print(f"  ❌ [FAIL] {desc} | {fail_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().split("\n")[-1]
            print(f"  ⚠️  [ERROR] {desc} | {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestXMLEncoding)