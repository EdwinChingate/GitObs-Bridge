src="/path/to/source"
dst="/path/to/target"
mkdir -p "$dst"
for f in "$src"/*.md; do
    base="$(basename "$f" .md)"
    cp "$f" "$dst/$base.js"
done
