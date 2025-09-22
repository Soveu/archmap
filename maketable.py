import json

data = {}
with open("archs.json") as f:
    data = json.load(f)

revdata = {}
for k, v in data.items():
    for v2 in v:
        if v2 not in revdata:
            revdata[v2] = set()
        revdata[v2].add(k)


architectures = sorted(data.keys())
extensions = sorted(revdata.keys())

yes = "🟢"
no = "🔴"

# first two lines
print("| x | " + " | ".join(architectures) + " |")
print("| --- |" + (" --- |" * len(architectures)))

def has_ext_f(ext):
    def inner(arch):
        return arch in revdata[ext]

    return inner

def make_cell_f(ext):
    f = has_ext_f(ext)

    def inner(arch):
        if f(arch):
            return yes
        else:
            return no

    return inner

for ext in extensions:
    make_cell = make_cell_f(ext)
    print(f"| {ext} |" + " | ".join(map(make_cell, architectures)) + " |")
