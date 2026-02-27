import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarization-system"
AUTHOR_USER_NAME = "zaharblank"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "transcendence.499@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Tiny nlp package for text summaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/HELLRAISER3/text-summarization-system",
    project_urls={
        "Bug Tracker": f"https://github.com/HELLRAISER3/text-summarization-system/issues"
    },
    package_dir={"" : "src"},
    packages=setuptools.find_packages(where="src")

)