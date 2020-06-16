import json
import pathlib
from collections import Mapping, defaultdict

from inflection import parameterize
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files, File
from mkdocs.config import Config
from mkdocs.structure.pages import Page
from typing_extensions import TypedDict


class EmojiCode(TypedDict):
    code: int
    name: str
    description: str
    emoji: str
    category: str


CODES_DIR = pathlib.Path(__file__).parent.resolve() / "emojicodes.json"


class EmojiCodesPlugin(BasePlugin):

    def __init__(self):
        self.codes: Mapping[str, EmojiCode] = json.loads(CODES_DIR.read_text())
        self.codes_by_category = defaultdict(dict)
        for name, code in self.codes.items():
            self.codes_by_category[code['category']][name] = code

    def on_files(self, files: Files, config: Config):
        json_dir = "api"
        (pathlib.Path(config['docs_dir']).resolve() / json_dir).mkdir(parents=True, exist_ok=True)
        for category, codes in self.codes_by_category.items():
            dir = parameterize(f"{category}-responses")
            for name, emojicode in codes.items():
                md_file = File(
                    f"{dir}/{name}.md",
                    config["docs_dir"],
                    config["site_dir"],
                    config["use_directory_urls"]
                )
                files.append(md_file)
                json_file = File(
                    f"{json_dir}/{name}.json",
                    config["docs_dir"],
                    config["site_dir"],
                    config["use_directory_urls"]
                )
                with open(json_file.abs_src_path, "w") as file:
                    json.dump(emojicode, file, indent=2)
                files.append(json_file)
        all_json_file = File(
            f"{json_dir}/all.json",
            config["docs_dir"],
            config["site_dir"],
            config["use_directory_urls"]
        )
        with open(all_json_file.abs_src_path, "w") as file:
            json.dump(self.codes, file, indent=2)

    def on_page_read_source(self, page: Page, config: Config):
        file: File = page.file
        if file.name in self.codes:
            emojicode = self.codes[file.name]
            if "md" in file.src_path:
                description = (
                    f"**Description:** {emojicode['description']}"
                    if emojicode['description'] else ""
                )
                json_path = f"/api/{file.name}.json"
                json_url = f"**JSON URL:** [{json_path}](../{json_path}){{target=_blank}}"
                return (
                    f"# {emojicode['emoji']} - {emojicode['name']}\n\n"
                    f"> **Integer Code:** {emojicode['code']}  \n"
                    f"> {description}  \n"
                    f"> {json_url}"
                )
