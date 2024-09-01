import pkg_resources

installed_packages = {pkg.key for pkg in pkg_resources.working_set}

top_level_packages = set()

for dist in pkg_resources.working_set:
    top_level_packages.add(dist.key)
    for req in dist.requires():
        top_level_packages.discard(req.key)

with open('requirements/base.txt', 'w') as f:
    for pkg in sorted(top_level_packages):
        version = pkg_resources.get_distribution(pkg).version
        f.write(f'{pkg}=={version}\n')

print("Top-level requirements written to requirements.txt")
