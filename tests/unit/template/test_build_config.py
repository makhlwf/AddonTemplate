import unittest
from pathlib import Path
import buildVars


class TestBuildConfig(unittest.TestCase):
	"""Test suite for verifying build configuration and file structure."""

	def test_doc_file_name_is_help_html(self):
		"""Ensure addon_docFileName defaults to help.html."""
		self.assertEqual(buildVars.addon_info["addon_docFileName"], "help.html")

	def test_help_md_exists(self):
		"""Ensure help.md exists in the repository root."""
		self.assertTrue(Path("help.md").is_file(), "help.md must exist in root directory")
