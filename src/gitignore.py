"""Settings for building the gitignore file."""

FOLDER_PATTERN = "[a-zA-Z]*[a-zA-Z]"
FILE_PATTERN = "[a-zA-Z]*[a-zA-Z]"

ALLOW_DIRECTORIES = ["/.github"]
IGNORE_DIRECTORIES = ["/build", "/builds", "/data", "/settings", "log", "logs", "node_modules", "temp", "temporary", "tmp"]
ALLOW_EXTENSIONS = ["md", "txt", "sh", "py", "toml", "yml"]
ALLOW_FILES = [".editorconfig", "Makefile", ".git*[a-z]", "/.mailmap", "/src/tools/hooks/[a-z]*[a-z]"]
IGNORE_FILES = ["*.min.*", "package-lock.json"]

TEXT = """
# Ignore everything
*
# Allow folders (to allow files within folders)
!/**/

# Only allow folders matching this glob
*/
!%(folder_pattern)s/

# Allow these directories
%(allow_directories)s

# Ignore these directories
%(ignore_directories)s

# Allow files matching the following globs with the following extensions
%(allow_extensions)s

# Allow these files
%(allow_files)s

# Ignore these files
%(ignore_files)s
"""