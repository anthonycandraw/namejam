prefix = ["bev", "tap", "tapt", "data", "logic", "brain", "power", "bright", "grid", "trend", "chart", "flow", "mix", "drip", "shelf", "instant", "auto", "chain", "light", "plug", "source", "stat", "stock", "case", "array", "independent", "shop", "shopper", "consumer", "buyer", "buy", "last", "well"]

suffix = ["data", "insights", "logic", "logics", "logix", "sights", "intelligence", "brain", "power", "alert", "IQ", "reason", "mind", "bright", "matter", "aware", "ware", "wit", "quick", "sage", "wisdom", "wise", "savvy", "graph", "grid", "link", "trend", "trends", "change", "innovation", "cloud", "chart", "stat", "infuse", "fuse", "rich", "enrich", "return", "value", "find", "catch", "search", "hound", "get", "fetch", "track", "rise", "velocity", "swift", "rate", "dispatch", "boost", "raise", "lift", "up", "excel", "surge", "grow", "thrive", "step", "build", "break", "gain", "step", "grade", "skip", "tap", "proof", "proven", "tapt", "tapped", "rich", "full", "flow", "mix", "craft", "drip", "jar", "stock", "case", "shelf", "skim", "instant", "splash", "demand", "onDemand", "stat", "stock", "in", "plug", "source", "buyer", "consumer", "user", "shopper", "shop", "buy", "end", "independent", "purchase", "purchaser", "auto", "chain", "light", "illuminate", "illustrious", "lustre", "shine", "bright", "array", "suite", "call", "still", "distill", "well", "pour"]

exceptions = []

full=["Last Three Feet", "Last 3 Feet", "Last 3 Ft"]

names = []
de_duped = []

def name_combine(first, second):
    list_count = 0

    file = open("bevrage_names.txt", "w")

    for x in first:
        for y in second:
            if x != y:
                names.append(x.title() + y.title())

    for full_name in full:
        names.append(full_name.title())

    names.sort()

    for item in names:
        list_count += 1
        file.write("%s\n" % item)

    file.close()

name_combine(prefix, suffix)
